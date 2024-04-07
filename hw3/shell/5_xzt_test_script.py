import os
import re
import time
import json
import subprocess

json_output = []

default_statistics_target_size = [10, 500]
# default_statistics_target_size = [10, 20, 30, 50, 100, 128, 150, 200, 250, 256, 300, 350, 400, 450, 500]
actual_pattern = re.compile(r'\s+count\s+-+\s+(\d+)\s+\(1 row\)')

# Adjusted pattern for estimated rows that works with both Seq Scan and Index Scan
# not working
# estimated_pattern = re.compile(r'->\s+(?:Seq Scan|Index Scan) on one\s+\(cost=[\d.]+..[\d.]+ rows=(\d+) width=\d+\)')
# estimated_pattern = re.compile(r'->\s+(?:Seq Scan|Index Scan)\s+\(cost=\d+\.\d+\.\.\d+\.\d+\s+rows=(\d+) width=\d+\)')

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
	sql_commands = [
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 1",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 798",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 1197",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 1198",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 1995",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 1996",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 2395",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 2794",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 3591",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 3592",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 3993",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 3994",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 4393",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 4792",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 5191",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 5590",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 5989",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 6388",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 6787",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 7186",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 7585",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 7984",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 8383",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 8782",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 9181",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b > 9580",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND b < 9979",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 1",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 21",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 41",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 61",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 81",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 101",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 121",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 141",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 161",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 181",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 201",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 221",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 241",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 261",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 281",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 301",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 321",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 341",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 361",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 381",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 401",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 421",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 441",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c < 461",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND c > 481",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 19",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 28",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 32",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 36",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 40",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 44",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 48",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 52",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 56",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 60",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 64",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 68",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 72",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 76",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 80",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 84",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 88",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 92",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 96",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 100",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 104",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 108",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d < 112",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND d > 116",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 20",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 25",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 29",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 33",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 37",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 41",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 45",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 49",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 53",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 57",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 61",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 65",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 69",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 73",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 77",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 81",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 85",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 89",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 93",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 97",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 101",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 105",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a < 109",
		"EXPLAIN SELECT COUNT(*) FROM One, Two WHERE One.id = Two.id AND a > 113"
	]


	# Prepare the SQL commands to be executed
	all_sql_commands = f"""
	SET default_statistics_target = {new_default_statistics_target};
	VACUUM ANALYZE;
	"""

	# Appending each SQL command with a semicolon and a newline character to all_sql_commands
	for command in sql_commands:
		all_sql_commands += command + ";\n"

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
			
		# # also append to the json file
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

