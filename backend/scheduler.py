from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from emailer import send_task_reminder
from models import Task
from database import SessionLocal
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def check_pending_tasks():
    """Check for pending tasks and send reminders"""
    db = SessionLocal()
    try:
        # Get tasks due today that haven't been completed
        today = datetime.utcnow().date()
        pending_tasks = db.query(Task).filter(
            Task.due_date >= today,
            Task.completed == False
        ).all()

        for task in pending_tasks:
            # Send reminder email
            lead = db.query(Lead).filter(Lead.id == task.lead_id).first()
            if lead:
                send_task_reminder(lead.email, task.description)
                logger.info(f"Sent reminder for task: {task.description} to {lead.email}")
    finally:
        db.close()

# Schedule the task checker to run daily at 9 AM
scheduler.add_job(
    check_pending_tasks,
    CronTrigger(hour=9, minute=0),
    id="task_reminder",
    name="Check for pending tasks and send reminders"
)

# Start the scheduler
scheduler.start()
