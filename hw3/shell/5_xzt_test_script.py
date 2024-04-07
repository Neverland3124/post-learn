import os
import re
import time
import json
import subprocess

json_output = []

default_statistics_target_size = [10, 400, 500]
# default_statistics_target_size = [10, 20, 30, 50, 100, 128, 150, 200, 250, 256, 300, 350, 400, 450, 500]
actual_pattern = re.compile(r'\s+count\s+-+\s+(\d+)\s+\(1 row\)')

# Adjusted pattern for estimated rows that works with both Seq Scan and Index Scan
# not working
# estimated_pattern = re.compile(r'->\s+(?:Seq Scan|Index Scan) on one\s+\(cost=[\d.]+..[\d.]+ rows=(\d+) width=\d+\)')
# estimated_pattern = re.compile(r'->\s+(?:Seq Scan|Index Scan)\s+\(cost=\d+\.\d+\.\.\d+\.\d+\s+rows=(\d+) width=\d+\)')
pattern = re.compile(
	r'->\s+(?P<join_type>Merge Join|Hash Join|Nested Loop).*?rows=(?P<rows1>\d+).*?'
	r'(?:->\s+Index Scan|->\s+Seq Scan).*?rows=(?P<rows2>\d+)',
    re.DOTALL | re.MULTILINE
)


estimated_pattern = re.compile(
	r'->\s+(?:Seq Scan|Index Scan).*?\(cost=\d+\.\d+..\d+\.\d+\s+rows=(\d+) width=\d+\)',
	re.DOTALL  # This flag allows '.' to match newlines
)

directory = "result_3"
os.makedirs(directory, exist_ok=True)


# Ensure the directory exists

index = 0
nums = len(default_statistics_target_size)
start_time = 0
end_time = 130

