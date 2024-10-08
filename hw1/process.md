# CSCD43 HW1 Process
## Table structure
```sql
CREATE TABLE Data (
    ID INTEGER PRIMARY KEY,
    A INTEGER,
    B INTEGER,
    C INTEGER);
```

## script to generate file
- file name: generate_data.sh
```shell
#!/bin/bash

# Define the output file
outputFile="data.csv"

# Generate 5000 lines of data
for id in {1..5000}
do
  # Generate random numbers between 1 and 100 for A, B, and C
  a=$((RANDOM % 100 + 1))
  b=$((RANDOM % 100 + 1))
  c=$((RANDOM % 100 + 1))

  # Append the data to the file
  echo "${id},${a},${b},${c}" >> "$outputFile"
done

echo "Data generation complete. File: $outputFile"

```
- git permission
```shell
chmod +x generate_data.sh
./generate_data.sh
```
- in database:
```sql

copy Data(ID, A, B, C) from '/cmshome/xuzhitao/cscd43/hw1_github_repo/data.csv' delimiter ',';
```
- check
```sql
SELECT COUNT(*) FROM Data;
SELECT * FROM Data;
```

## Write 10 queries of the form:
SELECT COUNT(*)
FROM Data
WHERE <some range condition on A,B,C>;

### file ScanQueries.sql
```sql
-- Select
SELECT COUNT(*) FROM Data WHERE A < 60;
 count 
-------
  2949
(1 row)
SELECT COUNT(*) FROM Data WHERE B < 30;
 count 
-------
  1446
(1 row)
SELECT COUNT(*) FROM Data WHERE C > 2;
 count 
-------
  4910
(1 row)
SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40;
 count 
-------
  1544
(1 row)
SELECT COUNT(*) FROM Data WHERE A > 35 AND B > 60;
 count 
-------
  1281
(1 row)
SELECT COUNT(*) FROM Data WHERE A > 30 AND C < 30;
 count 
-------
   981
(1 row)
SELECT COUNT(*) FROM Data WHERE B > 20 AND C < 30;
 count 
-------
  1120
(1 row)
SELECT COUNT(*) FROM Data WHERE A > 5 AND B < 70 AND C > 50;
 count 
-------
  1629
(1 row)
SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40 AND C > 10;
 count 
-------
  1382
(1 row)
SELECT COUNT(*) FROM Data WHERE A < 70 AND B < 80 AND C < 90;
 count 
-------
  2456
(1 row)

-- Explain
EXPLAIN SELECT COUNT(*) FROM Data WHERE A < 60;
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=23.34..23.34 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..22.50 rows=334 width=0)
         Filter: (a < 60)
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE B < 30;
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=23.34..23.34 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..22.50 rows=334 width=0)
         Filter: (b < 30)
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE C > 2;
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=23.34..23.34 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..22.50 rows=334 width=0)
         Filter: (c > 2)
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40;
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=25.28..25.28 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..25.00 rows=112 width=0)
         Filter: ((a > 20) AND (b < 40))
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 35 AND B > 60; 
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=25.28..25.28 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..25.00 rows=112 width=0)
         Filter: ((a > 35) AND (b > 60))
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 30 AND C < 30; 
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=25.28..25.28 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..25.00 rows=112 width=0)
         Filter: ((a > 30) AND (c < 30))
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE B > 20 AND C < 30;
                         QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=25.28..25.28 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..25.00 rows=112 width=0)
         Filter: ((b > 20) AND (c < 30))

EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 5 AND B < 70 AND C > 50;
                         QUERY PLAN                         
------------------------------------------------------------
 Aggregate  (cost=27.60..27.60 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..27.50 rows=38 width=0)
         Filter: ((a > 5) AND (b < 70) AND (c > 50))

EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40 AND C > 10;
                         QUERY PLAN                         
------------------------------------------------------------
 Aggregate  (cost=27.60..27.60 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..27.50 rows=38 width=0)
         Filter: ((a > 20) AND (b < 40) AND (c > 10))
(3 rows)

EXPLAIN SELECT COUNT(*) FROM Data WHERE A < 70 AND B < 80 AND C < 90; 
                         QUERY PLAN                         
------------------------------------------------------------
 Aggregate  (cost=27.60..27.60 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..27.50 rows=38 width=0)
         Filter: ((a < 70) AND (b < 80) AND (c < 90))
(3 rows)

```

