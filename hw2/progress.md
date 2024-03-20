# hw2

## TODO
- hash functions
- read source code locate where to add bitmap
- add it
- apply hash function
- test
- report and graph

ideas:
- Add BloomFilter struct definition
- Add BloomFilter in HashState struct
- Initialize it
- Use it when we do ExecHashTableInsert




- ExecHash is where we build hash table for inner relation (build tuple), we need to apply the bloom filter on it so that we could have a result bloom filter
- Then when we go through outer hash table (probe tuple), we could then verify each record with such bloom filter.

- find where add the inner hash table
- find where add the outer hash table
    - step 3 in the handout
    - understand why
- add the filter there
    - design the hash functions
    - add the bit array for bf
    - use the bf to filter out result
- original performance
- new performance
- sql statement
- data
- report

## Important functions / structure
- nodeHash.c
    - ExecHash: constructs an in-memory hash table from the tuples of the inner relation
- nodeHashjoin.c
    - ExecHashJoin: fetching tuples from the outer relation, probing the hash table built on the inner relation for matches, and applying join conditions to produce the result set
    - ExecHashJoinOuterGetTuple: retrieves the next tuple from the outer relation 
- execnode.h
    - HashJoinState: The HashJoinState structure represents the state of execution of a hash join operation.

## Commands
```shell
# Zhitao Part
# sql
SET enable_nestloop TO off;
SET enable_mergejoin TO off;

CREATE TABLE R (ID INTEGER PRIMARY KEY, A INTEGER, B INTEGER, C INTEGER);
CREATE TABLE S (ID INTEGER PRIMARY KEY, A INTEGER, B INTEGER, C INTEGER);

copy R(ID, A, B, C) from '/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/shell/data1.csv' delimiter ',';
copy S(ID, A, B, C) from '/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/shell/data2.csv' delimiter ',';

select count(*) from R;
select count(*) from S;

SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3 AND S.ID > 1;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 4000 AND S.ID > 2000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 4000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 7000 AND S.ID > 3000;
EXPLAIN SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000;
vacuum analyze;


SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 5000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 7000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 9000 AND S.ID > 1000;

SET enable_nestloop TO off; SET enable_mergejoin TO off; VACUUM ANALYZE;SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000; SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 5000 AND S.ID > 1000; SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 7000 AND S.ID > 1000; SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 9000 AND S.ID > 1000;

./bin/postmaster -p 14324 -D ./data >logfile 2>&1 &
./bin/createdb hw -p 14324
./bin/psql hw -p 14324



# Lianting Part

```

## Code
```c

	/* BEGIN NEWCODE */
	
	/* END NEWCODE */
```
