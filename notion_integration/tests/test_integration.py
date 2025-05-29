import unittest
from datetime import datetime
from notion_integration.config import NotionConfig
from notion_integration.databases import NotionDatabases


class TestNotionIntegration(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.config = NotionConfig()
        self.databases = NotionDatabases(self.config)
        
        # Test data
        self.test_email_campaign = {
            'name': 'Test Email Campaign',
            'lead_score': 95,
            'roi': 2.5,
            'last_followup': datetime.now().isoformat(),
            'conversion_rate': 0.15,
            'target_audience': ['B2B', 'Enterprise'],
            'industry': 'SaaS',
            'team_member': 'John Doe',
            'notes': 'Test campaign for automation',
            'tags': ['High Priority', 'New']
        }
        
        self.test_linkedin_campaign = {
            'profile_name': 'Test LinkedIn Profile',
            'connections': 50,
            'engagements': 25,
            'meetings': 5,
            'target_audience': 'B2B companies in tech industry',
            'success_rate': 0.8,
            'team_member': 'Jane Smith',
            'notes': 'LinkedIn automation test',
            'tags': ['High Priority']
        }

    def test_create_email_campaign(self):
        """Test creating email campaign"""
        result = self.config.create_email_campaign(self.test_email_campaign)
        self.assertTrue('id' in result)
        self.assertEqual(result['properties']['Campaign Name']['title'][0]['text']['content'],
                         self.test_email_campaign['name'])

    def test_update_linkedin_metrics(self):
        """Test updating LinkedIn metrics"""
        campaign = self.config.create_email_campaign(self.test_email_campaign)
        result = self.config.update_linkedin_metrics(campaign['id'], self.test_linkedin_campaign)
        self.assertTrue('id' in result)
        
    def test_campaign_sync(self):
        """Test campaign synchronization"""
        result = self.config.sync_campaign_data(self.test_email_campaign, self.config.email_db_id)
        self.assertTrue('id' in result)
        
    def test_get_metrics(self):
        """Test getting campaign metrics"""
        metrics = self.config.get_campaign_metrics(self.config.email_db_id, self.test_email_campaign['name'])
        self.assertTrue('results' in metrics)
        
    def test_database_creation(self):
        """Test database creation"""
        result = self.databases.create_database('email_campaigns')
        self.assertTrue('id' in result)
        
    def test_database_query(self):
        """Test database querying"""
        database = self.databases.create_database('email_campaigns')
        query = {
            "filter": {
                "property": "Campaign Name",
                "rich_text": {
                    "equals": self.test_email_campaign['name']
                }
            }
        }
        results = self.databases.query_database(database['id'], query)
        self.assertTrue('results' in results)
        
    def test_error_handling(self):
        """Test error handling"""
        with self.assertRaises(ValueError):
            self.databases.create_database('nonexistent_database')
        
    def test_performance_metrics(self):
        """Test performance metrics tracking"""
        campaign = self.config.create_email_campaign(self.test_email_campaign)
        metrics = self.config.get_campaign_metrics(self.config.email_db_id, self.test_email_campaign['name'])
        self.assertTrue('results' in metrics)
        
    def test_integration_flow(self):
        """Test complete integration flow"""
        # Create campaign
        campaign = self.config.create_email_campaign(self.test_email_campaign)
        
        # Update metrics
        self.config.update_linkedin_metrics(campaign['id'], self.test_linkedin_campaign)
        
        # Get metrics
        metrics = self.config.get_campaign_metrics(self.config.email_db_id, self.test_email_campaign['name'])
        
        # Verify results
        self.assertTrue('results' in metrics)
        self.assertEqual(len(metrics['results']), 1)
        
    def tearDown(self):
        """Clean up test data"""
        # Clean up test campaigns
        pass  # Add cleanup logic here

if __name__ == '__main__':
    unittest.main()
