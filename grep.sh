#!/bin/bash

# usage: ./grep.sh (lru | lfu | mru)
# example: ./grep.sh lru

# Directory containing the log files, specified by the first argument
logdir="./logs/$1"

# Output file to store the results, specified by the second argument
outputfile="result/$1.txt"

# Empty the output file in case it already exists
> "$outputfile"

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
