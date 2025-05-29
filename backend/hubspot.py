from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class HubSpotIntegration:
    def __init__(self):
        self.api_client = HubSpot(api_key=os.getenv('HUBSPOT_API_KEY'))
        
    def create_contact(self, lead_data):
        """Create a new contact in HubSpot"""
        try:
            contact = SimplePublicObjectInput(
                properties={
                    'email': lead_data['email'],
                    'firstname': lead_data.get('name', '').split()[0],
                    'lastname': lead_data.get('name', '').split()[-1],
                    'company': lead_data.get('company', ''),
                    'phone': lead_data.get('phone', ''),
                    'organization_type': lead_data.get('organization_type', ''),
                    'sustainability_score': lead_data.get('sustainability_score', 0)
                }
            )
            response = self.api_client.crm.contacts.basic_api.create(contact)
            return response
        except ApiException as e:
            print(f"Error creating contact: {e}")
            return None

    def update_contact(self, contact_id, lead_data):
        """Update an existing contact in HubSpot"""
        try:
            contact = SimplePublicObjectInput(
                properties={
                    'email': lead_data.get('email'),
                    'firstname': lead_data.get('name', '').split()[0],
                    'lastname': lead_data.get('name', '').split()[-1],
                    'company': lead_data.get('company'),
                    'phone': lead_data.get('phone'),
                    'organization_type': lead_data.get('organization_type'),
                    'sustainability_score': lead_data.get('sustainability_score')
                }
            )
            response = self.api_client.crm.contacts.basic_api.update(
                contact_id=contact_id,
                simple_public_object_input=contact
            )
            return response
        except ApiException as e:
            print(f"Error updating contact: {e}")
            return None

    def create_deal(self, lead_data):
        """Create a deal for the lead"""
        try:
            deal = SimplePublicObjectInput(
                properties={
                    'dealname': f"{lead_data['name']} - {lead_data['company']}",
                    'dealstage': 'qualifiedtobuy',
                    'amount': lead_data.get('estimated_value', 0),
                    'closedate': datetime.utcnow().isoformat()
                }
            )
            response = self.api_client.crm.deals.basic_api.create(deal)
            return response
        except ApiException as e:
            print(f"Error creating deal: {e}")
            return None

    def create_task(self, lead_data, task_description):
        """Create a task in HubSpot"""
        try:
            task = SimplePublicObjectInput(
                properties={
                    'hs_task_body': task_description,
                    'hs_task_status': 'NOT_STARTED',
                    'hs_task_priority': 'HIGH',
                    'hs_task_subject': f"Follow up with {lead_data['name']}"
                }
            )
            response = self.api_client.crm.tasks.basic_api.create(task)
            return response
        except ApiException as e:
            print(f"Error creating task: {e}")
            return None
