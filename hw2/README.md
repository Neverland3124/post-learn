# CSCD43 Homework 2

## Student Information
- Student 1: Zhitao Xu, Student numbe: 1006668697
- Student 2: Lianting Wang, Student numbe: 1007452374

## What works in the assignment
- Gererally everything works in the assignment:
    - We firstly implement the bloom filter structure and implement the hash functions
    - Then we use static bloomfilter size (which we could set the bloomfilter manually) and a list of hash function to compare and plot the diagram
    - After that we generate data and collect them to plot the diagram. 
    - We analyze the diagram and change the bloomfilter to be dynamic to match the expectation of rows

## What doesn't work in the assignment
- nothing 

## Preparation we done
- We prepared the sql structure and some sql workload statements
```sql
-- Structure
CREATE TABLE R (ID INTEGER PRIMARY KEY, A INTEGER, B INTEGER, C INTEGER);
CREATE TABLE S (ID INTEGER PRIMARY KEY, A INTEGER, B INTEGER, C INTEGER);

-- Workload statements
-- TODO: update
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 5000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 7000 AND S.ID > 1000;
SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 9000 AND S.ID > 1000;
```

# Result of the Assignment 
- Code of the BloomFilter
    - nodeHash.c, nodeHash.h, nodeHashjoin.c, execnodes.h
    - we didn't change plannodes.h and nodeHashjoin.h
- SQL Statements
    - workload.sql
- This README.md
- report.pdf