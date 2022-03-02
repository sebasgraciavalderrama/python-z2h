# Task 1 - Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
import csv, re, numpy, PyPDF2

# Open the file - THIS DOES
data = open('find_the_link.csv', encoding='utf-8')
# Call csv.reader
csv_data = csv.reader(data, delimiter=',')
data_lines = list(csv_data)
url_by_char = []
# Iterate the list of lists
for item in data_lines:
    for character in item:
        # Regex to identify which characters are different from a number.
        char = re.search(r'\D', character)
        # If the regex does not return a valid find (any character different from a number)
        # we move on until we find the next valid find.
        # KEEP IN MIND THIS DOES NOT ALLOW NUMBERS
        # TO BE IN THE URL, THEREFORE ONLY WORKS FOR URL'S WITH NO NUMBERS.
        if char is not None:
            # We add the character to the list
            url_by_char.append(character)
# Since we have a list, we now join it and store the resulting string in a variable
url = ''.join(url_by_char)
print(url)

# Using diagonal function from NumPy
url_by_char_numpy = []
url_numpy = ''.join(numpy.diagonal(data_lines))
print(url_numpy)

# Task 2 - Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can’t download from Google Drive) and find the phone number that is in the document.
f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
phone_number = ''
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(f'Number of pages from the extracted PDF: {len(pdf_text)}' )
#print("Text from PDF: ", *pdf_text, sep='\n')
#print(pdf_text)
for text in pdf_text:
    phone = re.search(r'\d{3}.\d{3}.\d{4}', text)
    if phone is not None:
        phone_number = phone.group().replace('.', ' ')
print(f'The phone number found in the PDF is: {phone_number}')