for sizes in default_statistics_target_size:
	index += 1

	elapsed_time = end_time - start_time # Calculate elapsed time

	print(f"Iteration: ({index} / {nums})")
	print(f"Expected additional running time: {(nums - index + 1) * elapsed_time // 60} minutes")
	
	start_time = time.time() # start time

	# The variables to be modified and their new values
	new_default_statistics_target = sizes  # The new value for BLOOMFILTER_SIZE

	# Start the PostgreSQL server
	start_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postmaster -p 54324 -D /cmshome/xuzhitao/cscd43/postgresql-7.4.13/data > /cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/logfile 2>&1 &"
	subprocess.run(start_command, shell=True)

	# Wait for the server to start
	time.sleep(10)

	# Your SQL commands, for mapping purposes
	# Prepare the SQL commands to be executed
	all_sql_commands = f"""
	SET default_statistics_target = {new_default_statistics_target};
	ALTER TABLE One DROP CONSTRAINT IF EXISTS one_pk;
	ALTER TABLE Two DROP CONSTRAINT IF EXISTS two_pk;
	ALTER TABLE Two DROP CONSTRAINT IF EXISTS two_fk_one;
	VACUUM ANALYZE;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 3049 AND One.b < 5048 AND Two.a > 71 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 5923 AND One.b < 7922 AND Two.a > 78 AND Two.a < 97;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 4484 AND One.b < 6483 AND Two.a > 40 AND Two.a < 59;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 3351 AND One.b < 5350 AND Two.a > 87 AND Two.a < 106;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 3930 AND One.b < 5929 AND Two.a > 25 AND Two.a < 44;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 5947 AND One.b < 7946 AND Two.a > 66 AND Two.a < 85;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 5572 AND One.b < 7571 AND Two.a > 35 AND Two.a < 54;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 2481 AND One.b < 5480 AND Two.a > 46 AND Two.a < 75;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1504 AND One.b < 4503 AND Two.a > 35 AND Two.a < 64;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 0 AND One.b < 9999 AND Two.a > 21 AND Two.a < 41;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 300 AND One.b < 7299 AND Two.a < 101;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 600 AND One.b < 4599 AND Two.a > 41 AND Two.a < 61;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 700 AND One.b < 3699 AND Two.a > 61;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 800 AND One.b < 2799 AND Two.a > 81 AND Two.a < 101;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 900 AND One.b < 1899 AND Two.a > 101 AND Two.a < 121;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 0 AND One.b < 1000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1000 AND One.b < 2000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 2000 AND One.b < 3000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 3000 AND One.b < 4000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 4000 AND One.b < 5000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 5000 AND One.b < 6000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 6000 AND One.b < 7000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 100 AND One.c < 200 AND Two.a > 41;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 300 AND One.c < 400 AND  Two.a < 101;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 400 AND One.c < 500 AND Two.a > 101 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 50 AND One.c < 450 AND Two.a > 30 AND Two.a < 75;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 250 AND One.c < 450 AND Two.a > 95 AND Two.a < 115;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 200 AND One.c < 499 AND Two.a > 60 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 1 AND One.c < 150 AND Two.a > 22;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 10 AND One.c < 200 AND Two.a > 82 AND Two.a < 102;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 200 AND One.c < 350 AND Two.a > 102 AND Two.a < 122;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 350 AND One.c < 499 AND Two.a > 25 AND Two.a < 45;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 20 AND One.c < 480 AND Two.a > 62 AND Two.a < 82;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 30 AND One.c < 470 AND Two.a > 22 AND Two.a < 102;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 40 AND One.c < 460 AND Two.a > 102 AND Two.a < 122;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 80 AND One.c < 420 AND Two.a > 82 AND Two.a < 102;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 90 AND One.c < 410 AND Two.a > 102 AND Two.a < 122;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 0 AND One.c < 50 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 50 AND One.c < 100 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 100 AND One.c < 150 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 150 AND One.c < 200 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 300 AND One.c < 350 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 100 AND One.d < 120 AND Two.a > 80 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 40 AND One.d < 80 AND Two.a > 30 AND Two.a < 60;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 80 AND One.d < 120 AND Two.a > 20 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 70 AND Two.a > 70 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 30 AND One.d < 90 AND Two.a > 40 AND Two.a < 100;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 21 AND One.d < 40 AND Two.a > 24 AND Two.a < 74;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 100 AND Two.a > 34 AND Two.a < 64;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 60 AND One.d < 80 AND Two.a > 64 AND Two.a < 84;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 100 AND Two.a > 54 AND Two.a < 114;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 100 AND One.d < 120 AND Two.a > 104 AND Two.a < 124;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1 AND One.b < 9999 AND Two.a > 21 AND Two.a < 80;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1 AND One.b < 9999 AND Two.a > 100 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 1 AND One.c < 500 AND Two.a > 21 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 1 AND One.c < 500 AND Two.a > 60 AND Two.a < 80;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 1 AND One.c < 500 AND Two.a > 70 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 120 AND Two.a > 21 AND Two.a < 60;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 120 AND Two.a > 30 AND Two.a < 80;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 120 AND Two.a > 100 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1 AND One.b > 2000 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 4000 AND One.b < 5999 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 400 AND One.c < 500 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 50 AND One.d < 40.0 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 100 AND One.d < 40.0 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 20 AND One.d < 40 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 40 AND One.d < 80 AND Two.a > 21 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 2000 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 100 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 30 AND Two.a < 120; 
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 0 AND One.b < 8000 AND Two.a > 20 AND Two.a < 110;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1000 AND One.b < 9000 AND Two.a > 25 AND Two.a < 115;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 500 AND One.b < 8500 AND Two.a > 30 AND Two.a < 100;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 1500 AND One.b < 9500 AND Two.a > 35 AND Two.a < 105;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 2000 AND One.b < 9999 AND Two.a > 40 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 2500 AND One.b < 7500 AND Two.a > 45 AND Two.a < 95;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 3000 AND One.b < 7000 AND Two.a > 50 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 3500 AND One.b < 6500 AND Two.a > 55 AND Two.a < 85;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 4000 AND One.b < 6000 AND Two.a > 60 AND Two.a < 110;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.b > 0 AND One.b < 5000 AND Two.a > 65 AND Two.a < 105;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 10 AND One.c < 450 AND Two.a > 30 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 20 AND One.c < 400 AND Two.a > 35 AND Two.a < 115;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 30 AND One.c < 350 AND Two.a > 40 AND Two.a < 110;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 40 AND One.c < 300 AND Two.a > 45 AND Two.a < 105;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 50 AND One.c < 250 AND Two.a > 50 AND Two.a < 100;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 60 AND One.c < 450 AND Two.a > 55 AND Two.a < 95;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 70 AND One.c < 400 AND Two.a > 60 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 80 AND One.c < 350 AND Two.a > 65 AND Two.a < 85;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 90 AND One.c < 300 AND Two.a > 70 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.c > 100 AND One.c < 250 AND Two.a > 75 AND Two.a < 115;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 30 AND One.d < 100 AND Two.a > 35 AND Two.a < 105;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 35 AND One.d < 95 AND Two.a > 40 AND Two.a < 100;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 40 AND One.d < 90 AND Two.a > 45 AND Two.a < 95;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 45 AND One.d < 85 AND Two.a > 50 AND Two.a < 90;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 50 AND One.d < 80 AND Two.a > 55 AND Two.a < 85;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 55 AND One.d < 75 AND Two.a > 60 AND Two.a < 80;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 60 AND One.d < 70 AND Two.a > 65 AND Two.a < 75;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 65 AND One.d < 115 AND Two.a > 70 AND Two.a < 120;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 70 AND One.d < 110 AND Two.a > 75 AND Two.a < 115;
    EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND One.d > 75 AND One.d < 105 AND Two.a > 80 AND Two.a < 110;

	"""

	# Appending each SQL command with a semicolon and a newline character to all_sql_commands
	# for command in sql_commands:
	# 	all_sql_commands += command + ";\n"

	# Write the SQL commands to a file
	with open("sql_commands.sql", "w") as file:
		file.write(all_sql_commands)

	# Execute the SQL commands using psql
	psql_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/psql hw -p 54324 -f sql_commands.sql"
	result = subprocess.run(psql_command, shell=True, capture_output=True, text=True)

	# Print the output and errors
	if result.returncode == 0:
		print("Postgresql Running Successful")
		# write to sql_output_#.txt
		filename = f"sql_output_{new_default_statistics_target}.txt"
		filepath = os.path.join(directory, filename)
		with open(filepath, "w") as output_file:
			output_file.write(result.stdout)
			
		
		# query_details = []
		# # also append to the json file
		# pattern_counts = pattern.findall(result.stdout)
		# for match in pattern_counts:
		# 	join_type, rows1, rows2 = match
		# 	query_details.append((join_type, rows1, rows2))


		# output_filename = f'./result_3/5.3_output_{new_default_statistics_target}.txt'

		# # Open the file in write mode and print the details
		# with open(output_filename, 'w') as output_file:
		# 	for detail in query_details:
		# 		# Convert the detail tuple to a string and write it to the file
		# 		# Assuming you want each detail on a new line
		# 		output_file.write(f"{detail}\n")

		# print(f"Details have been written to {output_filename}")

		# actual_counts = actual_pattern.findall(result.stdout)
		# # print(actual_counts)
		# estimated_rows = estimated_pattern.findall(result.stdout)
		# # print(estimated_rows)
        
        # # Combine the actual and estimated counts into a list of dictionaries
		# command_results = []
		# for actual, estimated in zip(actual_counts, estimated_rows):
		# 	actual = int(actual)
		# 	estimated = int(estimated)
		# 	error = abs(estimated - actual) / actual if actual != 0 else 0
		# 	command_results.append({'actual': actual, 'estimated': estimated, 'error': error})

		# # print(command_results)
		
		# set_estimation_errors = [result['error'] for result in command_results]
		# if set_estimation_errors:
		# 	avg_set_error = sum(set_estimation_errors) / len(set_estimation_errors)
		# 	# print(f"Average estimation error for size {sizes}: round: {avg_set_error:.4f}")
		# 	print(f"Average estimation error for size {sizes}: unround:{avg_set_error:f}")
		# else:
		# 	print(f"No estimation errors calculated for size {sizes}.")
        
        # # Append the results for this default_statistics_target_size
		# json_output.append({
		# 	'default_statistics_target': sizes,
		# 	'results': command_results
		# })


	else:
		print("Error in Postgresql Running")
		print("Error Output:", result.stderr)
	
	# Delete the SQL commands file after using it
	os.remove("sql_commands.sql")

	# Stop the PostgreSQL server
	stop_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/pg_ctl stop -p 54324 -D /cmshome/xuzhitao/cscd43/postgresql-7.4.13/data"
	subprocess.run(stop_command, shell=True)


	end_time = time.time()  # end time

# json_filepath = os.path.join(directory, "summary_results.json")
# with open(json_filepath, "w") as json_file:
# 	json.dump(json_output, json_file, indent=4)

# Define the filename where you want to save the details