### file IndexScanQueries.sql
```sql
-- Select
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

-- Explain
Explain SELECT COUNT(*) FROM Data WHERE ID > 20;
test=#                          QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=23.34..23.34 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..22.50 rows=334 width=0)
         Filter: (id > 20)
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID < 2000;
test=#                          QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=23.34..23.34 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..22.50 rows=334 width=0)
         Filter: (id < 2000)
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 4000;
test=#                          QUERY PLAN                          
-------------------------------------------------------------
 Aggregate  (cost=23.34..23.34 rows=1 width=0)
   ->  Seq Scan on data  (cost=0.00..22.50 rows=334 width=0)
         Filter: (id > 4000)
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 7 AND ID < 200;
test=#                                  QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 7) AND (id < 200))
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 20 AND ID < 90;
test=#                                  QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 20) AND (id < 90))
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 99 AND ID < 3500;
test=#                                  QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 99) AND (id < 3500))
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 100 AND ID < 4000;
test=#                                  QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 100) AND (id < 4000))
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 600 AND ID < 2900;
test=#                                  QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 600) AND (id < 2900))
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 3500 AND ID < 3600;
test=#                                  QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 3500) AND (id < 3600))
(3 rows)

Explain SELECT COUNT(*) FROM Data WHERE ID > 4666 AND ID < 4999;
test=# 
                                 QUERY PLAN                                  
-----------------------------------------------------------------------------
 Aggregate  (cost=17.10..17.10 rows=1 width=0)
   ->  Index Scan using data_pkey on data  (cost=0.00..17.08 rows=5 width=0)
         Index Cond: ((id > 4666) AND (id < 4999))
(3 rows)

```

### try the queries
- try executing these queries in PostgreSQL , and
- check, using the EXPLAIN command in psql, that they are indeed executed using Sequential Scans or Index Scans, as specified
- Some use index scans, some use sequential scans


## postgres in backend mode
- 
```shell
cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test

# to a file
cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > scan.log 2>&1
cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > indexscan.log 2>&1
```

## LRU commands:
```shell
mkdir -p ./logs/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/20_scan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/30_scan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/50_scan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/100_scan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 150 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/150_scan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/200_scan.log 2>&1 && 

mkdir -p ./logs/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/20_indexscan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/30_indexscan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/50_indexscan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/100_indexscan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 150 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/150_indexscan.log 2>&1 && \
mkdir -p ./logs/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lru/200_indexscan.log 2>&1 && 
```

## MRU result:
```shell
mkdir -p ./logs/mru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/20_scan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/30_scan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/50_scan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/100_scan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 150 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/150_scan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/200_scan.log 2>&1 

mkdir -p ./logs/mru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/20_indexscan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/30_indexscan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/50_indexscan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/100_indexscan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 150 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/150_indexscan.log 2>&1 && \
mkdir -p ./logs/mru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/mru/200_indexscan.log 2>&1 
```

## LFU result:
```shell
mkdir -p ./logs/lfu/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/20_scan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/30_scan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/50_scan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/100_scan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 150 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/150_scan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/200_scan.log 2>&1 &&

mkdir -p ./logs/lfu/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/20_indexscan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/30_indexscan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/50_indexscan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/100_indexscan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 150 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/150_indexscan.log 2>&1 && \
mkdir -p ./logs/lfu/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs/lfu/200_indexscan.log 2>&1 &&
```

## Files to change
- The files which will most likely need the most are:
- freelist.c
	- it manages pages which are not pinned in memory and are eligible for replacement.
- bufmgr.c
	- it defines the interface used by the rest of PostgreSQL to access the memory buffer.
- buf_init.c
	- it handles initializations of the buffer manager data structures.
- buf_internals.h
	- it defines the data structures used by the rest of the buffer manager.


## Ideas to change from lru to mru and lfu
- lru (original one)
	- least recently used buffer
	- [1, 2, 3, 4]
	- want 5 in, take 1 out
- mru
	- most recently used buffer
	- [1, 2, 3, 4]
	- want 5 in, take 4 out
	- change the algo of chose the oldest to chose the earliest
