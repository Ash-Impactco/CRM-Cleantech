# CRM-Cleantech

## CRM Automation System

A full-stack CRM system with automated lead management and follow-up capabilities.

## Features

- Lead management (Create, Read, Update, Delete)
- Automated task creation for new leads
- Email follow-up automation
- RESTful API endpoints
- SQLite database with SQLAlchemy ORM
- Background task scheduling

## Setup Instructions

1. Clone the repository
2. Install dependencies:
```bash
pip install -r backend/requirements.txt
```

3. Configure environment variables:
- Copy `backend/.env.example` to `backend/.env`
- Update SMTP credentials in `.env` file

4. Run the backend server:
```bash
cd backend
uvicorn main:app --reload
```

## API Endpoints

- `POST /leads/` - Create a new lead
- `GET /leads/` - List all leads
- `GET /leads/{lead_id}` - Get specific lead
- `PUT /leads/{lead_id}` - Update lead
- `DELETE /leads/{lead_id}` - Delete lead

## Database

The system uses SQLite as the database. The database file will be created automatically at `backend/crm.db`.

## Email Configuration

To enable email functionality, configure the following in your `.env` file:
- `SMTP_SERVER`: SMTP server address
- `SMTP_FROM_EMAIL`: Sender email address
- `SMTP_PASSWORD`: App-specific password for SMTP authentication

## License

MIT License