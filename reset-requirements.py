def read_and_write(lines):
	with open("output.txt", "w") as output_file:
		for line in lines:
			package = line.split("==")[0] + "\n"
			output_file.write(package)


with open("requirements.txt", "r") as file:
	req_lines = file.readlines()
	read_and_write(req_lines)
