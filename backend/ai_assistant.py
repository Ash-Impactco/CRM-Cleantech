import openai
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class AIAssistant:
    def __init__(self):
        self.system_prompt = """You are an AI assistant for a clean tech CRM system. 
        Your role is to help generate personalized follow-up emails and analyze leads.
        Focus on sustainability metrics and clean tech benefits in your responses."""

    def generate_followup_email(self, lead_data: Dict) -> str:
        """Generate a personalized follow-up email for a lead"""
        prompt = f"""Write a follow-up email to {lead_data['name']} at {lead_data['company']}.
        They are a {lead_data['organization_type']} with a sustainability score of {lead_data['sustainability_score']}.
        Focus on how our clean tech solutions can help them achieve their sustainability goals.
        Include relevant metrics like CO2 reduction and energy savings.
        Keep it friendly, professional, and informative."""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content

    def analyze_lead(self, lead_data: Dict) -> Dict:
        """Analyze lead data and provide insights"""
        prompt = f"""Analyze this lead:
        Name: {lead_data['name']}
        Company: {lead_data['company']}
        Organization Type: {lead_data['organization_type']}
        Sustainability Score: {lead_data['sustainability_score']}
        
        Provide insights about:
        1. Potential value proposition
        2. Recommended next steps
        3. Relevant sustainability metrics to highlight
        
        Return a JSON object with these insights."""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        try:
            return eval(response.choices[0].message.content)
        except:
            return {"error": "Failed to parse AI response"}

    def generate_task_description(self, lead_data: Dict) -> str:
        """Generate a task description for follow-up"""
        prompt = f"""Generate a follow-up task description for {lead_data['name']} at {lead_data['company']}.
        They are a {lead_data['organization_type']} with a sustainability score of {lead_data['sustainability_score']}.
        Include key talking points about our clean tech solutions and sustainability benefits."""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
