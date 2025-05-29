import openai
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class AIAssistant:
    def __init__(self):
        self.system_prompt = """You are a Cleantech GrowthLab expert specializing in B2B GTM strategies for clean tech companies.
        Your role is to help craft high-impact communications and optimize growth strategies.
        
        Key principles:
        1. Zero-waste growth focus - maximize ROI while minimizing CAC
        2. B2B Cleantech GTM expertise - understand complex regulatory environments
        3. Long-cycle procurement management - optimize for slow-moving buying groups
        4. Growth playbook integration - align with Cleantech GrowthLab methodologies
        5. Data-driven decision making - use metrics for optimization
        6. Industry-specific customization - tailor to Utilities, Enterprise Sustainability, IPPs, etc.
        7. Scalable solutions - focus on repeatable, transferable processes"""

    def generate_followup_email(self, lead_data: Dict) -> str:
        """Generate a professional follow-up email tailored to the lead's organization type"""
        
        # Tailor the approach based on organization type
        if lead_data['organization_type'] == 'Investor':
            focus = "ROI and financial metrics"
            key_metrics = ["IRR", "NPV", "Payback period"]
        elif lead_data['organization_type'] == 'Government':
            focus = "Policy alignment and public benefit"
            key_metrics = ["Carbon reduction targets", "Energy efficiency", "Public health impact"]
        elif lead_data['organization_type'] == 'Corporate':
            focus = "Corporate sustainability goals"
            key_metrics = ["GHG emissions reduction", "Energy cost savings", "Sustainability reporting"]
        else:  # NGO
            focus = "Impact and scalability"
            key_metrics = ["Community impact", "Environmental restoration", "Social benefits"]

        prompt = f"""Craft a professional follow-up email to {lead_data['name']} at {lead_data['company']}.
        
        Key points:
        1. They are a {lead_data['organization_type']} with a sustainability score of {lead_data['sustainability_score']}
        2. Focus on {focus} and how our solutions align with their goals
        3. Highlight relevant metrics: {', '.join(key_metrics)}
        4. Include specific examples of successful implementations
        5. Suggest a specific next step
        6. Keep it concise (3-4 paragraphs)
        7. End with a clear call-to-action
        8. Sign off professionally
        
        Format:
        Subject: [Your Company] - [Brief, compelling subject line]
        
        [Salutation]
        
        [First paragraph - Connection and context]
        
        [Second paragraph - Value proposition and metrics]
        
        [Third paragraph - Next steps]
        
        [Closing]
        
        [Signature]"""
        
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
