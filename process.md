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
SELECT COUNT(*) FROM Data WHERE B < 30;
SELECT COUNT(*) FROM Data WHERE C > 2;
SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40;
SELECT COUNT(*) FROM Data WHERE A > 35 AND B > 60;
SELECT COUNT(*) FROM Data WHERE A > 30 AND C < 30;
SELECT COUNT(*) FROM Data WHERE B > 20 AND C < 30;
SELECT COUNT(*) FROM Data WHERE A > 5 AND B < 70 AND C > 50;
SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40 AND C > 10;
SELECT COUNT(*) FROM Data WHERE A < 70 AND B < 80 AND C < 90;

-- Explain
EXPLAIN SELECT COUNT(*) FROM Data WHERE A < 60;
EXPLAIN SELECT COUNT(*) FROM Data WHERE B < 30;
EXPLAIN SELECT COUNT(*) FROM Data WHERE C > 2;
EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40;
EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 35 AND B > 60;
EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 30 AND C < 30;
EXPLAIN SELECT COUNT(*) FROM Data WHERE B > 20 AND C < 30;
EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 5 AND B < 70 AND C > 50;
EXPLAIN SELECT COUNT(*) FROM Data WHERE A > 20 AND B < 40 AND C > 10;
EXPLAIN SELECT COUNT(*) FROM Data WHERE A < 70 AND B < 80 AND C < 90;
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
Explain SELECT COUNT(*) FROM Data WHERE ID < 2000;
Explain SELECT COUNT(*) FROM Data WHERE ID > 4000;
Explain SELECT COUNT(*) FROM Data WHERE ID > 7 AND ID < 200;
Explain SELECT COUNT(*) FROM Data WHERE ID > 20 AND ID < 90;
Explain SELECT COUNT(*) FROM Data WHERE ID > 99 AND ID < 3500;
Explain SELECT COUNT(*) FROM Data WHERE ID > 100 AND ID < 4000;
Explain SELECT COUNT(*) FROM Data WHERE ID > 600 AND ID < 2900;
Explain SELECT COUNT(*) FROM Data WHERE ID > 3500 AND ID < 3600;
Explain SELECT COUNT(*) FROM Data WHERE ID > 4666 AND ID < 4999;
```

### try the queries
- try executing these queries in PostgreSQL , and
- check, using the EXPLAIN command in psql, that they are indeed executed using Sequential Scans or Index Scans, as specified
- Some use index scans, some use sequential scans
- TODO: which use what?

## postgres in backend mode
- 
```shell
cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s data
```
- output
```shell
xuzhitao@iits-i406-03:~/cscd43/hw1_github_repo$ cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test
LOG:  database system was shut down at 2024-01-25 14:50:35 EST
LOG:  checkpoint record is at 0/BE3720
LOG:  redo record is at 0/BE3720; undo record is at 0/0; shutdown TRUE
LOG:  next transaction ID: 626; next OID: 27152
LOG:  database system is ready

POSTGRES backend interactive interface 
$Revision: 1.375.2.5 $ $Date: 2005/12/14 17:07:00 $

backend> 	 1: count	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
	 1: count = "2949"	(typeid = 20, len = 8, typmod = -1, byval = f)
	----
LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
	!	0.033431 elapsed 0.001859 user 0.001345 system sec
	!	[0.004155 user 0.002493 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/80 [0/508] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	31/0 [80/2] voluntary/involuntary context switches
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
	!	0.001399 elapsed 0.001212 user 0.000189 system sec
	!	[0.005384 user 0.002692 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/3 [0/512] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.001683 elapsed 0.001683 user 0.000000 system sec
	!	[0.007078 user 0.002697 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/7 [0/519] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.001626 elapsed 0.001626 user 0.000000 system sec
	!	[0.008718 user 0.002697 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/519] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.001895 elapsed 0.001039 user 0.000856 system sec
	!	[0.009771 user 0.003553 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/2 [0/521] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.001835 elapsed 0.001598 user 0.000237 system sec
	!	[0.011379 user 0.003793 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/521] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.002057 elapsed 0.002057 user 0.000000 system sec
	!	[0.013446 user 0.003796 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/521] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.002100 elapsed 0.002100 user 0.000000 system sec
	!	[0.015561 user 0.003796 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/521] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.001776 elapsed 0.001727 user 0.000048 system sec
	!	[0.017300 user 0.003844 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/521] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
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
	!	0.002709 elapsed 0.002708 user 0.000000 system sec
	!	[0.020021 user 0.003847 sys total]
	!	0/0 [0/24] filesystem blocks in/out
	!	0/0 [0/521] page faults/reclaims, 0 [0] swaps
	!	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
	!	0/0 [80/2] voluntary/involuntary context switches
	! buffer usage stats:
	!	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00%
	!	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
	!	Direct blocks:          0 read,          0 written
backend> LOG:  shutting down
LOG:  database system is shut down
xuzhitao@iits-i406-03:~/cscd43/hw1_github_repo$ 

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