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
- TODO: which use what?

## postgres in backend mode
- 
```shell
cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test

```

## LRU result:
- scanqueries d1
```shell
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
LOG:  database system was shut down at 2024-01-26 17:24:30 EST
LOG:  checkpoint record is at 0/BE3A38
LOG:  redo record is at 0/BE3A38; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 828; next OID: 27152
LOG:  database system is ready

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2949"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.033335 elapsed 0.003051 user 0.000626 system sec
	!	[0.004849 user 0.002424 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/78 [0/504] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	31/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:        146 read,          0 written, buffer hit rate = 38.14%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1446"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001515 elapsed 0.001430 user 0.000085 system sec
	!	[0.006298 user 0.002519 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/3 [0/508] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         38 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "4910"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002091 elapsed 0.002091 user 0.000000 system sec
	!	[0.008401 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/7 [0/515] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         58 read,          0 written, buffer hit rate = 34.09%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1544"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001900 elapsed 0.001899 user 0.000000 system sec
	!	[0.010317 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/515] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1281"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001859 elapsed 0.001858 user 0.000000 system sec
	!	[0.012192 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/2 [0/517] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "981"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001890 elapsed 0.001890 user 0.000000 system sec
	!	[0.014095 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/517] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1120"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001602 elapsed 0.001602 user 0.000000 system sec
	!	[0.015711 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/517] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1629"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002729 elapsed 0.002728 user 0.000000 system sec
	!	[0.018453 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/517] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1382"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002023 elapsed 0.002022 user 0.000000 system sec
	!	[0.020494 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/517] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2456"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002621 elapsed 0.002620 user 0.000000 system sec
	!	[0.023129 user 0.002524 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/517] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> LOG:  shutting down
LOG:  database system is shut down
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ 
```

- indexscanqueries d1
```shell
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
LOG:  database system was shut down at 2024-01-26 17:26:08 EST
LOG:  checkpoint record is at 0/BE3AC8
LOG:  redo record is at 0/BE3AC8; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 850; next OID: 27152
LOG:  database system is ready

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "4980"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.036056 elapsed 0.001039 user 0.002988 system sec
	!	[0.001039 user 0.006235 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/78 [0/503] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	33/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:        144 read,          0 written, buffer hit rate = 38.72%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1999"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001350 elapsed 0.001350 user 0.000000 system sec
	!	[0.002392 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/8 [0/512] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         55 read,          0 written, buffer hit rate = 35.29%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1000"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001262 elapsed 0.001262 user 0.000000 system sec
	!	[0.003670 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/512] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "192"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002162 elapsed 0.000251 user 0.000000 system sec
	!	[0.003933 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/2 [0/514] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	2/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          5 read,          0 written, buffer hit rate = 97.44%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "69"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000080 elapsed 0.000081 user 0.000000 system sec
	!	[0.004032 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/2 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          0 read,          0 written, buffer hit rate = 100.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "3400"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001248 elapsed 0.001249 user 0.000000 system sec
	!	[0.005297 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         34 read,          0 written, buffer hit rate = 99.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "3899"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001645 elapsed 0.001644 user 0.000000 system sec
	!	[0.006960 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         44 read,          0 written, buffer hit rate = 98.88%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2299"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000946 elapsed 0.000945 user 0.000000 system sec
	!	[0.007927 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         28 read,          0 written, buffer hit rate = 98.79%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "99"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000104 elapsed 0.000104 user 0.000000 system sec
	!	[0.008049 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          4 read,          0 written, buffer hit rate = 96.08%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "332"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000185 elapsed 0.000186 user 0.000000 system sec
	!	[0.008252 user 0.006257 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          5 read,          0 written, buffer hit rate = 98.51%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> LOG:  shutting down
LOG:  database system is shut down
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ 
```


