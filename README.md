# PostgreSQL Investigation

This repository contains three homework assignments related to PostgreSQL.

## Folder Structure

- `hw1`: Algorithm of PostgreSQL Buffer Pool
- `hw2`: Adding Bloom Filter for Hash Index
- `hw3`: Query Plan Analysis

### hw1: Algorithm of PostgreSQL Buffer Pool

In this assignment, we investigate the buffer pool algorithm of PostgreSQL. The original Least Recently Used (LRU) algorithm is modified to Least Frequently Used (LFU) and Most Recently Used (MRU). The folder contains:

- Implementation of LFU and MRU algorithms.
- A report comparing the results of LRU, LFU, and MRU.

### hw2: Adding Bloom Filter for Hash Index

This assignment involves adding a Bloom filter to the hash index of PostgreSQL. The performance is tested under different numbers of hash functions. The folder contains:

- Implementation of the Bloom filter for the hash index.
- Performance tests with varying numbers of hash functions.
- A report on the performance results.

### hw3: Query Plan Analysis

In this assignment, we test how different queries affect the query plan and how PostgreSQL chooses different indexes to construct the SELECT statement and actual query. The folder contains:

- Various test queries.
- Analysis of query plans.
- A report file explaining the findings and methodology.