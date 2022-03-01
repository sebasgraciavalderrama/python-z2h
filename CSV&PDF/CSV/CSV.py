import csv

# Open the file
data = open('example.csv', encoding='utf-8')
# Call csv.reader
csv_data = csv.reader(data)
# reformat it intp a python object list of lists
data_lines = list(csv_data)

print(type(data_lines))

print('Items are: ', *data_lines, sep='\n')
print(data_lines[0])
print(len(data_lines))

for line in data_lines[:5]:
    print(line)

print(data_lines[10][3])

all_emails = []

for lines in data_lines[1:]:
    all_emails.append(lines[3])

print('Emails are: ', *all_emails, sep='\n')

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1]+ ' ' + line[2])

print('Full names are: ', *full_names, sep='\n')

# Writing to the csv file
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()
