---
title: "Install Postgres on Ubuntu"
date: 2023-11-11T20:38:31-05:00
tags: ['postgres', 'Ubuntu']
draft: false
---

## Install Postgres on Ubuntu
### Install
```
sudo apt install postgresql postgresql-contrib -y
```

### Test process
```
ps aux | grep postgres
```

### Start service
If it is not started, start the service. 
```
sudo systemctl start postgresql.service
```

### Log in with `postgres`
```
sudo -i -u postgres
postgres@yyh-Macmini:~$ psql
psql (14.9 (Ubuntu 14.9-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# \q
exit
```
or use the following command to enter.
```
sudo -u postgres psql
```

### Create User Role
If you do not want to switch the account, use 
```
sudo -u postgres createuser --interactive
```
If you are in postgres account, use 
```
createuser --interactive
```

### Create a new database
If you do not want to switch the account, use 
```
sudo -u postgres createdb sammy
```
If you are in postgres account, use 
```
createdb sammy
```

### Use the new user role
```
sudo adduser sammy
```
use 
```shell
sudo -i -u sammy
psql
```
or `sudo -u sammy psql`

If you want to connect a database, use `psql -d postgres`

Use `\conninfo` to check the connection information. 

### List the tables
```
\d
```
or 
```
\dt
```
