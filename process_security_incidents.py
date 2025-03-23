import csv
 
security_incidents = 'security_incidents.csv'
security_incidents_modified = 'security_incidents_modified.csv'

#read file
with open(security_incidents, mode='r') as input_file:
    reader = csv.reader(input_file)
    csv_data = list(reader)

#add new column & default value
new_column_name = 'Status'
default_value = "Pending"

#add our new column to header
header = csv_data[0] + [new_column_name]

#add default value to each row
rows = [row + [default_value] for row in csv_data[1:]]

#write to a new csv
with open(security_incidents_modified, mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Data modified and saved to {security_incidents_modified}")