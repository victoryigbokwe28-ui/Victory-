

# 🚀 Portfolio | Victory Igbokwe

Welcome to my professional portfolio. I'm an AI automation specialist and workflow engineer focused on applying generative AI, automation platforms, and data systems to solve real business problems.

---

## 📌 Overview

Core areas:
- Prompt Engineering & AI Response Evaluation
- AI Workflow Automation & Integrations
- Generative AI tools (ChatGPT, Claude, Gemini)
- Zapier & Make (Integromat) automation
- Airtable, Notion, HubSpot systems
- Google Workspace, Excel / Google Sheets
- Basic SQL & Python automation
- Loom-based documentation and team training

---

## 🗂️ Repository Structure

- README.md — this overview
- projects/ — project showcases and examples
- docs/ — guides and how-tos
- examples/ — sample exports, scripts, queries
- assets/ — images, diagrams, Loom links placeholders

---

## 🌟 Featured Projects (high level)

1. Prompt Engineering Showcase — Examples and best practices for ChatGPT, Claude, Gemini
2. Zapier Automations — End-to-end business workflows (email -> Airtable -> HubSpot)
3. Make (Integromat) Multi-step Workflows — Advanced orchestration and APIs
4. Airtable Systems — Base schemas, views, automations
5. Notion Workspace Setup — Templates, SOPs, onboarding
6. HubSpot CRM Integrations — Lead capture, enrichment, workflows
7. Data Automation — Python scripts, SQL queries, Sheets automation

---

## 📫 Contact

GitHub: https://github.com/victoryigbokwe28-ui

---

**Last updated:** June 2026
EOF

# projects
mkdir -p projects/prompt-engineering projects/zapier-automation projects/make-automation projects/airtable-systems projects/notion-workspace projects/hubspot-crm projects/data-automation

cat > projects/prompt-engineering/README.md <<'EOF'
# Prompt Engineering Showcase

This project contains prompt patterns, examples, and evaluation guidelines for generative AI models (ChatGPT, Claude, Gemini).

Contents:
- Examples of prompt templates for common tasks (summarization, rewriting, generation, classification)
- Evaluation rubric for model outputs
- Small sandbox with API call examples (no keys included)

See docs/prompt-engineering.md for details.
EOF

cat > projects/zapier-automation/README.md <<'EOF'
# Zapier Automation Examples

This folder contains sample Zap templates, workflow descriptions, and recommended triggers/actions for business automation.

Example workflows:
- Form submission -> Airtable record -> HubSpot contact create -> Slack notification
- New sale in WooCommerce -> Google Sheets row -> Accounting notification

Files:
- workflow-descriptions.md
- sample_zap_export.json (placeholder)

Guides: docs/zapier-guide.md
EOF

cat > projects/make-automation/README.md <<'EOF'
# Make (Integromat) Automation

Guides and sample scenarios for building complex multi-step integrations in Make.

Includes:
- Scenario descriptions
- API examples
- Best practices for error handling and idempotency

See docs/make-guide.md
EOF

cat > projects/airtable-systems/README.md <<'EOF'
# Airtable Systems

A collection of base designs and automation examples for project tracking, CRM, and operations.

Includes:
- Base schema suggestions
- Automation recipes
- Sync patterns with external tools (Zapier/Make)

See docs/airtable-guide.md
EOF

cat > projects/notion-workspace/README.md <<'EOF'
# Notion Workspace Management

Templates and SOPs for building a Notion workspace for teams.

Includes:
- Onboarding template
- Meeting notes and OKR trackers
- Knowledge base structure

See docs/notion-guide.md
EOF

cat > projects/hubspot-crm/README.md <<'EOF'
# HubSpot CRM Examples

Examples of HubSpot workflow setups, contact enrichment flows, and CRM hygiene patterns.

Includes:
- Lead capture through forms
- Lifecycle stage automation
- Syncing contacts to Airtable/Sheets

See docs/hubspot-guide.md
EOF

cat > projects/data-automation/README.md <<'EOF'
# Data Automation

Collection of small Python scripts and SQL queries used for automation tasks, ETL jobs, and reporting.

Files:
- examples/python/automation_example.py
- examples/sql/queries.sql

See docs/python-scripts.md and docs/sql-queries.md
EOF

# docs
mkdir -p docs
cat > docs/prompt-engineering.md <<'EOF'
# Prompt Engineering Guide

This guide covers principles, templates, and evaluation methods for crafting effective prompts across models.

1) Principles
- Be explicit about format, length, and role.  Example: "You are an expert product manager. Produce a 5-bullet feature brief." 
- Provide examples (few-shot) when tasks require specific structure.
- Use step-by-step decomposition for complex reasoning tasks.

2) Prompt Templates
- Summarization:
  "Summarize the text below in 3 short bullet points focusing on outcomes and decisions.\n\nText:\n{input}"

- Classification (with output schema):
  "Classify the following customer feedback into one of: [Feature Request, Bug Report, Praise, Other]. Output JSON: {\"label\":..., \"reason\":...}\n\nFeedback:\n{input}"

