# hw3

## Commands
```shell


./bin/postmaster -p 14324 -D ./data >logfile 2>&1 &
./bin/createdb hw -p 14324
./bin/psql hw -p 14324
./bin/pg_ctl stop -D ./data -m fast;

```
```sql
CREATE TABLE One(id integer, b integer, c integer, d integer);
CREATE TABLE Two(id integer, a integer);

CREATE TABLE One(
id integer,
b integer,
c integer,
d integer);
CREATE TABLE Two(
id integer,
a integer);

vacuum analyze;


```

## Setup
- Some sample queries to understand the data
```sql
```

## 3
### 3.1
- 