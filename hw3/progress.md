# hw3

## Commands
```shell


./bin/postmaster -p 14324 -D ./data >logfile 2>&1 &
./bin/createdb hw -p 14324
./bin/psql hw -p 14324
./bin/pg_ctl stop -D ./data -m fast;

```
```sql
CREATE TABLE One(
id integer,
b integer,
c integer,
d integer);
CREATE TABLE Two(
id integer,
a integer);

----------------------------Useful------------------------------


-- setup zhitao
CREATE TABLE One(id integer, b integer, c integer, d integer);
CREATE TABLE Two(id integer, a integer);
copy One(id, b, c, d) from '/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw3/shell/one.csv' delimiter ',';
copy Two(id, a) from '/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw3/shell/two.csv' delimiter ',';
select count(*) from One;
select count(*) from Two;

CREATE INDEX one_id_idx ON One (id); CREATE INDEX one_b_idx ON One (b); CREATE INDEX one_c_idx ON One (c); CREATE INDEX one_d_idx ON One (d); CREATE INDEX two_id_idx ON Two (id); CREATE INDEX two_a_idx ON Two (a);

-- 
vacuum analyze;

-- temp set default_statistics_target 0 - 1000, default 10
SET default_statistics_target = 100;
-- perm set
ALTER SYSTEM SET default_statistics_target = 200;
SELECT pg_reload_conf();
-- show
SHOW default_statistics_target;



-- sql statements

SELECT count(*) FROM One WHERE b > 500;

SELECT count(*) FROM One WHERE c < 80;

SELECT count(*) FROM One WHERE d BETWEEN 100 AND 200;

SELECT count(*) FROM One WHERE b > 300 AND c < 600;

SELECT count(*) FROM One WHERE d < 50 OR d > 950;

SELECT count(*) FROM Two WHERE a > 200;

SELECT count(*) FROM Two WHERE a < 100;

SELECT count(*) FROM One WHERE b > 250 ORDER BY c DESC;

SELECT count(*) FROM Two WHERE a NOT BETWEEN 300 AND 700;

SELECT count(*) FROM One WHERE id > 5000 LIMIT 10;



```

## Setup
- Some sample queries to understand the data
```sql
```

## 3
### 3.1
- System Catalogs
- Question 1: Use the PostgreSQL catalog to find the number of distinct values of each of the attributes in Table One. Write the SQL query you used to find out this information.
SQL query:
```sql
SELECT attname AS column_name, n_distinct
FROM pg_stats
WHERE tablename = 'one' AND schemaname = 'public'; 
-- attname refers to the "attribute name" of a column within a table
-- n_distinct is a statistic stored in the pg_stats system view that represents the number of distinct values for a table column. 
-- public is the default schema to store common objectes, without is the same

-- Result
column_name | n_distinct 
-------------+------------
 id          |         -1
 b           |  -0.416401
 c           |        453
 d           |        100
(4 rows)
```
The number of distinct values: in result
Analyze: 
- id: n_distinct = -1: This indicates that the id column is estimated to have a unique value for every row in the table
- b: n_distinct = -0.416401: Negative values (other than -1) represent the ratio of distinct values to the total number of rows, expressed as a negative fraction. In this case, the b column is estimated to have distinct values in approximately 41.64% of the rows. This means if you have 100 rows, about 42 of them (rounding the percentage) are expected to have unique values in column b.
- c: n_distinct = 453: Positive values indicate the actual estimated number of distinct values within the column across the entire table. Here, the c column is estimated to have 453 distinct values. This is an absolute number, not a ratio or percentage.
- d: n_distinct = 100: Similarly, this indicates that column d is estimated to have 100 distinct values throughout the table.

