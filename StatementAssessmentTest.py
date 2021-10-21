st = 'Print only the words that start with s in this sentence'

#-----------------------------A---------------------------
new_string = st.split()
for word in new_string:
    if word[0] == 's':
        print(word)
#-----------------------------B---------------------------

x = range(11)
for num in x:
    if num % 2 == 0:
        print(num)

#-----------------------------C---------------------------
my_list = [x for x in range(51) if x % 3 == 0]
print(my_list)

#-----------------------------D---------------------------
words = st.split()
for word in words:
    if len(word) % 2 == 0:
        print("even!")
#-----------------------------E---------------------------
my_numbers = range(1,101)
for num in my_numbers:
    print(num)
    if num % 3 == 0:
        print("Fizz")
        continue
    elif num % 5 == 0:
        print("Buzz")
        continue
    elif num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
        continue
#-----------------------------F---------------------------
st1 = 'Create a list of the first letters of every word in this string'
my_words = [letters[0] for letters in st1.split()]
print(my_words)