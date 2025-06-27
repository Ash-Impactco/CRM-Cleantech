import React from 'react';
import ReactMarkdown from 'react-markdown';
import styles from '../styles/Home.module.css';

const workflow = `# AI Automation Workflow Documentation

## Overview
This documentation outlines the complete AI automation workflow for our Clean Tech CRM system, including email marketing and LinkedIn marketing automation.

## 1. Email Marketing Automation Workflow

### 1.1 Lead Identification
- AI-Powered Lead Scoring
  - Analyzes company data
  - Evaluates sustainability metrics
  - Calculates lead potential
  - Generates lead score

### 1.2 Campaign Creation
- AI Campaign Generator
  - Creates personalized content
  - Generates email templates
  - Sets up automation workflows
  - Configures follow-up sequences

### 1.3 Lead Engagement
- Smart Follow-up System
  - Monitors lead activity
  - Triggers automated responses
  - Adjusts follow-up frequency
  - Tracks engagement metrics

### 1.4 Performance Analysis
- AI Analytics Engine
  - Tracks campaign metrics
  - Analyzes conversion rates
  - Identifies optimization opportunities
  - Generates performance reports

## 2. LinkedIn Marketing Automation Workflow

### 2.1 Profile Optimization
- AI Profile Analyzer
  - Evaluates profile completeness
  - Suggests optimization points
  - Generates content recommendations
  - Monitors engagement metrics

### 2.2 Connection Building
- Smart Connection System
  - Identifies target audience
  - Generates personalized messages
  - Manages connection requests
  - Tracks acceptance rates

### 2.3 Engagement Management
- AI Engagement Engine
  - Monitors network activity
  - Suggests engagement opportunities
  - Automates content sharing
  - Tracks engagement metrics

### 2.4 Meeting Scheduling
- Smart Scheduler
  - Identifies meeting opportunities
  - Sends personalized invitations
  - Manages scheduling conflicts
  - Tracks meeting outcomes

## 3. Combined Workflow Integration

### 3.1 Data Flow
```
Email Marketing → LinkedIn Marketing → Performance Analysis → Optimization
```

### 3.2 AI Integration Points
1. Lead Scoring → Connection Targeting
2. Campaign Metrics → Profile Optimization
3. Engagement Analysis → Follow-up Strategy
4. Performance Data → Workflow Optimization

## 4. Implementation Steps

### 4.1 Initial Setup
1. Configure AI Models
2. Set up Data Integration
3. Define Campaign Parameters
4. Create Initial Templates

### 4.2 Workflow Configuration
1. Set up Lead Scoring Rules
2. Configure Automation Triggers
3. Define Performance Metrics
4. Set up Monitoring Alerts

### 4.3 Optimization Process
1. Analyze Performance Data
2. Adjust AI Parameters
3. Update Campaign Settings
4. Monitor Results

## 5. Technical Architecture

### 5.1 Data Layer
- Lead Database
- Campaign Metrics
- Engagement History
- Performance Analytics

### 5.2 AI Components
- Lead Scoring Model
- Content Generator
- Engagement Analyzer
- Optimization Engine

### 5.3 Integration Points
- HubSpot CRM
- LinkedIn API
- Email Service
- Analytics Platform

## 6. Performance Metrics

### 6.1 Email Marketing
- Open Rate
- Click-through Rate
- Conversion Rate
- Lead Response Time
- ROI Calculation

### 6.2 LinkedIn Marketing
- Connection Rate
- Engagement Rate
- Meeting Conversion
- Response Time
- Pipeline Growth

## 7. Best Practices

### 7.1 Data Management
- Regular Data Cleaning
- Performance Monitoring
- Security Compliance
- Backup Procedures

### 7.2 Workflow Optimization
- Regular Performance Reviews
- AI Model Updates
- Campaign Adjustments
- System Maintenance

### 7.3 Security Measures
- Data Encryption
- Access Controls
- Audit Logging
- Compliance Monitoring

## 8. Maintenance Schedule

### 8.1 Weekly Tasks
- Performance Review
- Data Validation
- System Monitoring
- Backup Verification

### 8.2 Monthly Tasks
- AI Model Updates
- Campaign Optimization
- Security Audit
- Performance Analysis

### 8.3 Quarterly Tasks
- System Audit
- Compliance Check
- Performance Review
- Strategy Update

## 9. Troubleshooting Guide

### 9.1 Common Issues
- Campaign Performance Drop
- AI Model Accuracy Issues
- Integration Errors
- Performance Bottlenecks

### 9.2 Resolution Steps
1. Identify Issue
2. Analyze Data
3. Implement Fix
4. Monitor Results

## 10. Update Log

### Version 1.0.0
- Initial Implementation
- Basic AI Integration
- Email Marketing Setup

### Version 1.1.0
- LinkedIn Integration
- Advanced Analytics
- Performance Optimization
`;