- Question 2: Use the catalog to find out the space used by the relation Two on the disk, in number of bytes. Write down the SQL query used to find this information.
SQL query:
```sql
SELECT 
    relname AS "Table", 
    relpages * 8192 AS "Estimated Size (bytes)" 
FROM 
    pg_class 
WHERE 
    relname = 'two';
-- relname: This column in pg_class represents the name of the relation.
--  filter it to table two in the query
-- relpages: This column contains the number of disk pages that the relation occupies. PostgreSQL typically uses a page size of 8 KB (or 8192 bytes)
-- pg_class is a system catalog in PostgreSQL that contains information about database tables and other relation types

-- Result
hw-#  Table | Estimated Size (bytes) 
-------+------------------------
 two   |                 450560
(1 row)

```
The space used by Two in disk: 450560: The estimated size of the table on disk, in bytes. Based on your query, the two table is estimated to use 450,560 bytes (or about 440 KB) of disk space.
Analyze:


### 3.2
- Equality Queries
- Question 1: Use the PostgreSQL catalog to find the number of distinct values of each of the attributes in Table One. Write the SQL query you used to find out this information.
SQL query:
```sql
SELECT * FROM One WHERE d = 10;
SELECT * FROM One WHERE d = 37;
SELECT * FROM One WHERE d = 50;

SELECT * FROM One WHERE d = 67;
SELECT count(*) FROM One WHERE d = 67;
EXPLAIN SELECT * FROM One WHERE d = 67;
EXPLAIN SELECT count(*) FROM One WHERE d = 67;

hw=# EXPLAIN SELECT * FROM One WHERE d = 67;
                       QUERY PLAN                       
--------------------------------------------------------
 Seq Scan on one  (cost=0.00..189.00 rows=584 width=16)
   Filter: (d = 67)
(2 rows)

SELECT * FROM One WHERE d = 91;
SELECT count(*) FROM One WHERE d = 91;
EXPLAIN SELECT * FROM One WHERE d = 91;
EXPLAIN SELECT count(*) FROM One WHERE d = 91;

hw=# EXPLAIN SELECT * FROM One WHERE d = 91;
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Index Scan using one_d_idx on one  (cost=0.00..130.67 rows=44 width=16)
   Index Cond: (d = 91)
(2 rows)

SELECT * FROM One WHERE d = 70;
SELECT * FROM One WHERE d = 92;

hw=# SELECT d, COUNT(d) AS frequency
FROM One
GROUP BY hw-# hw-# d
ORDER BY frequency DESC;hw-# 
  d  | frequency 
-----+-----------
  69 |      2778
  68 |       938
  67 |       533
  66 |       399
  65 |       323
  64 |       254
  63 |       241
  62 |       194
  61 |       190
  60 |       151
  58 |       144
  59 |       134
  57 |       134
  56 |       131
  55 |       105
  52 |       102
  54 |       100
  53 |        88
  47 |        85
  51 |        83
  50 |        82
  48 |        78
  46 |        76
  49 |        74
  45 |        68
  41 |        65
  44 |        64
  39 |        61
  38 |        60
  42 |        57
  43 |        56
  40 |        56
  37 |        56
  31 |        53
  35 |        49
  26 |        49
  34 |        48
  29 |        48
  32 |        46
  36 |        45
  30 |        45
  25 |        45
  24 |        45
  21 |        45
  75 |        43
  28 |        42
  27 |        40
  88 |        39
  94 |        38
  33 |        37
  23 |        36
  72 |        35
  84 |        34
  70 |        34
  78 |        33
  77 |        33
  82 |        32
  81 |        32
  71 |        32
 116 |        31
  86 |        31
  76 |        31
  74 |        31
  92 |        30
  22 |        30
  73 |        29
 115 |        28
 114 |        28
 104 |        27
  97 |        27
 106 |        26
  90 |        26
  85 |        26
  80 |        26
  79 |        26
 119 |        25
  83 |        25
  20 |        25
 105 |        24
  95 |        24
  87 |        24
  93 |        23
  91 |        23
  99 |        22
  96 |        22
 117 |        21
 111 |        21
 110 |        21
 108 |        21
 102 |        21
  89 |        21
 112 |        20
 109 |        20
 103 |        20
 100 |        20
 101 |        19
  98 |        19
 107 |        17
 113 |        16
 118 |        14
 120 |         1
(101 rows)

hw=# EXPLAIN SELECT * FROM One WHERE d = 61;
                       QUERY PLAN                       
--------------------------------------------------------
 Seq Scan on one  (cost=0.00..189.00 rows=187 width=16)
   Filter: (d = 61)
(2 rows)

--   61 |       190
--   60 |       151

hw=# EXPLAIN SELECT * FROM One WHERE d = 60;
                               QUERY PLAN                                
-------------------------------------------------------------------------
 Index Scan using one_d_idx on one  (cost=0.00..130.64 rows=44 width=16)
   Index Cond: (d = 60)
(2 rows)
```
- Explain:

