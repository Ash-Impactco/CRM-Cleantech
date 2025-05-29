export const workflowMarkdown = `
# AI Automation Workflow

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
\`\`\`mermaid
graph TD
    A[Lead Identification] --> B{AI Lead Scoring}
    B -->|High Score| C[Email Campaign Creation]
    B -->|Medium Score| D[LinkedIn Connection]
    B -->|Low Score| E[Lead Nurture]

    C --> F[Smart Follow-up System]
    F --> G[Performance Analysis]
    G --> H[Optimization]
    H --> C

    D --> I[Profile Optimization]
    I --> J[Connection Building]
    J --> K[Engagement Management]
    K --> L[Meeting Scheduling]
    L --> G

    H --> M[AI Model Update]
    M --> N[Workflow Optimization]
    N --> O[Performance Monitor]
    O --> H

    subgraph Email Marketing
    C --> F --> G
    end

    subgraph LinkedIn Marketing
    D --> I --> J --> K --> L
    end

    subgraph AI Integration
    B --> C
    B --> D
    B --> E
    G --> H --> M --> N --> O
    end

    subgraph Performance
    G --> H
    L --> G
    O --> H
    end
\`\`\`

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
`;
