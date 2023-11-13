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

### Log in with `postgres`
```
sudo -i -u postgres
postgres@yyh-Macmini:~$ psql
psql (14.9 (Ubuntu 14.9-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# \q
exit
```