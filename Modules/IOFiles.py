import os
import send2trash

f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

print(os.getcwd())
print(os.listdir('/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h'))

#shutil.move('practice.txt', '/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h/Modules/TestDir')

# 'Safe delete'
send2trash.send2trash('practice.txt')

# os.walk
file_path = '/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h/Modules/TestDir'
for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print('\n')
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\tSubfolder: {sub_folders}")
    print('\n')
    print('The files are: ')
    for f in files:
        print(f"\t File: {f}")
    print('\n')



