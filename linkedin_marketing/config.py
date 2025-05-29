import os
from typing import Dict, Any

class LinkedInConfig:
    def __init__(self):
        """Initialize LinkedIn marketing configuration"""
        # Profile settings
        self.daily_activities = {
            'connections': 10,
            'likes': 10,
            'messages': 10
        }
        
        # Target audience settings
        self.target_audience = {
            'min_customer_value': 7500,  # EUR
            'min_team_size': 3,
            'industries': [
                'Manufacturing',
                'Service',
                'SaaS'
            ]
        }
        
        # Message templates
        self.message_templates = {
            'meeting': [
                "Free sample/tryout",
                "Free sparring/advice",
                "Showroom visit",
                "Product demonstration"
            ],
            'dialogue': [
                "Problem-solving questions",
                "Industry-specific challenges",
                "Value proposition discussions"
            ],
            'event': [
                "Workshops",
                "Roundtables",
                "Community events",
                "Webinars"
            ],
            'content': [
                "White papers",
                "Sales materials",
                "Case studies",
                "Industry reports"
            ]
        }
        
        # Success metrics
        self.success_metrics = {
            'connection_rate': 80,  # connections/month/profile
            'engagement_rate': 6,  # interests/month/profile
            'meeting_conversion': 1  # meetings/month/profile
        }
        
        # Investment packages
        self.packages = {
            'basic': {
                'price': 10000,  # DKK/month
                'profiles': 1
            },
            'standard': {
                'price': 15000,
                'profiles': 2
            },
            'premium': {
                'price': 19000,
                'profiles': 3
            },
            'enterprise': {
                'price': 35000,
                'profiles': 7
            }
        }
        
    def validate_target_audience(self, company_data: Dict) -> bool:
        """Validate if company meets target audience criteria"""
        return all([
            company_data.get('customer_value', 0) >= self.target_audience['min_customer_value'],
            company_data.get('team_size', 0) >= self.target_audience['min_team_size'],
            company_data.get('industry', '').lower() in map(str.lower, self.target_audience['industries'])
        ])
        
    def get_suggested_template(self, company_type: str) -> str:
        """Get suggested message template based on company type"""
        if company_type.lower() == 'manufacturing':
            return self.message_templates['meeting'][0]
        elif company_type.lower() == 'service':
            return self.message_templates['dialogue'][0]
        elif company_type.lower() == 'saas':
            return self.message_templates['content'][0]
        return self.message_templates['event'][0]
        
    def calculate_package_price(self, num_profiles: int) -> int:
        """Calculate package price based on number of profiles"""
        if num_profiles <= 1:
            return self.packages['basic']['price']
        elif num_profiles <= 2:
            return self.packages['standard']['price']
        elif num_profiles <= 3:
            return self.packages['premium']['price']
        return self.packages['enterprise']['price']
        
    def get_success_metrics(self) -> Dict[str, int]:
        """Get current success metrics"""
        return self.success_metrics
        
    def get_daily_activities(self) -> Dict[str, int]:
        """Get daily activity limits"""
        return self.daily_activities
