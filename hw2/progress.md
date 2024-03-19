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

SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000;
vacuum analyze;


./bin/postmaster -p 14324 -D ./data >logfile 2>&1 &
./bin/createdb hw -p 14324
./bin/psql hw -p 14324



# Lianting Part

```

## nodeHash.c
- Each function plays a specific role in managing hash tables used for hash joins. Here's a brief explanation of each function:

### `ExecHash`
- **Purpose**: Constructs an in-memory hash table from the tuples of the inner relation (the relation on the "inner" side of a hash join). It processes each tuple from the inner relation, computes its hash value, and inserts it into the appropriate bucket in the hash table. If the hash table cannot fit all tuples due to memory constraints, it partitions the data into batches and stores excess tuples in temporary files.
- **Workflow**: Iterates over all tuples in the inner relation, computes hash values, inserts tuples into the hash table or temporary batch files as needed.

### `ExecInitHash`
- **Purpose**: Initializes the hash node within a query execution plan. This involves setting up the hash state, which includes creating the expression context for evaluating hash keys and initializing child plan nodes.
- **Workflow**: Creates and initializes the hash state structure, sets up expression evaluation contexts, and initializes child nodes and tuple slots.

### `ExecEndHash`
- **Purpose**: Cleans up resources associated with the hash node after the hash join is completed. This includes freeing the expression context and shutting down child plan nodes.
- **Workflow**: Frees the expression context and calls `ExecEndNode` on the child nodes to clean up.

### `ExecHashTableCreate`
- **Purpose**: Allocates and initializes a hash table structure for use in a hash join. This involves determining the size of the hash table based on the estimated size of the inner relation, allocating memory for the hash table, and initializing control structures for managing batches and temporary files if needed.
- **Workflow**: Calculates hash table size, allocates memory, initializes control structures for batching.

### `ExecChooseHashTableSize`
- **Purpose**: Determines the optimal size for the hash table and the number of batches, based on the size of the inner relation and available memory. It aims to balance memory usage and performance by adjusting the number of hash buckets and the use of temporary files for batching.
- **Workflow**: Estimates the optimal number of hash buckets and batches based on the estimated size of the inner relation and available memory.

### `ExecHashTableDestroy`
- **Purpose**: Frees all resources associated with a hash table. This includes closing temporary files used for batching, releasing memory used for the hash table and its entries, and deleting the associated memory contexts.
- **Workflow**: Closes temporary files, releases memory, and deletes memory contexts associated with the hash table.

### `ExecHashTableInsert`
- **Purpose**: Inserts a tuple into the hash table. If the tuple belongs to a batch that is not currently being processed, it gets written to a temporary file for later processing.
- **Workflow**: Computes the tuple's hash value, determines the appropriate bucket or batch file, and inserts the tuple accordingly.

### `ExecHashGetBucket`
- **Purpose**: Computes the hash value for a given tuple and determines the corresponding bucket in the hash table.
- **Workflow**: Evaluates hash keys, computes hash value, and returns the bucket number for the tuple.

### `ExecHashGetBatch`
- **Purpose**: Determines which batch a given bucket belongs to. If the bucket is part of the current in-memory hash table, it returns -1; otherwise, it returns the batch number for processing the bucket's tuples from temporary files.
- **Workflow**: Calculates and returns the batch number based on the bucket number and hash table configuration.

### `ExecScanHashBucket`
- **Purpose**: Iterates over tuples in a specific hash bucket that match a given join condition. It's used to find matching tuples from the hash table during the join process.
- **Workflow**: Iterates through tuples in a bucket, applying join conditions to find matches.

### `ExecHashTableReset`
- **Purpose**: Resets the hash table for processing a new batch. This involves clearing out the current contents of the hash table and reinitializing it for the next batch of tuples.
- **Workflow**: Clears current hash table entries, reinitializes bucket headers for a new batch.

### `ExecReScanHash`
- **Purpose**: Prepares the hash node for re-scanning, typically due to a change in the query parameters or for executing a nested loop join. This involves re-scanning the child node if necessary.
- **Workflow**: Checks if the child node's parameters have changed and triggers a re-scan of the child node if required.



## nodeHashjoin.c
The provided code is part of PostgreSQL's implementation for executing hash joins. Hash joins are a method of joining two tables (relations) by using a hash table to improve the efficiency of the join. Below is a brief explanation of each function in the context of executing a hash join:

### `ExecHashJoin`
- **Purpose**: Implements the core logic of the hash join operation. It manages fetching tuples from the outer relation, probing the hash table built on the inner relation for matches, and applying join conditions to produce the result set.
- **Workflow**: If it's the first call, builds a hash table for the inner relation. Then, iterates over tuples from the outer relation, probing the hash table for matching inner tuples. For each match, it checks additional join conditions and produces result tuples until no more matches are found or the outer relation is exhausted.

### `ExecInitHashJoin`
- **Purpose**: Initializes the hash join state, including setting up the expression contexts, initializing child nodes (inner and outer relations), and preparing the hash table structure.
- **Workflow**: Initializes various components necessary for the hash join operation, such as expression contexts for evaluating join conditions and the hash table for the inner relation.

### `ExecEndHashJoin`
- **Purpose**: Cleans up resources used by the hash join, including the hash table and any open temporary files used for batch processing.
- **Workflow**: Destroys the hash table, closes temporary files, and releases memory used during the hash join operation.

### `ExecHashJoinOuterGetTuple`
- **Purpose**: Retrieves the next tuple from the outer relation. During the first pass, tuples are fetched directly from the outer node. In subsequent passes (if batching is used), tuples are read from temporary files.
- **Workflow**: Depending on the current batch, fetches tuples either by executing the outer plan node or reading from a temporary file.

### `ExecHashJoinGetSavedTuple`
- **Purpose**: Reads a tuple from a temporary file during batch processing in a hash join. This function is used when processing batches beyond the first.
- **Workflow**: Reads and reconstructs a tuple from a temporary file, storing it in a provided tuple slot for further processing.

### `ExecHashJoinNewBatch`
- **Purpose**: Prepares the hash join for processing a new batch. This involves resetting the hash table and loading new tuples into it from temporary files.
- **Workflow**: Closes the current batch's files, opens the next batch's files, resets the hash table, and inserts tuples from the new batch's inner file into the hash table.

### `ExecHashJoinSaveTuple`
- **Purpose**: Saves a tuple to a temporary file. This is used when an outer or inner tuple belongs to a future batch and cannot be processed in the current pass.
- **Workflow**: Writes a tuple's data to a specified temporary file for later retrieval during batch processing.

### `ExecReScanHashJoin`
- **Purpose**: Prepares the hash join for re-execution, typically due to a change in the query parameters or a request for a new iteration over the result set.
- **Workflow**: Resets the hash join's state, including the current tuple positions and the hash table. If necessary, the hash table is rebuilt.

Each of these functions plays a specific role in managing the lifecycle of a hash join operation, from initialization and execution to handling batching (if needed due to memory constraints) and cleanup.


## Code
```c

	/* BEGIN NEWCODE */
	
	/* END NEWCODE */
```