const projectOverview = `# Clean Tech CRM Automation System

A specialized CRM solution for B2B Cleantech companies, built in partnership with Cleantech GrowthLab.

## Key Features

- **Zero-Waste Growth Optimization**
  - Automated pipeline tracking
  - ROI-focused lead scoring
  - Growth playbook integration

- **B2B Cleantech GTM Specialization**
  - Industry-specific lead qualification
  - Regulatory compliance tracking
  - Long-cycle procurement management

- **Integrated Growth Solutions**
  - ABM strategy integration
  - SEO & PPC optimization
  - Marketing automation

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Redis for caching
- Node.js 16+
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/your-repo/clean-tech-crm.git
cd clean-tech-crm
```

2. Install dependencies
```bash
# Backend
pip install -r backend/requirements.txt

# Frontend
npm install
```

3. Configure environment
```bash
cp .env.example .env
# Edit .env with your credentials
```

4. Initialize database
```bash
createdb crm_db
alembic upgrade head
```

5. Start the application
```bash
# Backend
uvicorn backend.main:app --reload

# Frontend
npm run dev
```

## API Documentation

Detailed API documentation is available in [docs/api/api_documentation.md](docs/api/api_documentation.md)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request
4. Include test cases
5. Update documentation

## License

MIT License

## Support

For support, please contact support@cleantechgrowthlab.com or visit our website at https://cleantechgrowthlab.com

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
`;

const apiDocs = `# Clean Tech CRM API Documentation

## Overview

The Clean Tech CRM API is designed specifically for B2B Cleantech companies facing unique GTM challenges. It provides specialized tools for managing complex regulatory environments and long procurement cycles in the cleantech ecosystem.

## Key Features

1. **Zero-Waste Growth Optimization**
   - Automated pipeline tracking
   - ROI-focused lead scoring
   - Customizable growth playbooks integration

2. **B2B Cleantech GTM Specialization**
   - Industry-specific lead qualification
   - Regulatory compliance tracking
   - Long-cycle procurement management

3. **Integrated Growth Solutions**
   - ABM strategy integration
   - SEO & PPC optimization
   - Marketing automation

## API Endpoints

### Lead Management

```http
POST /leads/
```

Create a new lead with specialized B2B cleantech data

Request Body:
```json
{
    "name": "string",
    "email": "string",
    "company": "string",
    "organization_type": "Investor|Government|Corporate|NGO",
    "sustainability_score": integer,
    "regulatory_compliance": {
        "status": "string",
        "requirements": ["string"]
    },
    "procurement_cycle": {
        "estimated_duration": integer,
        "stage": "string"
    }
}
```

### Pipeline Optimization

```http
GET /leads/stats/growth
```

Get growth optimization metrics

Response:
```json
{
    "pipeline_value": {
        "current": number,
        "growth_rate": number
    },
    "conversion_rates": {
        "mql_to_sql": number,
        "sql_to_won": number
    },
    "regulatory_compliance": {
        "pending": number,
        "approved": number,
        "rejected": number
    }
}
```

### Growth Playbook Integration

```http
POST /leads/{id}/playbook
```

Apply growth playbook recommendations

Request Body:
```json
{
    "playbook_id": "string",
    "strategy": {
        "type": "Customer Acquisition|Channel Launch|Channel Optimization",
        "focus_areas": ["string"]
    },
    "implementation_plan": {
        "timeline": ["string"],
        "resources": ["string"]
    }
}
```

## Error Handling

```json
{
    "error": {
        "code": "string",
        "message": "string",
        "details": {
            "validation_errors": ["string"],
            "system_errors": ["string"]
        }
    }
}
```

## Rate Limiting

- 100 requests per minute per API key
- 10,000 requests per day per organization
- Burst limit: 200 requests in 10 seconds

## Authentication

```http
Authorization: Bearer YOUR_API_KEY
```

## Logging and Monitoring

- All API requests are logged
- Performance metrics tracking
- Error rate monitoring
- Usage analytics

## Best Practices

1. **Error Handling**
   - Implement retry logic with exponential backoff
   - Handle rate limiting gracefully
   - Validate responses against schema

2. **Security**
   - Use HTTPS for all requests
   - Rotate API keys regularly
   - Implement proper access controls

3. **Performance**
   - Cache responses where appropriate
   - Use pagination for large datasets
   - Implement proper error handling
`;

const setupGuide = `# Clean Tech CRM Setup Guide

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
`;

const growthlab = `# Cleantech GrowthLab Integration

This directory contains all the integration code and documentation for Cleantech GrowthLab's methodologies and growth optimization strategies.

## Key Components

### 1. Documentation