## MRU result:
- scanqueries d1
```shell
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
LOG:  database system was shut down at 2024-01-26 17:36:57 EST
LOG:  checkpoint record is at 0/BE3C30
LOG:  redo record is at 0/BE3C30; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 895; next OID: 27152
LOG:  database system is ready

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2949"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.035888 elapsed 0.003578 user 0.000000 system sec
	!	[0.003578 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/53 [0/476] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	31/1 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:        210 read,          0 written, buffer hit rate = 11.02%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1446"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001187 elapsed 0.001187 user 0.000000 system sec
	!	[0.004793 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/3 [0/480] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         38 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "4910"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001656 elapsed 0.001656 user 0.000000 system sec
	!	[0.006463 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/7 [0/487] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         74 read,          0 written, buffer hit rate = 15.91%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1544"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001904 elapsed 0.001903 user 0.000000 system sec
	!	[0.008381 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/0 [0/487] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1281"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001960 elapsed 0.001960 user 0.000000 system sec
	!	[0.010354 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/2 [0/489] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "981"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002596 elapsed 0.002595 user 0.000000 system sec
	!	[0.012973 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/0 [0/489] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1120"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002559 elapsed 0.002558 user 0.000000 system sec
	!	[0.015563 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/0 [0/489] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1629"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.003352 elapsed 0.003350 user 0.000000 system sec
	!	[0.018945 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/0 [0/489] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1382"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002996 elapsed 0.002994 user 0.000000 system sec
	!	[0.021978 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/0 [0/489] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2456"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.003087 elapsed 0.003087 user 0.000000 system sec
	!	[0.025101 user 0.002601 sys total]
	!	0/0 [8/24] filesystem blocks in/out
	!	0/0 [0/489] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/4] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> LOG:  shutting down
LOG:  database system is shut down
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ 

```

- indexscanqueries d1
```shell
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
LOG:  database system was shut down at 2024-01-26 17:34:53 EST
LOG:  checkpoint record is at 0/BE3BE8
LOG:  redo record is at 0/BE3BE8; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 884; next OID: 27152
LOG:  database system is ready

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "4980"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.048376 elapsed 0.002899 user 0.001605 system sec
	!	[0.004254 user 0.005672 sys total]
	!	1200/0 [7056/24] filesystem blocks in/out
	!	15/50 [44/451] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	44/0 [125/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:        208 read,          0 written, buffer hit rate = 11.49%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1999"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001534 elapsed 0.001097 user 0.000437 system sec
	!	[0.005388 user 0.006158 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/8 [44/460] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [125/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         70 read,          0 written, buffer hit rate = 17.65%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1000"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001332 elapsed 0.001332 user 0.000000 system sec
	!	[0.006729 user 0.006168 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/0 [44/460] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [125/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "192"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001980 elapsed 0.000207 user 0.000015 system sec
	!	[0.006956 user 0.006183 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/2 [44/462] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	2/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          5 read,          0 written, buffer hit rate = 97.44%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "69"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000086 elapsed 0.000045 user 0.000040 system sec
	!	[0.007011 user 0.006232 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/2 [44/464] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          2 read,          0 written, buffer hit rate = 97.22%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "3400"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001274 elapsed 0.001055 user 0.000219 system sec
	!	[0.008076 user 0.006460 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/0 [44/464] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         37 read,          0 written, buffer hit rate = 98.92%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "3899"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001440 elapsed 0.001440 user 0.000000 system sec
	!	[0.009524 user 0.006467 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/0 [44/464] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         44 read,          0 written, buffer hit rate = 98.88%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2299"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000894 elapsed 0.000894 user 0.000000 system sec
	!	[0.010432 user 0.006467 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/0 [44/464] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         28 read,          0 written, buffer hit rate = 98.79%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "99"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000099 elapsed 0.000084 user 0.000015 system sec
	!	[0.010534 user 0.006482 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/0 [44/464] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          4 read,          0 written, buffer hit rate = 96.08%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "332"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000161 elapsed 0.000100 user 0.000062 system sec
	!	[0.010645 user 0.006551 sys total]
	!	0/0 [7056/24] filesystem blocks in/out
	!	0/0 [44/464] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [127/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          7 read,          0 written, buffer hit rate = 97.92%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> LOG:  shutting down
LOG:  database system is shut down
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
	- change the algo of chose the oldest to chose the eariest
- lfu
	- least frequently used buffer
	- [1, 2, 3, 4]
	- want 5 in, take the one used least out
	- will need a counter on the time of used