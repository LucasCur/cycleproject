import re
import csv

# Input file path
input_file_path = 'srcdata2.txt'

# Output file path
output_file_path = 'output_links.csv'

# Regular expression pattern to extract src values
pattern = r'src="(https://cdn.thecyclemap.info/[^"]+)"'

# Open input file for reading
with open(input_file_path, 'r') as input_file:
    # Read the content of the file
    content = input_file.read()

    # Use regular expression to find all src values
    src_values = re.findall(pattern, content)

    # Open output file for writing
    with open(output_file_path, 'w', newline='') as output_file:
        # Create a CSV writer
        csv_writer = csv.writer(output_file)

        # Write the src values to the CSV file
        csv_writer.writerow(src_values)

print(f"Extracted {len(src_values)} links and saved to {output_file_path}.")