3) Evaluation Rubric
- Correctness (0-3)
- Completeness (0-3)
- Conciseness (0-2)
- Tone/Style match (0-2)

Use automated checks where possible: JSON schema validation, token length, and simulated user tests.
EOF

cat > docs/zapier-guide.md <<'EOF'
# Zapier Guide

Best practices:
- Use webhook triggers where native integrations are missing.
- Keep steps idempotent by checking for existing records before creating.
- Use Paths & Filters to reduce noise and run steps conditionally.

Example flow: Form -> Formatter -> Airtable -> HubSpot -> Slack
EOF

cat > docs/make-guide.md <<'EOF'
# Make Guide

Make (Integromat) tips:
- Use routers for branching logic.
- Keep scenario runs small; use iterators for lists.
- Implement error handlers and retry logic.
EOF

cat > docs/airtable-guide.md <<'EOF'
# Airtable Guide

Airtable design patterns:
- Use linked records for normalization.
- Create views for role-specific needs (Ops, Sales, Product).
- Use automations to perform lightweight enrichment and notifications.
EOF

cat > docs/notion-guide.md <<'EOF'
# Notion Guide

Suggestions:
- Use a top-level "Team Home" with links to Projects, Knowledge Base, and SOPs.
- Templates: Meeting note, PRD, Onboarding checklist
- Integrations: embed Loom videos, Sheets, and Airtable views
EOF

cat > docs/hubspot-guide.md <<'EOF'
# HubSpot Guide

HubSpot recommendations:
- Standardize contact properties and lifecycle stages.
- Use workflows for lead scoring and assignment.
- Regularly dedupe and enforce validation on critical properties.
EOF

cat > docs/python-scripts.md <<'EOF'
# Python Scripts Collection

Example automation script: reads a CSV, enriches data, and writes to Airtable via API (no keys included). Replace placeholders with your API keys and secrets.

See examples/python/automation_example.py
EOF

cat > docs/sql-queries.md <<'EOF'
# SQL Queries Library

Common queries:
- Recent leads: SELECT * FROM leads WHERE created_at > NOW() - INTERVAL '30 days';
- Aggregations by source and status

See examples/sql/queries.sql for samples.
EOF

# examples
mkdir -p examples/python examples/sql
cat > examples/python/README.md <<'EOF'
# Automation Example

This is a small Python script that demonstrates reading a CSV, performing a simple transform, and printing results. Replace or extend for real integrations.

Requirements: Python 3.8+
EOF

cat > examples/python/automation_example.py <<'EOF'
import csv

INPUT_CSV = 'data/input.csv'

def transform_row(row):
    # Example transform: normalize email and combine name
    email = row.get('email','').strip().lower()
    name = (row.get('first_name','').strip() + ' ' + row.get('last_name','').strip()).strip()
    return {'name': name, 'email': email}

def main():
    try:
        with open(INPUT_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            out = [transform_row(r) for r in reader]
        for r in out:
            print(r)
    except FileNotFoundError:
        print(f"Place a CSV at {INPUT_CSV} with columns: first_name,last_name,email")

if __name__ == '__main__':
    main()
EOF

cat > examples/sql/queries.sql <<'EOF'
-- Example SQL queries
-- Recent leads in the last 30 days
SELECT * FROM leads WHERE created_at > NOW() - INTERVAL '30 days';

-- Count leads by source
SELECT source, COUNT(*) FROM leads GROUP BY source ORDER BY 2 DESC;
EOF

cat > examples/sample_zap_export.json <<'EOF'
# Placeholder for sample Zap export
{
  "zap": "sample-placeholder",
  "description": "Exported zap schema would go here. Replace with real export from Zapier."
}
EOF

# root files
cat > .gitignore <<'EOF'
.DS_Store
__pycache__/
.env
.env.*
*.pyc
.idea/
.vscode/
node_modules/

# Mac
.DS_Store

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
EOF

cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2026 Victory Igbokwe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

cat > CONTRIBUTING.md <<'EOF'
# Contribution Guidelines

Thank you for checking out this portfolio. If you'd like to contribute or report an issue, open an issue or submit a PR with proposed changes.
EOF

mkdir -p assets
cat > assets/README.md <<'EOF'
# Assets

This folder is reserved for images, diagrams, and Loom links used across documentation. Add files here as needed (SVG/PNG/MP4) and update README docs with embed links.
EOF

echo "Victory portfolio scaffold created in $(pwd)/.. (folder: $ROOT)"
echo "To create a zip: cd .. && zip -r Victory.zip Victory"
echo "To initialize git and push to a remote repo you own:"
echo "  cd Victory"
echo "  git init"
echo "  git add ."
echo "  git commit -m \"Initial Victory portfolio\""
echo "  # create a repo on GitHub first, then add remote and push"
echo "  git remote add origin <your-git-remote-url>"
echo "  git branch -M main"
echo "  git push -u origin main"

After running, you'll have the complete folder ready to upload. I can also:

- Produce a ZIP here by printing it as base64 (larger message) if you prefer a single download file.  
- Make small edits to any file before you upload.  
- Provide a one-line gh CLI command to create the GitHub repo and push (if you want to use the GitHub CLI).

Which would you like next?