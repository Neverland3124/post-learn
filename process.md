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
- output scanqueries d1
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
- output scanqueries d5
```shell
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 5 -s test
DEBUG:  found "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres" using argv[0]
DEBUG:  invoking IpcMemoryCreate(size=2899968)
LOG:  database system was shut down at 2024-01-26 17:24:34 EST
LOG:  checkpoint record is at 0/BE3A80
LOG:  redo record is at 0/BE3A80; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 839; next OID: 27152
LOG:  database system is ready
DEBUG:  InitPostgres

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A < 60;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 60 0 0 0 0 0 0 0 ]})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 60 0 0 0 0 0 0 0 ]})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 23.34 :total_cost 23.34 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 22.50 :plan_rows 334 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 60 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2949"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.033253 elapsed 0.003788 user 0.000000 system sec
	!	[0.003788 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/82 [0/508] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	31/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:        146 read,          0 written, buffer hit rate = 38.14%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE B < 30;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 23.34 :total_cost 23.34 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 22.50 :plan_rows 334 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1446"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001644 elapsed 0.001644 user 0.000000 system sec
	!	[0.005453 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/1 [0/509] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         38 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE C > 2;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false
	:args ({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true
	:constisnull false :constvalue 4 [ 2 0 0 0 0 0 0 0 ]})}} :rowMarks ()
	:targetList ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <>
	:havingQual <> :distinctClause <> :sortClause <> :limitOffset <> :limitCount
	<> :setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false
	:args ({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true
	:constisnull false :constvalue 4 [ 2 0 0 0 0 0 0 0 ]})}} :rowMarks ()
	:targetList ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <>
	:havingQual <> :distinctClause <> :sortClause <> :limitOffset <> :limitCount
	<> :setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 23.34 :total_cost 23.34 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 22.50 :plan_rows 334 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 2 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "4910"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001966 elapsed 0.001966 user 0.000000 system sec
	!	[0.007434 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/7 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         58 read,          0 written, buffer hit rate = 34.09%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 2 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 40 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 2 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 40 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 25.28 :total_cost 25.28 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 25.00 :plan_rows 112 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 20 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 40 0 0 0 0 0 0
	0 ]})}) :lefttree <> :righttree <> :initPlan <> :extParam () :allParam ()
	:nParamExec 0 :scanrelid 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1544"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002082 elapsed 0.002082 user 0.000000 system sec
	!	[0.009530 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/8 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A > 35 AND B > 60;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 2 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 35 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 60 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 2 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 35 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 60 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 25.28 :total_cost 25.28 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 25.00 :plan_rows 112 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 35 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 60 0 0 0 0 0 0
	0 ]})}) :lefttree <> :righttree <> :initPlan <> :extParam () :allParam ()
	:nParamExec 0 :scanrelid 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1281"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002009 elapsed 0.002009 user 0.000000 system sec
	!	[0.011551 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A > 30 AND C < 30;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 2 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 30 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 2 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 30 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 25.28 :total_cost 25.28 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 25.00 :plan_rows 112 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 4 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 30 0 0 0 0 0 0
	0 ]})}) :lefttree <> :righttree <> :initPlan <> :extParam () :allParam ()
	:nParamExec 0 :scanrelid 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "981"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001780 elapsed 0.001780 user 0.000000 system sec
	!	[0.013343 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE B > 20 AND C < 30;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 30 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 25.28 :total_cost 25.28 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 25.00 :plan_rows 112 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 3 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 3} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 20 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 4 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 30 0 0 0 0 0 0
	0 ]})}) :lefttree <> :righttree <> :initPlan <> :extParam () :allParam ()
	:nParamExec 0 :scanrelid 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1120"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001941 elapsed 0.001941 user 0.000000 system sec
	!	[0.015295 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A > 5 AND B < 70 AND C > 50;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({BOOLEXPR :boolop and :args ({OPEXPR
	:opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 5 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 70 0 0 0 0 0 0
	0 ]})})} {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 50 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({BOOLEXPR :boolop and :args ({OPEXPR
	:opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 5 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 70 0 0 0 0 0 0
	0 ]})})} {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 50 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 27.60 :total_cost 27.60 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 27.50 :plan_rows 38 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 5 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 70 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 50 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1629"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002960 elapsed 0.002960 user 0.000000 system sec
	!	[0.018266 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40 AND C > 10;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({BOOLEXPR :boolop and :args ({OPEXPR
	:opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 20 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 40 0 0 0 0 0 0
	0 ]})})} {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 10 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({BOOLEXPR :boolop and :args ({OPEXPR
	:opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 20 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 40 0 0 0 0 0 0
	0 ]})})} {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 10 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 27.60 :total_cost 27.60 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 27.50 :plan_rows 38 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 20 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 40 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 10 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1382"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002287 elapsed 0.002287 user 0.000000 system sec
	!	[0.020581 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE A < 70 AND B < 80 AND C < 90;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({BOOLEXPR :boolop and :args ({OPEXPR
	:opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 70 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 80 0 0 0 0 0 0
	0 ]})})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 90 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({BOOLEXPR :boolop and :args ({OPEXPR
	:opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 2}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 70 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 80 0 0 0 0 0 0
	0 ]})})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 90 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 27.60 :total_cost 27.60 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 27.50 :plan_rows 38 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 2 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 2} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 70 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 80 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 4 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 4} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 90 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2456"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002427 elapsed 0.002426 user 0.000000 system sec
	!	[0.023020 user 0.003421 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/524] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  proc_exit(0)
DEBUG:  shmem_exit(0)
LOG:  shutting down
LOG:  database system is shut down
DEBUG:  exit(0)
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ 
```
- output indexscanqueries d1
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
- output indexscanqueries d5
```shell
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$ cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 5 -s test
DEBUG:  found "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres" using argv[0]
DEBUG:  invoking IpcMemoryCreate(size=2899968)
LOG:  database system was shut down at 2024-01-26 17:29:16 EST
LOG:  checkpoint record is at 0/BE3B10
LOG:  redo record is at 0/BE3B10; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 861; next OID: 27152
LOG:  database system is ready
DEBUG:  InitPostgres

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 20;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false
	:args ({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true
	:constisnull false :constvalue 4 [ 20 0 0 0 0 0 0 0 ]})}} :rowMarks ()
	:targetList ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <>
	:havingQual <> :distinctClause <> :sortClause <> :limitOffset <> :limitCount
	<> :setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false
	:args ({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true
	:constisnull false :constvalue 4 [ 20 0 0 0 0 0 0 0 ]})}} :rowMarks ()
	:targetList ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <>
	:havingQual <> :distinctClause <> :sortClause <> :limitOffset <> :limitCount
	<> :setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 23.34 :total_cost 23.34 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 22.50 :plan_rows 334 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 20 0 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "4980"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.040580 elapsed 0.002804 user 0.001193 system sec
	!	[0.002804 user 0.004206 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/86 [0/509] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	33/0 [76/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:        144 read,          0 written, buffer hit rate = 38.72%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID < 2000;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -48 7 0 0 0 0 0 0 ]})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -48 7 0 0 0 0 0 0 ]})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 23.34 :total_cost 23.34 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 22.50 :plan_rows 334 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -48 7 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1999"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001790 elapsed 0.000968 user 0.000822 system sec
	!	[0.003782 user 0.005043 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/7 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         55 read,          0 written, buffer hit rate = 35.29%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 4000;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false
	:args ({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true
	:constisnull false :constvalue 4 [ -96 15 0 0 0 0 0 0 ]})}} :rowMarks ()
	:targetList ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <>
	:havingQual <> :distinctClause <> :sortClause <> :limitOffset <> :limitCount
	<> :setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {OPEXPR :opno 521 :opfuncid 0 :opresulttype 16 :opretset false
	:args ({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true
	:constisnull false :constvalue 4 [ -96 15 0 0 0 0 0 0 ]})}} :rowMarks ()
	:targetList ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <>
	:havingQual <> :distinctClause <> :sortClause <> :limitOffset <> :limitCount
	<> :setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 23.34 :total_cost 23.34 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{SEQSCAN :startup_cost 0.00 :total_cost 22.50 :plan_rows 334 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual
	({OPEXPR :opno 521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR
	:varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1
	:varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -96 15 0 0 0 0 0 0 ]})}) :lefttree <> :righttree <>
	:initPlan <> :extParam () :allParam () :nParamExec 0 :scanrelid 1} :righttree
	<> :initPlan <> :extParam () :allParam () :nParamExec 0 :aggstrategy 0
	:numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "1000"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001446 elapsed 0.001445 user 0.000000 system sec
	!	[0.005235 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/516] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [76/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 7 AND ID < 200;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 7 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -56 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 7 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -56 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 7 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -56 0 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 7 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -56 0 0 0 0 0
	0 0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "192"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.002417 elapsed 0.000395 user 0.000000 system sec
	!	[0.005650 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/9 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	2/0 [78/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          5 read,          0 written, buffer hit rate = 97.44%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 20 AND ID < 90;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 90 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 90 0 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 20 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 90 0 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 20 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 90 0 0 0 0 0 0
	0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam () :allParam ()
	:nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "69"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000238 elapsed 0.000237 user 0.000000 system sec
	!	[0.005907 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          0 read,          0 written, buffer hit rate = 100.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 99 AND ID < 3500;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 99 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -84 13 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 99 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -84 13 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 99 0 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -84 13 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 99 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -84 13 0 0 0 0
	0 0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "3400"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001523 elapsed 0.001523 user 0.000000 system sec
	!	[0.007448 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [78/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         34 read,          0 written, buffer hit rate = 99.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 100 AND ID < 4000;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 100 0 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -96 15 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 100 0 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -96 15 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 100 0 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -96 15 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 100 0 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -96 15 0 0 0 0
	0 0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "3899"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001994 elapsed 0.001771 user 0.000000 system sec
	!	[0.009239 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	1/0 [79/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         44 read,          0 written, buffer hit rate = 98.88%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 600 AND ID < 2900;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 88 2 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 84 11 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 88 2 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 84 11 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 88 2 0 0 0 0 0
	0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 84 11 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 88 2 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 84 11 0 0 0 0
	0 0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2299"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.001050 elapsed 0.001050 user 0.000000 system sec
	!	[0.010314 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [79/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         28 read,          0 written, buffer hit rate = 98.79%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 3500 AND ID < 3600;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -84 13 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 16 14 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -84 13 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 16 14 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -84 13 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ 16 14 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ -84 13 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 16 14 0 0 0 0
	0 0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam () :allParam
	() :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "99"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000243 elapsed 0.000242 user 0.000000 system sec
	!	[0.010572 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [79/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          4 read,          0 written, buffer hit rate = 96.08%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  StartTransactionCommand
LOG:  statement: SELECT COUNT(*) FROM Data WHERE ID > 4666 AND ID < 4999;
	
DEBUG:  parse tree:
DETAIL:  {QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 58 18 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -121 19 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()}
	
DEBUG:  rewritten parse tree:
DETAIL:  ({QUERY :commandType 1 :querySource 0 :canSetTag true :utilityStmt <>
	:resultRelation 0 :into <> :hasAggs true :hasSubLinks false :rtable ({RTE
	:alias <> :eref {ALIAS :aliasname data :colnames ("id" "a" "b" "c")} :rtekind
	0 :relid 22148 :inh true :inFromCl true :checkForRead true :checkForWrite
	false :checkAsUser 0}) :jointree {FROMEXPR :fromlist ({RANGETBLREF :rtindex
	1}) :quals {BOOLEXPR :boolop and :args ({OPEXPR :opno 521 :opfuncid 0
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 58 18 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 0 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -121 19 0 0 0 0 0 0 ]})})}} :rowMarks () :targetList
	({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1 :resname
	count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false} :expr
	{AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23 :constlen 4
	:constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0 0 ]}
	:agglevelsup 0 :aggstar true :aggdistinct false}}) :groupClause <> :havingQual
	<> :distinctClause <> :sortClause <> :limitOffset <> :limitCount <>
	:setOperations <> :resultRelations ()})
	
DEBUG:  plan:
DETAIL:  {AGG :startup_cost 17.10 :total_cost 17.10 :plan_rows 1 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 20 :restypmod -1
	:resname count :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {AGGREF :aggfnoid 2147 :aggtype 20 :target {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 1 0 0 0 0 0 0
	0 ]} :agglevelsup 0 :aggstar true :aggdistinct false}}) :qual <> :lefttree
	{INDEXSCAN :startup_cost 0.00 :total_cost 17.08 :plan_rows 5 :plan_width 0
	:targetlist ({TARGETENTRY :resdom {RESDOM :resno 1 :restype 23 :restypmod -1
	:resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0 :resjunk false}
	:expr {VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0
	:varnoold 1 :varoattno 1}} {TARGETENTRY :resdom {RESDOM :resno 2 :restype 23
	:restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0 :resorigcol 0
	:resjunk false} :expr {VAR :varno 1 :varattno 2 :vartype 23 :vartypmod -1
	:varlevelsup 0 :varnoold 1 :varoattno 2}} {TARGETENTRY :resdom {RESDOM :resno
	3 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0 :resorigtbl 0
	:resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 3 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 3}} {TARGETENTRY :resdom
	{RESDOM :resno 4 :restype 23 :restypmod -1 :resname <> :ressortgroupref 0
	:resorigtbl 0 :resorigcol 0 :resjunk false} :expr {VAR :varno 1 :varattno 4
	:vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 4}}) :qual <>
	:lefttree <> :righttree <> :initPlan <> :extParam () :allParam () :nParamExec
	0 :scanrelid 1 :indxid ( 22150) :indxqual (({OPEXPR :opno 521 :opfuncid 147
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ 58 18 0 0 0 0
	0 0 ]})} {OPEXPR :opno 97 :opfuncid 66 :opresulttype 16 :opretset false :args
	({VAR :varno 1 :varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold
	1 :varoattno 1} {CONST :consttype 23 :constlen 4 :constbyval true :constisnull
	false :constvalue 4 [ -121 19 0 0 0 0 0 0 ]})})) :indxqualorig (({OPEXPR :opno
	521 :opfuncid 147 :opresulttype 16 :opretset false :args ({VAR :varno 1
	:varattno 1 :vartype 23 :vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1}
	{CONST :consttype 23 :constlen 4 :constbyval true :constisnull false
	:constvalue 4 [ 58 18 0 0 0 0 0 0 ]})} {OPEXPR :opno 97 :opfuncid 66
	:opresulttype 16 :opretset false :args ({VAR :varno 1 :varattno 1 :vartype 23
	:vartypmod -1 :varlevelsup 0 :varnoold 1 :varoattno 1} {CONST :consttype 23
	:constlen 4 :constbyval true :constisnull false :constvalue 4 [ -121 19 0 0 0
	0 0 0 ]})})) :indxorderdir 1} :righttree <> :initPlan <> :extParam ()
	:allParam () :nParamExec 0 :aggstrategy 0 :numCols 0 :numGroups 0}
	
DEBUG:  PortalRun
	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "332"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
DEBUG:  CommitTransactionCommand
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.000320 elapsed 0.000319 user 0.000000 system sec
	!	[0.010907 user 0.005053 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/525] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [79/3] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:          5 read,          0 written, buffer hit rate = 98.51%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> DEBUG:  proc_exit(0)
DEBUG:  shmem_exit(0)
LOG:  shutting down
LOG:  database system is shut down
DEBUG:  exit(0)
xuzhitao@iits-i406-42:~/cscd43/hw1_github_repo$
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