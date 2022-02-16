import re

'''
    (555)-555-5555
    r"(\d\d\d)-\d\d\d-\d\d\d\d"
    r"(\d{3})-\d{3}-\d{4}"
'''

text = "The agent's phone number is 408-555-1234. Call soon!"

pattern = 'phone'
print(re.search(pattern, text))

pattern = 'NOT IN TEXT'
print(re.search(pattern, text))

pattern = 'phone'
print(re.search(pattern, text))

match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())

text = 'my phone once, my phone twice'
match = re.search('phone', text)
print(match)
print(match.span())
print(match.start())
print(match.end())
matches = re.findall('phone', text)
print(matches)
print(len(matches))

for match in re.finditer('phone', text):
    print(match.span())
    print(match.group())
