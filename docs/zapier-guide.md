# Zapier Guide

Best practices:
- Use webhook triggers where native integrations are missing.
- Keep steps idempotent by checking for existing records before creating.
- Use Paths & Filters to reduce noise and run steps conditionally.

Example flow: Form -> Formatter -> Airtable -> HubSpot -> Slack
