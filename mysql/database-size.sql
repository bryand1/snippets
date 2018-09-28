# https://makandracards.com/makandra/39413-mysql-mariadb-show-disk-usage-of-tables-and-columns

# You can find out about disk space usage of all tables within your database by running this
SELECT table_name AS `Table`, round(((data_length + index_length) / 1024 / 1024), 2) `Size (MB)` FROM information_schema.TABLES WHERE table_schema = "$your_database";

# To find out disk usage of a single column
SELECT sum(char_length($your_column))/1024/1024 FROM $your_table
