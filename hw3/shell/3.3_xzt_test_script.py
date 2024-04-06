import os
import re
import time
import json
import subprocess

json_output = []

# default_statistics_target_size = [10, 200]
default_statistics_target_size = [10, 20, 30, 50, 100, 200, 300, 400, 500]

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
		filename = f"sql_output_{new_default_statistics_target}.txt"
		filepath = os.path.join(directory, filename)
		with open(filepath, "w") as output_file:
			output_file.write(result.stdout)
	else:
		print("Error in Postgresql Running")
		print("Error Output:", result.stderr)
	
	# Delete the SQL commands file after using it
	os.remove("sql_commands.sql")

	# Stop the PostgreSQL server
	stop_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/pg_ctl stop -p 54324 -D /cmshome/xuzhitao/cscd43/postgresql-7.4.13/data"
	subprocess.run(stop_command, shell=True)




	# # Read the new content from the logfile
	# logfile_path = "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/logfile"
	# with open(logfile_path, "r") as file:
	# 	logfile_content = file.read()

	# # Delete the logfile after reading its contents
	# os.remove(logfile_path)

	# # Regex pattern to extract the results blocks
	# pattern = r"\*\*+Result\*\*+(.*?)\*\*+End Result\*\*+"
	# results = re.findall(pattern, logfile_content, re.DOTALL)

	# # Assuming each result block corresponds to a SQL command in order
	# # Parse and map the results to the SQL commands
	# mapped_results = []
	# for sql_command, result_block in zip(sql_commands, results):
	# 	# Extract the metrics from the result block
	# 	metrics = {
	# 		"Total Joined Tuples": re.search(r"Total Joined Tuples: (\d+)", result_block).group(1),
	# 		"Total Dropped Tuples (true negative)": re.search(r"Total Dropped Tuples \(true negative\): (\d+)", result_block).group(1),
	# 		"True Positives": re.search(r"True Positives (\d+)", result_block).group(1),
	# 		"Total UnDropped Tuples": re.search(r"Total UnDropped Tuples: (\d+)", result_block).group(1),
	# 		"False Positives": re.search(r"False Positives: (\d+)", result_block).group(1),
	# 		"False Positives Rate": re.search(r"False Positives Rate: ([\d.]+)", result_block).group(1),
	# 	}
	# 	# Map the SQL command to its extracted metrics
	# 	mapped_results.append({
	# 		"SQL Command": sql_command,
	# 		"Metrics": metrics
	# 	})

	# # Convert the mapped results to JSON
	# json_output.append({
	# 	"Bloomfilter size": new_bloomfilter_size, 
	# 	"Hashfunction count": new_bloomfilter_hashfunction_count,
	# 	"results": mapped_results
	# })

	# temp_json_output_str = json.dumps(json_output, indent=4)

	# # Write the results to a JSON file
	# with open("temp_results_q3.json", "w") as file:
	# 	file.write(temp_json_output_str)

	end_time = time.time()  # end time

# json_output_str = json.dumps(json_output, indent=4)

# # Write the results to a JSON file
# with open("results_q3.json", "w") as file:
# 	file.write(json_output_str)

# os.remove("temp_results_q3.json")
