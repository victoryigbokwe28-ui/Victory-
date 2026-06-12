-- Example SQL queries
-- Recent leads in the last 30 days
SELECT * FROM leads WHERE created_at > NOW() - INTERVAL '30 days';

-- Count leads by source
SELECT source, COUNT(*) FROM leads GROUP BY source ORDER BY 2 DESC;
