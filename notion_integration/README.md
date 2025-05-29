# Notion Integration Guide

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