### 3.3
- Single Column Range Queries
```sql
SELECT COUNT(*) FROM One WHERE c > value1 AND c < value2;

SELECT COUNT(*) FROM One WHERE c > 50 AND c < 250;


SELECT c, COUNT(c) AS frequency
FROM One
GROUP BY  c
ORDER BY frequency DESC;



  c  | frequency 
-----+-----------
 249 |      1103
 248 |       638
 247 |       446
 246 |       314
 245 |       277
 244 |       248
 243 |       204
 242 |       177
 241 |       174
 240 |       135
 238 |       124
 237 |       109
 236 |       104
 239 |       102
 235 |        94
 234 |        88
 ...
 273 |         3
 266 |         3
  67 |         3
  53 |         3
 469 |         2
 458 |         2
 439 |         2
 410 |         2
 404 |         2
 400 |         2
 377 |         2
 375 |         2
 368 |         2
 359 |         2
 344 |         2
 334 |         2
 316 |         2
  79 |         2
   1 |         2
 500 |         1
 493 |         1
 491 |         1
 490 |         1
 467 |         1
 449 |         1
 443 |         1
 437 |         1
 390 |         1
 336 |         1
(496 rows)

SET default_statistics_target = 200;
vacuum analyze;
SHOW default_statistics_target;

SELECT COUNT(*) FROM One WHERE c > 50 AND c < 250;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 50 AND c < 250;



-- Very broad range covering a large portion of the spectrum
SELECT COUNT(*) FROM One WHERE c > 50 AND c < 450;

-- on way
SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60;
SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320;
SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250;
SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460;
SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350;
SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400;
SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490;
SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500;
SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100;
SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455;

EXPLAIN SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455;

-- another way
SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60;
SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320;
SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250;
SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460;
SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350;
SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400;
SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490;
SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500;
SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100;
SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455;

```

## 3.4
- MultiColumn Range Queries
```sql
SET default_statistics_target = 10;
vacuum analyze;
SHOW default_statistics_target;


-- sample
SELECT COUNT(*) FROM One
WHERE c > value1 AND c < value2 AND
d > value3 AND d < value4;

-- init sql
-- for queries that return very few or no values
SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400 AND d > 5 AND d < 45;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400 AND d > 5 AND d < 45;

-- for queries that return many values
SELECT COUNT(*) FROM One WHERE c > 125 AND c < 400 AND d > 25 AND d < 80;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 125 AND c < 400 AND d > 25 AND d < 80;


-- set of sql queries
SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60 AND d > 25 AND d < 80;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60 AND d > 25 AND d < 80;
SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320 AND d > 45 AND d < 120;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320 AND d > 45 AND d < 120;
SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250 AND d > 55 AND d < 70;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250 AND d > 55 AND d < 70;
SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460 AND d > 30 AND d < 90;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460 AND d > 30 AND d < 90;
SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350 AND d > 100 AND d < 110;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350 AND d > 100 AND d < 110;
SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400 AND d > 20 AND d < 120;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400 AND d > 20 AND d < 120;
SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490 d > 32 AND d < 99;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490 AND d > 32 AND d < 99;
SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500 AND d > 57 AND d < 65;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500 AND d > 57 AND d < 65;
SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100 AND d > 85 AND d < 110;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100 AND d > 85 AND d < 110;
SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455 AND d > 25 AND d < 80;
EXPLAIN SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455 AND d > 25 AND d < 80;
```
