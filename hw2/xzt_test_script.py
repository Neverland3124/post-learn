import os
import re
import time
import json
import subprocess

json_output = []

bloomfilter_sizes = [2000, 5000, 10000, 20000, 40000, 81920]
hashfunction_counts = [2, 3, 4]

index = 0
nums = len(bloomfilter_sizes) * len(hashfunction_counts)
start_time = 0
end_time = 130

for sizes in bloomfilter_sizes:
	for counts in hashfunction_counts:
		index += 1

		elapsed_time = end_time - start_time # Calculate elapsed time

		print(f"Iteration: ({index} / {nums})")
		print(f"Expected additional running time: {(nums - index + 1) * elapsed_time // 60} minutes")
		
		start_time = time.time() # start time

		# The variables to be modified and their new values
		new_bloomfilter_size = sizes  # The new value for BLOOMFILTER_SIZE
		new_bloomfilter_hashfunction_count = counts  # The new value for BLOOMFILTER_HASHFUNCTION_COUNT

		# The path to the file
		file_path = './code_my/nodeHash.c'

		# Reading the content of the file
		with open(file_path, 'r') as file:
			lines = file.readlines()

		# Modifying the values of specified variables
		for i, line in enumerate(lines):
			if 'const static int BLOOMFILTER_SIZE =' in line:
				# Replace the line with the new BLOOMFILTER_SIZE value
				lines[i] = f'const static int BLOOMFILTER_SIZE = {new_bloomfilter_size};\n'
			elif 'const static int BLOOMFILTER_HASHFUNCTION_COUNT =' in line:
				# Replace the line with the new BLOOMFILTER_HASHFUNCTION_COUNT value
				lines[i] = f'const static int BLOOMFILTER_HASHFUNCTION_COUNT = {new_bloomfilter_hashfunction_count};\n'

		# Writing the modified content back to the file
		with open(file_path, 'w') as file:
			file.writelines(lines)

		print(f'bloomfilter_size = {new_bloomfilter_size}')
		print(f'bloomfilter_hashfunction_count = {new_bloomfilter_hashfunction_count}')
		print('File updated successfully.')

		# The shell command you want to execute
		shell_command = './shell/2_my_code_zhitao.sh'

		print('Compiling...')

		# Using subprocess.run to execute the shell command
		result = subprocess.run(shell_command, shell=True, capture_output=True, text=True)

		# Check if the command was executed successfully
		if result.returncode == 0:
			print("Postgresql Build Successful")
		else:
			print("Error in Postgresql Building")
			print("Error Output:", result.stderr)

		# Start the PostgreSQL server
		start_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/postmaster -p 54324 -D /cmshome/xuzhitao/cscd43/postgresql-7.4.13/data > /cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/logfile 2>&1 &"
		subprocess.run(start_command, shell=True)

		# Wait for the server to start
		time.sleep(10)

		# Your SQL commands, for mapping purposes
		sql_commands = [
			"SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 3000 AND S.ID > 1000",
			"SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 4500 AND S.ID > 1000",
			"SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 6000 AND S.ID > 1000",
			"SELECT COUNT(*) FROM R, S WHERE R.ID = S.ID AND R.ID < 7500 AND S.ID > 1000"
		]

		# Prepare the SQL commands to be executed
		all_sql_commands = """
		SET enable_nestloop TO off;
		SET enable_mergejoin TO off;
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
		else:
			print("Error in Postgresql Running")
			print("Error Output:", result.stderr)
		
		# Delete the SQL commands file after using it
		os.remove("sql_commands.sql")

		# Stop the PostgreSQL server
		stop_command = "/cmshome/xuzhitao/cscd43/postgresql-7.4.13/bin/pg_ctl stop -p 54324 -D /cmshome/xuzhitao/cscd43/postgresql-7.4.13/data"
		subprocess.run(stop_command, shell=True)

		# Read the new content from the logfile
		logfile_path = "/cmshome/xuzhitao/cscd43/cscd43-personal-hws/hw2/logfile"
		with open(logfile_path, "r") as file:
			logfile_content = file.read()

		# Delete the logfile after reading its contents
		os.remove(logfile_path)

		# Regex pattern to extract the results blocks
		pattern = r"\*\*+Result\*\*+(.*?)\*\*+End Result\*\*+"
		results = re.findall(pattern, logfile_content, re.DOTALL)

		# Assuming each result block corresponds to a SQL command in order
		# Parse and map the results to the SQL commands
		mapped_results = []
		for sql_command, result_block in zip(sql_commands, results):
			# Extract the metrics from the result block
			metrics = {
				"Total Joined Tuples": re.search(r"Total Joined Tuples: (\d+)", result_block).group(1),
				"Total Dropped Tuples (true negative)": re.search(r"Total Dropped Tuples \(true negative\): (\d+)", result_block).group(1),
				"True Positives": re.search(r"True Positives (\d+)", result_block).group(1),
				"Total UnDropped Tuples": re.search(r"Total UnDropped Tuples: (\d+)", result_block).group(1),
				"False Positives": re.search(r"False Positives: (\d+)", result_block).group(1),
				"False Positives Rate": re.search(r"False Positives Rate: ([\d.]+)", result_block).group(1),
			}
			# Map the SQL command to its extracted metrics
			mapped_results.append({
				"SQL Command": sql_command,
				"Metrics": metrics
			})

		# Convert the mapped results to JSON
		json_output.append({
			"Bloomfilter size": new_bloomfilter_size, 
			"Hashfunction count": new_bloomfilter_hashfunction_count,
			"results": mapped_results
		})

		temp_json_output_str = json.dumps(json_output, indent=4)

		# Write the results to a JSON file
		with open("temp_results.json", "w") as file:
			file.write(temp_json_output_str)

		end_time = time.time()  # end time

json_output_str = json.dumps(json_output, indent=4)

# Write the results to a JSON file
with open("results.json", "w") as file:
	file.write(json_output_str)

os.remove("temp_results.json")
