from sqlalchemy.orm import Session
from models import Lead, Task
from schemas import LeadCreate, TaskCreate
from datetime import datetime, timedelta
from emailer import send_followup_email

def get_lead_by_email(db: Session, email: str):
    return db.query(Lead).filter(Lead.email == email).first()

def get_lead_by_id(db: Session, lead_id: int):
    return db.query(Lead).filter(Lead.id == lead_id).first()

def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Lead).offset(skip).limit(limit).all()

def create_lead(db: Session, lead: LeadCreate):
    db_lead = Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    
    # Create initial tasks for new lead
    tasks = [
        Task(
            lead_id=db_lead.id,
            description="Initial contact",
            due_date=datetime.utcnow() + timedelta(days=1)
        ),
        Task(
            lead_id=db_lead.id,
            description="Follow-up call",
            due_date=datetime.utcnow() + timedelta(days=3)
        )
    ]
    db.bulk_save_objects(tasks)
    db.commit()
    
    # Send welcome email
    send_followup_email(db_lead.email, "Welcome to our CRM!", "Thank you for your interest!")
    
    return db_lead

def update_lead(db: Session, lead_id: int, lead: LeadCreate):
    db_lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if db_lead:
        for key, value in lead.dict().items():
            setattr(db_lead, key, value)
        db.commit()
        db.refresh(db_lead)
    return db_lead

def delete_lead(db: Session, lead_id: int):
    db_lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if db_lead:
        db.delete(db_lead)
        db.commit()
