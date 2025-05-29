from typing import Dict, List, Any

class NotionDatabases:
    def __init__(self, config):
        self.config = config
        self.databases = {
            'email_campaigns': {
                'name': 'Email Campaigns',
                'properties': {
                    'Campaign Name': {'title': {}},
                    'Status': {'status': {'options': ['Active', 'Paused', 'Completed']}},
                    'Lead Score': {'number': {}},
                    'ROI': {'number': {}},
                    'Last Follow-up': {'date': {}},
                    'Conversion Rate': {'number': {}},
                    'Target Audience': {'multi_select': {'options': ['B2B', 'B2C', 'Enterprise']}},
                    'Industry': {'select': {'options': ['Manufacturing', 'Service', 'SaaS']}},
                    'Team Member': {'people': {}},
                    'Notes': {'rich_text': {}},
                    'Tags': {'multi_select': {'options': ['High Priority', 'New', 'Follow-up Needed']}},
                    'Created': {'created_time': {}},
                    'Last Updated': {'last_edited_time': {}},
                    'Attachments': {'files': {}},
                    'Related Campaigns': {'relation': {}},
                    'Custom Fields': {'rich_text': {}},
                    'Automation Status': {'status': {'options': ['Pending', 'Running', 'Completed', 'Error']}},
                    'Error Log': {'rich_text': {}},
                    'Metrics': {
                        'object': 'database_property',
                        'type': 'rollup',
                        'rollup': {
                            'rollup_property_name': 'Lead Score',
                            'relation_property_name': 'Related Campaigns',
                            'function': 'average'
                        }
                    }
                }
            },
            'linkedin_campaigns': {
                'name': 'LinkedIn Campaigns',
                'properties': {
                    'Profile Name': {'title': {}},
                    'Connections': {'number': {}},
                    'Engagements': {'number': {}},
                    'Meetings': {'number': {}},
                    'Target Audience': {'rich_text': {}},
                    'Success Rate': {'number': {}},
                    'Automation Status': {'status': {'options': ['Active', 'Paused', 'Error']}},
                    'Last Activity': {'date': {}},
                    'Team Member': {'people': {}},
                    'Notes': {'rich_text': {}},
                    'Tags': {'multi_select': {'options': ['High Priority', 'New', 'Follow-up Needed']}},
                    'Created': {'created_time': {}},
                    'Last Updated': {'last_edited_time': {}},
                    'Attachments': {'files': {}},
                    'Related Campaigns': {'relation': {}},
                    'Custom Fields': {'rich_text': {}},
                    'Error Log': {'rich_text': {}},
                    'Metrics': {
                        'object': 'database_property',
                        'type': 'rollup',
                        'rollup': {
                            'rollup_property_name': 'Engagements',
                            'relation_property_name': 'Related Campaigns',
                            'function': 'average'
                        }
                    }
                }
            },
            'success_metrics': {
                'name': 'Success Metrics',
                'properties': {
                    'Metric Name': {'title': {}},
                    'Type': {'select': {'options': ['Lead', 'ROI', 'Conversion', 'Engagement']}},
                    'Value': {'number': {}},
                    'Target': {'number': {}},
                    'Status': {'status': {'options': ['Good', 'Warning', 'Critical']}},
                    'Trend': {'select': {'options': ['Up', 'Down', 'Stable']}},
                    'Period': {'select': {'options': ['Daily', 'Weekly', 'Monthly', 'Quarterly']}},
                    'Team Member': {'people': {}},
                    'Notes': {'rich_text': {}},
                    'Created': {'created_time': {}},
                    'Last Updated': {'last_edited_time': {}},
                    'Attachments': {'files': {}},
                    'Related Metrics': {'relation': {}},
                    'Custom Fields': {'rich_text': {}},
                    'Error Log': {'rich_text': {}},
                    'Metrics': {
                        'object': 'database_property',
                        'type': 'rollup',
                        'rollup': {
                            'rollup_property_name': 'Value',
                            'relation_property_name': 'Related Metrics',
                            'function': 'average'
                        }
                    }
                }
            },
            'automation_logs': {
                'name': 'Automation Logs',
                'properties': {
                    'Log ID': {'title': {}},
                    'Campaign Type': {'select': {'options': ['Email', 'LinkedIn']}},
                    'Campaign Name': {'rich_text': {}},
                    'Status': {'status': {'options': ['Success', 'Error', 'Warning']}},
                    'Error Message': {'rich_text': {}},
                    'Timestamp': {'date': {}},
                    'Team Member': {'people': {}},
                    'Notes': {'rich_text': {}},
                    'Created': {'created_time': {}},
                    'Last Updated': {'last_edited_time': {}},
                    'Attachments': {'files': {}},
                    'Related Logs': {'relation': {}},
                    'Custom Fields': {'rich_text': {}},
                    'Error Log': {'rich_text': {}},
                    'Metrics': {
                        'object': 'database_property',
                        'type': 'rollup',
                        'rollup': {
                            'rollup_property_name': 'Status',
                            'relation_property_name': 'Related Logs',
                            'function': 'count'
                        }
                    }
                }
            }
        }

    def create_database(self, database_name: str) -> Dict:
        """Create a new database in Notion"""
        database = self.databases.get(database_name)
        if not database:
            raise ValueError(f"Database {database_name} not found")

        payload = {
            "parent": {"type": "workspace"},
            "title": [{"text": {"content": database['name']}}],
            "properties": database['properties']
        }

        response = requests.post(
            "https://api.notion.com/v1/databases",
            headers=self.config.headers,
            json=payload
        )
        return response.json()

    def get_database(self, database_name: str) -> Dict:
        """Get database information from Notion"""
        database = self.databases.get(database_name)
        if not database:
            raise ValueError(f"Database {database_name} not found")

        response = requests.get(
            "https://api.notion.com/v1/databases",
            headers=self.config.headers
        )
        return response.json()

    def update_database(self, database_id: str, updates: Dict) -> Dict:
        """Update database properties"""
        response = requests.patch(
            f"https://api.notion.com/v1/databases/{database_id}",
            headers=self.config.headers,
            json=updates
        )
        return response.json()

    def query_database(self, database_id: str, query: Dict) -> Dict:
        """Query database with specific filters"""
        response = requests.post(
            f"https://api.notion.com/v1/databases/{database_id}/query",
            headers=self.config.headers,
            json=query
        )
        return response.json()
