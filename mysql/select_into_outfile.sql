-- MySQL will only allow OUTFILE in the directory
-- specified by the variable secure_file_priv

SHOW VARIABLES LIKE "secure_file_priv";

SELECT * INTO OUTFILE '/var/lib/mysql-files/table_name.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM table_name;

