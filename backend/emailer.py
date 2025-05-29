import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def send_followup_email(to_email: str, subject: str, content: str):
    """Send a follow-up email to a lead"""
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = os.getenv('SMTP_FROM_EMAIL')
    msg['To'] = to_email

    try:
        with smtplib.SMTP(os.getenv('SMTP_SERVER', 'smtp.gmail.com'), 587) as server:
            server.starttls()
            server.login(
                os.getenv('SMTP_FROM_EMAIL'),
                os.getenv('SMTP_PASSWORD')
            )
            server.send_message(msg)
            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_task_reminder(to_email: str, task_description: str):
    """Send a reminder email for a pending task"""
    subject = f"Task Reminder: {task_description}"
    content = f"Hello,\n\nThis is a reminder about your pending task: {task_description}\n\nPlease complete this task at your earliest convenience.\n\nBest regards,\nCRM System"
    return send_followup_email(to_email, subject, content)
