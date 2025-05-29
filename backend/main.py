from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from schemas import LeadCreate, Lead
from crud import create_lead, get_leads, get_lead_by_email
from typing import List
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM Automation System")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/leads/", response_model=Lead)
def create_lead_route(lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = get_lead_by_email(db, email=lead.email)
    if db_lead:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_lead(db=db, lead=lead)

@app.get("/leads/", response_model=List[Lead])
def read_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = get_leads(db, skip=skip, limit=limit)
    return leads

@app.get("/leads/{lead_id}", response_model=Lead)
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return db_lead

@app.put("/leads/{lead_id}", response_model=Lead)
def update_lead(lead_id: int, lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return update_lead(db=db, lead_id=lead_id, lead=lead)

@app.delete("/leads/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = get_lead_by_id(db, lead_id=lead_id)
    if db_lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    delete_lead(db=db, lead_id=lead_id)
    return {"detail": "Lead deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
