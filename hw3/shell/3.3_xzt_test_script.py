import os
import re
import time
import json
import subprocess

json_output = []

default_statistics_target_size = [10, 200]
# default_statistics_target_size = [10, 20, 30, 50, 100, 200, 300, 400, 500]
actual_pattern = re.compile(r'\s+count\s+-+\s+(\d+)\s+\(1 row\)')

# Adjusted pattern for estimated rows that works with both Seq Scan and Index Scan
estimated_pattern = re.compile(r'->\s+(?:Seq Scan|Index Scan) on one\s+\(cost=[\d.]+..[\d.]+ rows=(\d+) width=\d+\)')


directory = "result_1"
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
		"SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 10 AND c < 60",
		"SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 90 AND c < 320",
		"SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 200 AND c < 250",
		"SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 240 AND c < 460",
		"SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 300 AND c < 350",
		"SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 325 AND c < 400",
		"SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 400 AND c < 490",
		"SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 380 AND c < 500",
		"SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 1 AND c < 100",
		"SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455",
		"EXPLAIN SELECT COUNT(*) FROM One WHERE c > 100 AND c < 455"
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
			
		# also append to the json file
		actual_counts = actual_pattern.findall(result.stdout)
		estimated_rows = estimated_pattern.findall(result.stdout)
        
        # Combine the actual and estimated counts into a list of dictionaries
		command_results = []
		for actual, estimated in zip(actual_counts, estimated_rows):
			command_results.append({'actual': int(actual), 'estimated': int(estimated)})
        
        # Append the results for this default_statistics_target_size
		json_output.append({
			'default_statistics_target': sizes,
			'results': command_results
		})


	else:
		print("Error in Postgresql Running")
		print("Error Output:", result.stderr)
	
	# Delete the SQL commands file after using it
	os.remove("sql_commands.sql")

	# Stop the PostgreSQL server
	stop_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/pg_ctl stop -p 54324 -D /cmshome/xuzhitao/cscd43/postgresql-7.4.13/data"
	subprocess.run(stop_command, shell=True)


	end_time = time.time()  # end time

json_filepath = os.path.join(directory, "summary_results.json")
with open(json_filepath, "w") as json_file:
	json.dump(json_output, json_file, indent=4)

