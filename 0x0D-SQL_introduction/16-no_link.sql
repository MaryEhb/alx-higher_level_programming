--  lists all records of the table second_table but no rows without a name value
SELECT score, name FROM second_table WHERE NOT name = NULL ORDER BY score DESC;