- [growthlab_integration.md](docs/growthlab_integration.md): Comprehensive guide to integrating with GrowthLab's methodologies
- API documentation: Specialized endpoints for growth optimization
- Configuration guides: Environment variables and setup instructions

### 2. Configuration

- [config.py](config.py): GrowthLab integration configuration
- Environment variables: GrowthLab-specific settings
- Metrics thresholds: Optimization parameters

### 3. Integration Points

1. **Growth Playbook Integration**
   - Zero-Waste Growth Framework
   - ROI-focused lead scoring
   - Customizable growth playbooks

2. **Data Integration**
   - Lead scoring model
   - Growth metrics tracking
   - CAC optimization
   - ROI calculation

3. **API Integration**
   - Specialized endpoints
   - Growth optimization metrics
   - Playbook management

## Setup

1. Create environment variables:
```env
GROWTHLAB_API_KEY=your-key
GROWTHLAB_PLAYBOOK_ID=your-id
GROWTHLAB_STRATEGY=zero-waste
```

2. Configure metrics thresholds:
```env
PIPELINE_VELOCITY_THRESHOLD=0.8
CONVERSION_RATE_THRESHOLD=0.2
CAC_OPTIMIZATION_THRESHOLD=1.5
```

## Usage

1. Initialize GrowthLab configuration:
```python
from growthlab.config import GrowthLabConfig

config = GrowthLabConfig()
metrics = config.get_growth_metrics()
```

2. Generate growth reports:
```python
report = config.generate_growth_report()
recommendations = config.get_growth_recommendations()
```

## Best Practices

1. Regular metric updates
2. Growth strategy alignment
3. Performance monitoring
4. Continuous optimization

## Support

For support with GrowthLab integration, contact:
- Email: support@cleantechgrowthlab.com
- Website: https://cleantechgrowthlab.com
`;

const linkedinMarketing = `# LinkedIn Marketing Integration

This directory contains all the integration code and documentation for Elite Advertising's LinkedIn marketing solution.

## Key Components

### 1. Documentation

- [elite_advertising_integration.md](docs/elite_advertising_integration.md): Comprehensive guide to implementing Elite Advertising's LinkedIn marketing solution
- Case studies and success stories
- Implementation best practices
- Performance metrics and KPIs

### 2. Configuration

- [config.py](config.py): LinkedIn marketing configuration
- Environment variables for LinkedIn API
- Success metrics thresholds
- Package pricing and features

### 3. Integration Points

1. **Automated Relationship Building**
   - Daily activities (connections, likes, messages)
   - Message templates and hooks
   - Target audience optimization

2. **Profile Management**
   - Profile optimization
   - Sales Navigator integration
   - Content strategy

3. **Performance Tracking**
   - Connection rates
   - Engagement metrics
   - Meeting conversion

## Setup

1. Create environment variables:
```env
LINKEDIN_API_KEY=your-key
LINKEDIN_SECRET=your-secret
```

2. Configure LinkedIn profiles:
```python
from linkedin_marketing.config import LinkedInConfig

config = LinkedInConfig()
# Set up daily activities
# Configure message templates
# Define target audience
```

## Usage

1. Initialize configuration:
```python
config = LinkedInConfig()
# Validate target audience
# Get suggested templates
# Calculate package pricing
```

2. Track performance:
```python
metrics = config.get_success_metrics()
activities = config.get_daily_activities()
```

## Best Practices

1. Profile Optimization
   - Regular updates
   - Content strategy
   - Performance monitoring

2. Message Templates
   - A/B testing
   - Personalization
   - Value-based engagement

3. Relationship Building
   - Long-term engagement
   - Value delivery
   - Continuous improvement

## Support

For support with LinkedIn marketing integration:
- Contact Elite Advertising
- Review case studies
- Monitor performance metrics
- Optimize regularly
`;

const notionIntegration = `# Notion Integration Guide

## Overview

This guide provides comprehensive information about integrating the Clean Tech CRM & AI Marketing Automation system with Notion. The integration allows for seamless synchronization of:

1. **Email Marketing Data** (Clean Tech GrowthLab)
2. **LinkedIn Marketing Data** (Elite Advertising)
3. **Project Documentation**
4. **Success Metrics**

## Setup Instructions

### 1. Create Notion Integration

1. Go to Notion Integration page
2. Create a new integration
3. Name it "Clean Tech CRM Integration"
4. Copy the integration token

### 2. Create Notion Databases

#### Email Marketing Database
- Name: "Email Campaigns"
- Properties:
  - Campaign Name
  - Status
  - Lead Score
  - ROI Metrics
  - Last Follow-up
  - Conversion Rate

#### LinkedIn Marketing Database
- Name: "LinkedIn Campaigns"
- Properties:
  - Profile Name
  - Connections
  - Engagements
  - Meetings
  - Target Audience
  - Success Rate

### 3. Add Environment Variables