- lfu
	- least frequently used buffer
	- [1, 2, 3, 4]
	- want 5 in, take the one used least out
	- will need a counter on the time of used

## Commands
```shell
gmake clean && gmake uninstall && gmake && gmake install

gmake clean
gmake uninstall
gmake
gmake install
```



## new sql statements
```sql
-- Sequential Scan Queries (First 10):
-- Aim to vary access to different portions of the table and combine broad with specific conditions.

SELECT COUNT(*) FROM Data WHERE A < 50; (Broad range, touching many rows)
SELECT COUNT(*) FROM Data WHERE B % 10 = 0; (Selective, touching rows sporadically)
SELECT COUNT(*) FROM Data WHERE C BETWEEN 10 AND 20; (Specific range)
SELECT COUNT(*) FROM Data WHERE A > 25 AND B > 50 AND C < 75; (Mixed conditions)
SELECT COUNT(*) FROM Data WHERE A % 5 = 0 AND C % 5 = 0; (Selective on two columns)
SELECT COUNT(*) FROM Data WHERE A < 20 OR B > 80; (Combining less and more frequent data)
SELECT COUNT(*) FROM Data WHERE C > 90; (Highly selective)
SELECT COUNT(*) FROM Data WHERE A BETWEEN 40 AND 60; (Mid-range selectivity)
SELECT COUNT(*) FROM Data WHERE B < 25 OR C > 75; (Diverse data access)
SELECT COUNT(*) FROM Data WHERE A < 10 OR A > 90; (Edge conditions, possibly touching less cached data)

-- Index Scan Queries (Next 10):
-- Focus on varying the ID range and patterns to exploit index caching differences.
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 10 AND 50; (Small range, frequent access)
SELECT COUNT(*) FROM Data WHERE ID % 100 = 0; (Sporadic access across the table)
SELECT COUNT(*) FROM Data WHERE ID > 2500 AND ID < 2600; (Narrow range, middle of the table)
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 1 AND 1000; (Broad range)
SELECT COUNT(*) FROM Data WHERE ID % 2 = 0; (Every other row, promoting cache churn)
SELECT COUNT(*) FROM Data WHERE ID < 500 OR ID > 4500; (Edge conditions)
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 2000 AND 3000; (Mid-table focus)
SELECT COUNT(*) FROM Data WHERE ID % 500 = 0; (Specific, sporadic IDs)
SELECT COUNT(*) FROM Data WHERE ID > 1000 AND ID < 1500; (Narrow range, early table)
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 300 AND 600; (Small range, early table)
```
- sql without statement
```sql
SELECT COUNT(*) FROM Data WHERE A < 50;
SELECT COUNT(*) FROM Data WHERE B % 10 = 0;
SELECT COUNT(*) FROM Data WHERE C BETWEEN 10 AND 20;
SELECT COUNT(*) FROM Data WHERE A > 25 AND B > 50 AND C < 75;
SELECT COUNT(*) FROM Data WHERE A % 5 = 0 AND C % 5 = 0;
SELECT COUNT(*) FROM Data WHERE C > 90;
SELECT COUNT(*) FROM Data WHERE B < 25 OR C > 75;
SELECT COUNT(*) FROM Data WHERE A > 50 AND A < 60;
SELECT COUNT(*) FROM Data WHERE A > 55 AND A < 65 AND B > 25 AND B < 35;
SELECT COUNT(*) FROM Data WHERE A > 60 AND A < 70 AND B > 85 AND B < 90 AND C > 15 AND C < 25;

SELECT COUNT(*) FROM Data WHERE ID BETWEEN 10 AND 50;
SELECT COUNT(*) FROM Data WHERE ID % 100 = 0;
SELECT COUNT(*) FROM Data WHERE ID > 2500 AND ID < 2600;
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 1 AND 1000;
SELECT COUNT(*) FROM Data WHERE ID % 2 = 0;
SELECT COUNT(*) FROM Data WHERE ID < 500 OR ID > 4500;
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 300 AND 600;
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 100 AND 200;
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 2150 AND 2250;
SELECT COUNT(*) FROM Data WHERE ID BETWEEN 4200 AND 4230;

```