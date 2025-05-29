# Clean Tech CRM Setup Guide

## Prerequisites

1. **Technical Requirements**
   - Python 3.9+
   - PostgreSQL 13+
   - Redis for caching
   - Node.js 16+ (for frontend)
   - Git

2. **Business Requirements**
   - HubSpot API credentials
   - OpenAI API key
   - Email service provider credentials
   - Google Analytics account

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-repo/clean-tech-crm.git
cd clean-tech-crm
```

### 2. Set Up Environment

Create a `.env` file with the following variables:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/crm_db

# API Keys
HUBSPOT_API_KEY=your-hubspot-key
OPENAI_API_KEY=your-openai-key
SMTP_SERVER=smtp.gmail.com
SMTP_FROM_EMAIL=your-email@example.com
SMTP_PASSWORD=your-app-specific-password

# GrowthLab Integration
GROWTHLAB_API_KEY=your-growthlab-key
GROWTHLAB_PLAYBOOK_ID=your-playbook-id

# Analytics
ANALYTICS_ID=your-analytics-id
```

### 3. Install Dependencies

```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

### 4. Initialize Database

```bash
# Create database
createdb crm_db

# Run migrations
alembic upgrade head
```

### 5. Start Services

```bash
# Start backend
uvicorn main:app --reload

# Start frontend
npm run dev
```

## Configuration

### Growth Playbook Integration

1. Register at Cleantech GrowthLab
2. Obtain your Playbook ID
3. Configure playbook settings in the admin panel

### HubSpot Integration

1. Create a HubSpot API key
2. Configure lead syncing in settings
3. Set up custom properties

### Email Templates

1. Create templates in HubSpot
2. Configure template IDs in settings
3. Test email delivery

## Usage Examples

### Creating a Lead with Growth Playbook

```python
from api import CRMClient

crm = CRMClient()

lead_data = {
    "name": "John Smith",
    "email": "john@example.com",
    "company": "CleanTech Solutions",
    "organization_type": "Investor",
    "sustainability_score": 85,
    "regulatory_compliance": {
        "status": "pending",
        "requirements": ["ISO 14001", "CARB"]
    },
    "procurement_cycle": {
        "estimated_duration": 180,
        "stage": "Discovery"
    }
}

# Create lead
lead = crm.create_lead(lead_data)

# Apply growth playbook
playbook_data = {
    "playbook_id": "CLEANTECH_ACQUISITION",
    "strategy": {
        "type": "Customer Acquisition",
        "focus_areas": ["SEO", "ABM", "Content Marketing"]
    }
}

playbook_result = crm.apply_playbook(lead.id, playbook_data)
```

## Best Practices

1. **Data Management**
   - Regular database backups
   - Data validation
   - GDPR compliance

2. **Security**
   - Regular API key rotation
   - Environment variable management
   - Access control

3. **Performance**
   - Caching strategies
   - Rate limiting
   - Resource optimization
