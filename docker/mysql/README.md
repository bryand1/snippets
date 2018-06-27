# MySQL

This docker service uses two bindings to the local host:

+ ./mysql.conf.d - Database configuration (mysqld.cnf should be in this directory)
+ /data/mysql - Database files

Ensure these paths exist locally, or alter the docker-compose.yml to reflect your paths.

Start the database

```bash
docker-compose up -d
```
