
## Table structure
CREATE TABLE Data (
    ID INTEGER PRIMARY KEY,
    A INTEGER,
    B INTEGER,
    C INTEGER);

## script to generate file
```shell

```

## Write 10 queries of the form:
SELECT COUNT(*)
FROM Data
WHERE <some range condition on A,B,C>;

### file ScanQueries.sql
```sql
SELECT COUNT(*) FROM Data WHERE A < 60;
SELECT COUNT(*) FROM Data WHERE B < 30;
SELECT COUNT(*) FROM Data WHERE C > 2;
SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40;
SELECT COUNT(*) FROM Data WHERE A > 35 AND B > 60;
SELECT COUNT(*) FROM Data WHERE A > 30 AND C < 30;
SELECT COUNT(*) FROM Data WHERE B > 20 AND C < 30;
SELECT COUNT(*) FROM Data WHERE A > 5 AND B < 70 AND C > 50;
SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40 AND C > 10;
SELECT COUNT(*) FROM Data WHERE A < 70 AND B < 80 AND C < 90;
```

### file IndexScanQueries.sql
```sql
SELECT COUNT(*) FROM Data WHERE ID > 20;
SELECT COUNT(*) FROM Data WHERE ID < 2000;
SELECT COUNT(*) FROM Data WHERE ID > 4000;
SELECT COUNT(*) FROM Data WHERE ID > 7 AND ID < 200;
SELECT COUNT(*) FROM Data WHERE ID > 20 AND ID < 90;
SELECT COUNT(*) FROM Data WHERE ID > 99 AND ID < 3500;
SELECT COUNT(*) FROM Data WHERE ID > 100 AND ID < 4000;
SELECT COUNT(*) FROM Data WHERE ID > 600 AND ID < 2900;
SELECT COUNT(*) FROM Data WHERE ID > 3500 AND ID < 3600;
SELECT COUNT(*) FROM Data WHERE ID > 4666 AND ID < 4999;
```

### try the queries
- try executing these queries in PostgreSQL , and
- check, using the EXPLAIN command in psql, that they are indeed executed using Sequential Scans or Index Scans, as specified


##