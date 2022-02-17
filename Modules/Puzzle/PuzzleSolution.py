import shutil, os

shutil.unpack_archive('unzip_me_for_instructions.zip', 'unzip_me_for_instructions_folder', 'zip')

unzipme_location = '/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h/Modules/Puzzle/unzip_me_for_instructions_folder'
extracted_content = '/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h/Modules/Puzzle/unzip_me_for_instructions_folder/extracted_content'

my_phone_numbers = []

'''for folder, sub_folders, files in os.walk(unzipme_location):
    print(f"Currently looking at {folder}")
    print('\n')
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\tSubfolder: {sub_folders}")
    print('\n')
    print('The files are: ')
    for f in files:
        print(f"\t File: {f}")
    print('\n')'''

for folder, sub_folders, files in os.walk(extracted_content):
    for sub_fold in sub_folders:
        print(sub_fold)
        for f in files:
            print(f)