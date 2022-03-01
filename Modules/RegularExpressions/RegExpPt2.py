import re

text = "The agent's phone number is. Call soon!"
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group(1))
print(results.group(2))
print(results.group(3))
print(results.groups())
print(type(results.groups()))
