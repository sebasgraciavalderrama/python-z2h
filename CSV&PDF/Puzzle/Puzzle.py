# Task 1 - Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).
import csv, re

# Open the file
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
        if char is not None:
            # We add the character to the list
            url_by_char.append(character)
# Since we have a list, we now join it and store the resulting string in a variable
url = ''.join(url_by_char)
print(url)


# Task 2 - Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can’t download from Google Drive) and find the phone number that is in the document.
