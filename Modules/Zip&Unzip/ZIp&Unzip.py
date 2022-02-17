import zipfile, shutil

f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TOW FILE')
f.close()

# ZIP
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# UNZIP
zip_object = zipfile.ZipFile('comp_file.zip', 'r')
zip_object.extractall('extracted_content')


# Pack a directory to a .zip
dir_to_zip = '/Users/sgracia/Documents/GitHub/Z2H-Python/python-z2h/Modules/Zip&Unzip/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)

# Unpack a .zip to a directory
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')