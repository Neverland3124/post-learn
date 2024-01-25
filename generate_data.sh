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
