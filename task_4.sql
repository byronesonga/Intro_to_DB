SELECT 
    column_name        AS 'Column',
    column_type        AS 'Type',
    is_nullable        AS 'Null',
    column_key         AS 'Key',
    column_default     AS 'Default',
    extra              AS 'Extra'
FROM information_schema.columns
WHERE table_schema = 'songa_database'
  AND table_name   = 'books'
ORDER BY ordinal_position;
