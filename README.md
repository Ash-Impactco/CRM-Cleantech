# Clean Tech CRM Automation System

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