# SQL Queries Library

Common queries:
- Recent leads: SELECT * FROM leads WHERE created_at > NOW() - INTERVAL '30 days';
- Aggregations by source and status

See examples/sql/queries.sql for samples.
