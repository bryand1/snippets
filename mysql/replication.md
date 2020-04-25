## MySQL Replication

On master server:

```
sudo systemctl stop mysql
```

Edit master MySQL Database my.cnf

```
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
```

Start MySQL again and create repl user account and grant permission

```
CREATE USER 'repl'@'[IP_ADDR_SLAVE]' IDENTIFIED BY '[SLAVEPASSWORD]';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'[IP_ADDR_SLAVE]';
```

Export database using mysqldump
`--master-data` is required in order to maintain log position

```
mysqldump -uroot -p --all-database --master-data > masterdump.sql
```

Edit the settings in the slave VM

```
server-id = 2
```

```
CHANGE MASTER TO MASTER_HOST='[IP_ADDR_MASTER]', MASTER_USER='repl', MASTER_PASSWORD='[SLAVEPASSWORD]';
```

Copy mysqldump file to slave VM
Load the mysqldump into the installed MySQL database

```
mysql > start slave;
        show slave status\G
```
