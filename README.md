# CSCD43 Homework 1

## Student Information
- Student 1: Zhitao Xu, Student numbe: 1006668697
- Student 2: TODO:

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

### MRU Implementation
- For MRU, we checked over that four files and found we might not need to change to much to make the code work. The original algorithm is LRU which Postgres put the new buffer in to the end of the SharedFreeList. We changed that part to put the buffer to the next (top) of the SharedFreeList.
- Later then we realize that read or write to the buffer is also consider access to the buffer so we take a look at that part of the code. We add a function UpdateFreeList in read buffer to allow move the buffer to the first of the free list. For writing, we examine the code and found it will unpin the page and re-shift the buffer to the first one as well so we didn't change it.

### LRU Implementation
- For LRU, we add a counter buf_use_cnt int the struct of Buffer Descripter in buf_internals.h, init the counter in the buf_init.c, add increment on the counter when read / write / pin the buffer, add reset when we decide to choose it as new buffer to evict in Buffer Alloc function and select the buffer with lowest counter in GetFreeBuffer function in freelist.c.

## Conclusion
- So the set up part and implement part is quiet fluent and successful, what does not work in the assignment is mostly happens in the report and data part.

## What does not work in the assignment
### First type of diagram
- For the report of this assignment, we tried to generate two type of diagrams, the first type diagram with x-axis as 10 different queries to cross compare lru, mru, lfu algo by run them sequentially as handout's command.
```shell
cat <queryfile.sql> | postgres -B <numbuffers> -D <datadir> -d <debug-level> -s <databasename>
```
- For LRU and LFU algo, when we have a low number of buffers (lower than 32), we will have the last 6 query have buffer hit rate of 0%. When the number of buffers is bigger than 32, we can have an expected buffer hit rate of 100%. We analyze the root cause and think there might be a sequential flood on it. 
- For MRU, the case of buffer hit rate remain at 0% is not fixed as buffer size increase. We check the source code and add some analyze debug statements, and found the buffer hit rate becomes abnormal after four normal output. (We found the counter variable BufferHitCount in the source code correctly updated but the buffer hit rate output remains 0)
- We are not able to solve this issue and think it's might be a postgres issue in the early version
```shell
# some output snippet
Debug BufferHitCount: 32 # this correctly show that the buffer hit is more than 0
backend> LOG:  QUERY STATISTICS
DETAIL:  ! system usage stats:
    !	0.004787 elapsed 0.004111 user 0.000000 system sec
    !	[0.018879 user 0.007593 sys total]
    !	0/0 [0/208] filesystem blocks in/out
    !	0/2 [45/496] page faults/reclaims, 0 [0] swaps
    !	0 [0] signals rcvd, 0/0 [0/0] messages rcvd/sent
    !	0/8 [80/24] voluntary/involuntary context switches
    ! buffer usage stats:
    !	Shared blocks:         32 read,          0 written, buffer hit rate = 0.00% # but here it is still have 0 hit rate
    !	Local  blocks:          0 read,          0 written, buffer hit rate = 0.00%
    !	Direct blocks:          0 read,          0 written
```

### Second type of diagram
- Consider the previous diagram doesn't show the how the SQL statement change across the buffer size, we generate a second diagram to compare a SQL Query's buffer hit rate on different number of buffers (i.e.: x-axis is number of buffers). To make the number meaningful, we also run all queries seperately to compare this because if run the queries sequentially we will be comparing a list of 100% for later queries.
- The result of LRU and LFU is in expectation, they have quite similar but different buffer hit rate when the number of buffers is relatively small. When the number of buffers increase, they will approach to the same number.
- The result of MRU still not quite follows our expectation: the buffer hit rate didn't change across different buffer sizes. We tried different ways of implement MRU but still got same group of data so we are using the set of data to precede with our report.

## Conclusion
- The main difficulty of our working on the assignment is about MRU algorithm. Although we implemented different version of the algorithm, the buffer hit rate is still unchanged across different buffer sizes. We will provide our analyze on the actual data we got and the our thinking and insight on the reason of them in the report.

