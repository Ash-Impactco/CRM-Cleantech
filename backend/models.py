from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company = Column(String)
    phone = Column(String)
    organization_type = Column(String, nullable=False)  # e.g., "Investor", "Government", "Corporate", "NGO"
    sustainability_score = Column(Integer, default=0)
    status = Column(String, default="new")
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    tasks = relationship("Task", back_populate="lead")
    sustainability_metrics = relationship("SustainabilityMetrics", back_populate="lead", uselist=False)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    description = Column(String)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    lead = relationship("Lead", back_populate="tasks")

class SustainabilityMetrics(Base):
    __tablename__ = "sustainability_metrics"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), unique=True)
    co2_savings = Column(Float, default=0.0)  # kg CO2 saved
    energy_generated = Column(Float, default=0.0)  # kWh
    water_savings = Column(Float, default=0.0)  # liters
    waste_reduction = Column(Float, default=0.0)  # kg
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    lead = relationship("Lead", back_populate="sustainability_metrics")
