#!/bin/bash

# neeed to copy the file to the postgres directory
# cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hw1/code/original_files/buf_init.c" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/backend/storage/buffer/buf_init.c"
# cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hw1/code/original_files/bufmgr.c" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/backend/storage/buffer/bufmgr.c"
# cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hw1/code/original_files/freelist.c" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/backend/storage/buffer/freelist.c"
# cat "/cmshome/xuzhitao/cscd43/cscd43-personal-hw1/code/original_files/buf_internals.h" > "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/src/include/storage/buf_internals.h"

# # need to re gmake everything
# cd /cmshome/xuzhitao/cscd43/postgresql-7.4.13
# gmake clean && gmake uninstall && gmake && gmake install
# cd /cmshome/xuzhitao/cscd43/cscd43-personal-hw1

# Input file containing SQL queries
QUERY_FILE="ScanQueries.sql"

ALGO="lru"

# Output directory for logs
LOG_DIR="./logs/$ALGO"

# Ensure the log directory exists
mkdir -p "$LOG_DIR"

# PostgreSQL command settings
PG_CMD="/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres"
PG_DATA_DIR="/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/"
DB_NAME="test"
DEBUG_LEVEL="1"

# Buffer sizes to test with
BUFFER_SIZES=(20 30 40 50 75 100 200)

# Loop through each buffer size
for buffer_size in "${BUFFER_SIZES[@]}"; do
    # Construct the log file name based on the buffer size
    log_file="$LOG_DIR/${buffer_size}_scan.log"

    > "$log_file" # Clear the log file
    
    # Read each query from the file and execute it
    while IFS= read -r query; do
        if [[ ! -z "$query" ]]; then # Skip empty lines
            # Use echo to pass the query to PostgreSQL command and append the output to the log file
            echo "$query" | "$PG_CMD" -B "$buffer_size" -D "$PG_DATA_DIR" -d "$DEBUG_LEVEL" -s "$DB_NAME" >> "$log_file" 2>&1
        fi
    done < "$QUERY_FILE"

    echo "end file $log_file"
done


# Input file containing SQL queries
QUERY_FILE_2="IndexScanQueries.sql"

# Loop through each buffer size
for buffer_size in "${BUFFER_SIZES[@]}"; do
    # Construct the log file name based on the buffer size
    log_file="$LOG_DIR/${buffer_size}_indexscan.log"

    > "$log_file" # Clear the log file
    
    # Read each query from the file and execute it
    while IFS= read -r query; do
        if [[ ! -z "$query" ]]; then # Skip empty lines
            # Use echo to pass the query to PostgreSQL command and append the output to the log file
            echo "$query" | "$PG_CMD" -B "$buffer_size" -D "$PG_DATA_DIR" -d "$DEBUG_LEVEL" -s "$DB_NAME" >> "$log_file" 2>&1
        fi
    done < "$QUERY_FILE_2"

    echo "end file $log_file"
done

mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/20_scan.log 2>&1
mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/30_scan.log 2>&1
mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 40 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/50_scan.log 2>&1 
mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/50_scan.log 2>&1 
mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 75 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/75_scan.log 2>&1 
mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/100_scan.log 2>&1
mkdir -p ./logs_sequential/lru/ && cat ScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/200_scan.log 2>&1

mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 20 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/20_indexscan.log 2>&1
mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 30 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/30_indexscan.log 2>&1
mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 40 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/50_indexscan.log 2>&1 
mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 50 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/50_indexscan.log 2>&1 
mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 75 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/75_indexscan.log 2>&1 
mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 100 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/100_indexscan.log 2>&1
mkdir -p ./logs_sequential/lru/ && cat IndexScanQueries.sql | '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postgres' -B 200 -D '/cmshome/xuzhitao/cscd43/postgresql-7.4.13/data/' -d 1 -s test > ./logs_sequential/lru/200_indexscan.log 2>&1

# Directory containing the log files, specified by the first argument
logdir="./logs/$ALGO"

# Output file to store the results, specified by the second argument
outputfile="./result/$ALGO.txt"

# Empty the output file in case it already exists
> "$outputfile"

echo "Processing log files in $logdir and writing results to $outputfile"

# Loop through all files in the log directory
for logfile in "$logdir"/*
do
    # Check if the file is a regular file (not a directory or a link, etc.)
    if [ -f "$logfile" ]; then
        # Write the filename to the output file
        echo "File: $(basename "$logfile")" >> "$outputfile"
        
        # Use awk to extract and process buffer hit rates
        awk '
        /buffer hit rate = / {
            count++; # Increment count for each match
            # Process only odd occurrences
            if (count % 2 == 1) {
                gsub(/.*buffer hit rate = |%/, "", $0); # Remove everything except the numeric rate
                print $0 "%"; # Append '%' and print
            }
        }
        ' "$logfile" >> "$outputfile"
        
        # Reset the count for the next file
        awk 'BEGIN{count=0}' > /dev/null
        
        # Add a newline for separation between files for readability
        echo "" >> "$outputfile"
    fi
done


# Directory containing the log files, specified by the first argument
logdir="./logs_sequential/$ALGO"

# Output file to store the results, specified by the second argument
outputfile="./result_sequential/$ALGO.txt"

mkdir -p ./result_sequential
# Empty the output file in case it already exists
> "$outputfile"

echo "Processing log files in $logdir and writing results to $outputfile"

# Loop through all files in the log directory
for logfile in "$logdir"/*
do
    # Check if the file is a regular file (not a directory or a link, etc.)
    if [ -f "$logfile" ]; then
        # Write the filename to the output file
        echo "File: $(basename "$logfile")" >> "$outputfile"
        
        # Use awk to extract and process buffer hit rates
        awk '
        /buffer hit rate = / {
            count++; # Increment count for each match
            # Process only odd occurrences
            if (count % 2 == 1) {
                gsub(/.*buffer hit rate = |%/, "", $0); # Remove everything except the numeric rate
                print $0 "%"; # Append '%' and print
            }
        }
        ' "$logfile" >> "$outputfile"
        
        # Reset the count for the next file
        awk 'BEGIN{count=0}' > /dev/null
        
        # Add a newline for separation between files for readability
        echo "" >> "$outputfile"
    fi
done