```env
NOTION_TOKEN=your-integration-token
EMAIL_DATABASE_ID=your-email-database-id
LINKEDIN_DATABASE_ID=your-linkedin-database-id
```

## Integration Features

### 1. Email Marketing Integration

#### Campaign Tracking
- Automatic campaign creation in Notion
- Real-time lead scoring updates
- ROI metric tracking
- Follow-up scheduling

#### Lead Management
- Lead profile synchronization
- Score updates
- Communication history
- Conversion tracking

### 2. LinkedIn Marketing Integration

#### Campaign Management
- Automated profile tracking
- Connection metrics
- Engagement rates
- Meeting scheduling

#### Relationship Building
- Connection history
- Message templates
- Engagement metrics
- Success tracking

## Usage Examples

### Email Marketing

```python
# Create new email campaign in Notion
def create_email_campaign(campaign_data):
    payload = {
        "parent": {"database_id": EMAIL_DATABASE_ID},
        "properties": {
            "Campaign Name": {"title": [{"text": {"content": campaign_data['name']}}]},
            "Status": {"status": {"name": "Active"}},
            "Lead Score": {"number": campaign_data['lead_score']},
            "ROI": {"number": campaign_data['roi']}
        }
    }
    
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=headers,
        json=payload
    )
    return response.json()
```

### LinkedIn Marketing

```python
# Update LinkedIn campaign metrics
def update_linkedin_metrics(profile_id, metrics):
    payload = {
        "properties": {
            "Connections": {"number": metrics['connections']},
            "Engagements": {"number": metrics['engagements']},
            "Meetings": {"number": metrics['meetings']},
            "Success Rate": {"number": metrics['success_rate']}
        }
    }
    
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    response = requests.patch(
        f"https://api.notion.com/v1/pages/{profile_id}",
        headers=headers,
        json=payload
    )
    return response.json()
```

## Success Metrics

### Email Marketing
- Campaign Conversion Rate
- Lead Response Time
- ROI per Campaign
- Follow-up Success Rate

### LinkedIn Marketing
- Connection Rate
- Engagement Rate
- Meeting Conversion
- Pipeline Growth

## Best Practices

1. Regular Database Updates
2. Automated Sync Scheduling
3. Metric Tracking
4. Performance Monitoring

## Support

For Notion integration support:
- Email: support@cleantechgrowthlab.com
- Website: cleantechgrowthlab.com
`;

const presentation = `# Clean Tech CRM & AI Marketing Automation Presentation

This presentation showcases our integrated marketing automation solution with two main components:

1. ## Email Marketing Automation (Clean Tech GrowthLab)
   - AI-powered email campaigns
   - Smart lead scoring
   - Personalized follow-ups
   - ROI tracking

2. ## LinkedIn Marketing Automation (Elite Advertising)
   - Automated relationship building
   - Targeted audience engagement
   - Performance tracking
   - Scalable solutions

## Features

- Modern, responsive design
- Visual placeholders for images
- Clear success metrics
- Pricing information
- Implementation timeline
- Contact information

## How to Use

1. Open index.html in a web browser
2. Replace image placeholders with actual images
3. Customize content as needed
4. Use the presentation for:
   - Client demonstrations
   - Sales presentations
   - Internal training
   - Marketing materials

## Adding Images

1. Place images in the `images` directory
2. Update image placeholders in index.html
3. Supported formats: PNG, JPG, SVG

## Customization

1. Edit content in index.html
2. Modify styling in the <style> section
3. Add new sections as needed
4. Update metrics and statistics

## Support

For support or customization:
- Email: support@cleantechgrowthlab.com
- Website: cleantechgrowthlab.com
`;

const sections = [
  { id: 'workflow', label: 'AI Automation Workflow', content: workflow },
  { id: 'overview', label: 'Project Overview', content: projectOverview },
  { id: 'api', label: 'API Documentation', content: apiDocs },
  { id: 'setup', label: 'Setup Guide', content: setupGuide },
  { id: 'growthlab', label: 'GrowthLab Integration', content: growthlab },
  { id: 'linkedin', label: 'LinkedIn Marketing', content: linkedinMarketing },
  { id: 'notion', label: 'Notion Integration', content: notionIntegration },
  { id: 'presentation', label: 'Presentation', content: presentation },
];

export default function Home() {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>Clean Tech CRM & AI Automation</h1>
        <nav className={styles.navMenu}>
          {sections.map((section) => (
            <a key={section.id} href={`#${section.id}`} className={styles.navLink}>
              {section.label}
            </a>
          ))}
        </nav>
        <div className={styles.documentation}>
          {sections.map((section) => (
            <section key={section.id} id={section.id} className={styles.section}>
              <ReactMarkdown>{section.content}</ReactMarkdown>
            </section>
          ))}
        </div>
      </main>
    </div>
  );
}
