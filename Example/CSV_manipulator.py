import csv

# Specify the input and output file names
input_file = 'Example/input.csv'
output_file = 'output.csv'

# Read the CSV file
with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Add a new column with a default value
new_column_name = 'NewColumn'
default_value = 'DefaultValue'

# Add the new column to the header
header = data[0] + [new_column_name]

# Add the new column to each row
rows = [row + [default_value] for row in data[1:]]

# Write the modified data to a new CSV file
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Modified data saved to '{output_file}'")
