from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from schemas import LeadCreate, Lead
from crud import create_lead, get_leads, get_lead_by_email
from typing import List, Dict
import uvicorn
from hubspot import HubSpotIntegration
from ai_assistant import AIAssistant

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Clean Tech CRM Automation System",
    description="Specialized CRM for B2B Cleantech companies with integrated growth optimization",
    version="1.0.0",
    contact={
        "name": "Cleantech GrowthLab",
        "url": "https://cleantechgrowthlab.com",
        "email": "support@cleantechgrowthlab.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize integrations
hubspot = HubSpotIntegration()
ai_assistant = AIAssistant()

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/leads/", response_model=Dict)
def create_lead_route(lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = get_lead_by_email(db, email=lead.email)
    if db_lead:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create lead in local DB
    lead_data = create_lead(db=db, lead=lead)
    
    # Create in HubSpot
    hubspot_response = hubspot.create_contact(lead_data.dict())
    if hubspot_response:
        lead_data.hubspot_id = hubspot_response.id
        db.commit()
        db.refresh(lead_data)
    
    # Generate AI insights
    ai_insights = ai_assistant.analyze_lead(lead_data.dict())
    
    return {
        "lead": lead_data,
        "hubspot_status": "success" if hubspot_response else "failed",
        "ai_insights": ai_insights
    }

@app.get("/leads/", response_model=List[Dict])
def read_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = get_leads(db, skip=skip, limit=limit)
    return [{
        "lead": lead,
        "ai_analysis": ai_assistant.analyze_lead(lead.dict())
    } for lead in leads]

@app.get("/leads/{lead_id}", response_model=Dict)
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    return {
        "lead": db_lead,
        "ai_analysis": ai_assistant.analyze_lead(db_lead.dict())
    }

@app.put("/leads/{lead_id}", response_model=Dict)
def update_lead(lead_id: int, lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    # Update local DB
    updated_lead = update_lead(db=db, lead_id=lead_id, lead=lead)
    
    # Update HubSpot
    if db_lead.hubspot_id:
        hubspot.update_contact(db_lead.hubspot_id, lead.dict())
    
    return {
        "lead": updated_lead,
        "hubspot_status": "success"
    }

@app.delete("/leads/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    # Delete from HubSpot
    if db_lead.hubspot_id:
        # HubSpot API doesn't have a direct delete method, so we'll just mark it as inactive
        hubspot.update_contact(db_lead.hubspot_id, {'email': f"deleted_{db_lead.email}"})
    
    # Delete from local DB
    delete_lead(db=db, lead_id=lead_id)
    
    return {"detail": "Lead deleted successfully"}

@app.post("/leads/{lead_id}/followup")
def generate_followup(lead_id: int, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    
    # Generate follow-up email
    email_content = ai_assistant.generate_followup_email(db_lead.dict())
    
    # Create task in HubSpot
    task_description = ai_assistant.generate_task_description(db_lead.dict())
    if db_lead.hubspot_id:
        hubspot.create_task(db_lead.dict(), task_description)
    
    return {
        "email_content": email_content,
        "task_description": task_description
    }

@app.get("/leads/stats")
def get_leads_stats(db: Session = Depends(get_db)):
    """Get statistics about leads"""
    leads = get_leads(db)
    stats = {
        "total_leads": len(leads),
        "by_organization_type": {},
        "average_sustainability_score": 0,
        "total_impact": {
            "co2_savings": 0,
            "energy_generated": 0,
            "water_savings": 0,
            "waste_reduction": 0
        }
    }
    
    for lead in leads:
        if lead.organization_type in stats["by_organization_type"]:
            stats["by_organization_type"][lead.organization_type] += 1
        else:
            stats["by_organization_type"][lead.organization_type] = 1
        
        stats["average_sustainability_score"] += lead.sustainability_score
        
        if lead.sustainability_metrics:
            stats["total_impact"]["co2_savings"] += lead.sustainability_metrics.co2_savings
            stats["total_impact"]["energy_generated"] += lead.sustainability_metrics.energy_generated
            stats["total_impact"]["water_savings"] += lead.sustainability_metrics.water_savings
            stats["total_impact"]["waste_reduction"] += lead.sustainability_metrics.waste_reduction
    
    if leads:
        stats["average_sustainability_score"] /= len(leads)
    
    return stats

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
