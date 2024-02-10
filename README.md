# CSCD43 Homework 1

## Student Information
- Student 1: Zhitao Xu, Student numbe: 1006668697
- Student 2: Lianting Wang, Student numbe: 1007452374

## What works in the assignment
- The main part of this project is divided to three part:
    - Set up and SQL statement preparation
    - MRU Algorithm implement
    - LFU Algorithm implement

### Preparation
- For set up and SQL statement, we start with doing the setup and come up with 20 normal SQL statements, 10 for ScanQueries, 10 for IndexScanQueries. 
```sql
-- Scan Queries
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
-- IndexScanQueries
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
- In the later implementations, we did change the sql statements later to try generate more representitive data. 
```sql
-- Updated Scan Queries
SELECT COUNT(*) FROM Data WHERE A < 45;
SELECT COUNT(*) FROM Data WHERE B % 5 = 0;
SELECT COUNT(*) FROM Data WHERE C BETWEEN 15 AND 25;
SELECT COUNT(*) FROM Data WHERE A > 30 AND B > 45 AND C < 70;
SELECT COUNT(*) FROM Data WHERE A % 4 = 0 AND C % 4 = 0;
SELECT COUNT(*) FROM Data WHERE A < 25 OR B > 85;
SELECT COUNT(*) FROM Data WHERE C > 85;
SELECT COUNT(*) FROM Data WHERE A BETWEEN 45 AND 55;
SELECT COUNT(*) FROM Data WHERE B < 30 OR C > 70;
SELECT COUNT(*) FROM Data WHERE A < 15 OR A > 85;

-- Updated IndexScanQueries
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

### MRU Implementation
- For MRU, initially we checked over that four files and though we might not need to change to much to make the code work. The original algorithm is LRU which Postgres put the new buffer in to the end of the SharedFreeList. We changed that part to put the buffer to the next (top) of the SharedFreeList.
- However, this piece of code is not working as we check the buffer hit rate across different buffer hit rate. We examine the reason and dig in to it found:
    - When the buffer pool initialized, all buffer will be sent to the free list and directly apply MRU will cause all rest buffers in free list not affected and buffer hit rate remains really low when buffer size increase.
    - So we apply the original LRU Algorithm for number of buffers step to clear out all unused buffer, and then start to apply MRU algorithm to replace the buffer page.
    - Also, since read a buffer is also consider access the buffer, we implement a function to update the buffer to the first of the free list when we read the butter.

### LFU Implementation
- For LFU, we add a counter buf_use_cnt int the struct of Buffer Descripter in buf_internals.h, init the counter in the buf_init.c, add increment on the counter when read / write / pin the buffer, add reset when we decide to choose it as new buffer to evict in Buffer Alloc function and select the buffer with lowest counter in GetFreeBuffer function in freelist.c.

## Conclusion
- So the set up part and run through all sql statement is quiet fluent and successful.

## What does not work in the assignment (the challendge we meet)
- What does not work in the assignment is mostly happens in the implementation details as what we expected is not what we have.

### First type of diagram
- For the report of this assignment, we tried to generate two type of diagrams, the first type diagram with x-axis as 10 different queries to cross compare lru, mru, lfu algo by run them sequentially as handout's command.
```shell
cat <queryfile.sql> | postgres -B <numbuffers> -D <datadir> -d <debug-level> -s <databasename>
```
- For LRU and LFU algorithm, when we have a low number of buffers (lower than 32), we will have the query start from fifth query have buffer hit rate of 0% or extremely low. When the number of buffers is bigger than 32, we can have an expected buffer hit rate of around 100%. We analyze the root cause and think there might be a sequential flood on it. 
- For MRU, the threthold come to the number of buffers as 221. When the number of buffers is below 220, the buffer hit rate is abnormal with very low hit rate. After number of buffers 221, the buffer hit rate start to go up and when number of buffers is around 250, the buffer hit rate will increase to around 100%.
- We strugle on to make MRU working as expectation and spend a lot of time to generate data nd diagram on it.

### Second type of diagram
- Consider the previous diagram doesn't show the how one SQL statement change across the buffer size, we generate a second type of diagram to compare a SQL Query's buffer hit rate on different number of buffers (i.e.: x-axis is number of buffers). To make the number meaningful, we also run all queries seperately (individually) to compare this because if run the queries sequentially we will be comparing a list of 100% for later queries.
- After our change to MRU algo implementation, the diagram follows our expectation which the buffer hit rate of LRU and LFU is quite close which increase hugely at first and approach to a limit and MRU is increasing more stably to that limit as well.

## Conclusion
- The main difficulty of our working on the assignment is about MRU algorithm. We didn't get the trick of MRU algorithm at first and lead to wrong implemntation and useless data collection. Overally we get a quite deep understand of how the buffer replacement algorithm works in Postgres.

# Output Diagram
- In folder /Diagram
    - First type of diagram (sequential) will be start with Sequential
    - Second type of diagram (individual) will be start with individual