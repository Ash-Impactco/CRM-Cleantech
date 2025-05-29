import os
from typing import Dict, Any
import requests

class NotionConfig:
    def __init__(self):
        """Initialize Notion configuration"""
        self.token = os.getenv('NOTION_TOKEN')
        self.email_db_id = os.getenv('EMAIL_DATABASE_ID')
        self.linkedin_db_id = os.getenv('LINKEDIN_DATABASE_ID')
        
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        
    def create_email_campaign(self, campaign_data: Dict) -> Dict:
        """Create a new email campaign in Notion"""
        payload = {
            "parent": {"database_id": self.email_db_id},
            "properties": {
                "Campaign Name": {"title": [{"text": {"content": campaign_data['name']}}]},
                "Status": {"status": {"name": "Active"}},
                "Lead Score": {"number": campaign_data['lead_score']},
                "ROI": {"number": campaign_data['roi']},
                "Last Follow-up": {"date": {"start": campaign_data['last_followup']}},
                "Conversion Rate": {"number": campaign_data['conversion_rate']}
            }
        }
        
        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers=self.headers,
            json=payload
        )
        return response.json()
        
    def update_linkedin_metrics(self, profile_id: str, metrics: Dict) -> Dict:
        """Update LinkedIn campaign metrics in Notion"""
        payload = {
            "properties": {
                "Connections": {"number": metrics['connections']},
                "Engagements": {"number": metrics['engagements']},
                "Meetings": {"number": metrics['meetings']},
                "Success Rate": {"number": metrics['success_rate']},
                "Target Audience": {"rich_text": [{"text": {"content": metrics['target_audience']}}]}
            }
        }
        
        response = requests.patch(
            f"https://api.notion.com/v1/pages/{profile_id}",
            headers=self.headers,
            json=payload
        )
        return response.json()
        
    def get_campaign_metrics(self, db_id: str, campaign_name: str) -> Dict:
        """Get metrics for a specific campaign"""
        response = requests.post(
            "https://api.notion.com/v1/databases/query",
            headers=self.headers,
            json={
                "database_id": db_id,
                "filter": {
                    "property": "Campaign Name",
                    "rich_text": {
                        "equals": campaign_name
                    }
                }
            }
        )
        return response.json()
        
    def sync_campaign_data(self, campaign_data: Dict, db_id: str) -> Dict:
        """Synchronize campaign data with Notion"""
        existing = self.get_campaign_metrics(db_id, campaign_data['name'])
        
        if existing['results']:
            # Update existing campaign
            campaign_id = existing['results'][0]['id']
            return self.update_linkedin_metrics(campaign_id, campaign_data)
        else:
            # Create new campaign
            return self.create_email_campaign(campaign_data)
        
    def get_all_campaigns(self, db_id: str) -> Dict:
        """Get all campaigns from a database"""
        response = requests.post(
            "https://api.notion.com/v1/databases/query",
            headers=self.headers,
            json={"database_id": db_id}
        )
        return response.json()
