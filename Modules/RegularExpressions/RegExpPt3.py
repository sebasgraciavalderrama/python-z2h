import re

print(re.search(r'cat|dog', 'The dog is here'))

print(re.findall(r'at','The cat in the hat sat there.'))
print(re.findall(r'.at','The cat in the hat sat there.'))
print(re.findall(r'...at','The cat in the hat sat there when splat.'))
print(re.findall(r'^\d','1 is a number'))
print(re.findall(r'^\d','The 2 is a number'))
print(re.findall(r'\d$','The number is 2'))

phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall(r'[^!.? ]+', test_phrase))
clean = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(clean))

text = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+' # pattern = r'\w+-\w+' <-- this also works!
print(re.findall(pattern, text))

text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)', text))
print(re.search(r'cat(fish|nap|claw)', texttwo))
print(re.search(r'cat(fish|nap|claw)', textthree))

