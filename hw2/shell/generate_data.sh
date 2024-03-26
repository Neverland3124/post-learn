#!/bin/bash

# Define the output file
outputFile1="data1.csv"
outputFile2="data2.csv"

# Generate 10000 lines of data
for id in {1..10000}
do
  # Generate random numbers between 1 and 100 for A, B, and C
  a=$((RANDOM % 100 + 1))
  b=$((RANDOM % 100 + 1))
  c=$((RANDOM % 100 + 1))

  # Append the data to the file
  echo "${id},${a},${b},${c}" >> "$outputFile1"
done

# Generate 10000 lines of data
for id in {1..10000}
do
  # Generate random numbers between 1 and 100 for A, B, and C
  a=$((RANDOM % 100 + 1))
  b=$((RANDOM % 100 + 1))
  c=$((RANDOM % 100 + 1))

  # Append the data to the file
  echo "${id},${a},${b},${c}" >> "$outputFile2"
done

echo "Data generation complete. File: $outputFile"
