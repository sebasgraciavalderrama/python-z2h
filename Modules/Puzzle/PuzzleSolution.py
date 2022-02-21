import shutil, os, re

shutil.unpack_archive('unzip_me_for_instructions.zip', 'unzip_me_for_instructions_folder', 'zip')

extracted_content = '/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h/Modules/Puzzle/unzip_me_for_instructions_folder/extracted_content'
phone_number = []

counter = 1
for folder, sub_folders, files in os.walk(extracted_content):
    for special_file in files:
        file_path = os.path.join(folder, special_file)
        with open(file_path, 'r+') as read_file:
            #print('reading file: ' + str(counter))
            for line in read_file:
                #print(line)
                phone = re.search(r'\d{3}-\d{3}-\d{4}', line)
                if phone is not None:
                    phone_number.append(phone.group())
                    phone_number.append(counter)
            counter += 1

print(f'Total number of files: {counter}')
print('\n')
print(f'Phone number found in file number: {phone_number[1]}')
print(phone_number[0])