from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class LeadBase(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = "new"

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    description: str
    due_date: datetime
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    lead_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
