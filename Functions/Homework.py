import math, string

def vol(rad):
    return (4.0/3.0)*math.pi*pow(rad,3)

print(vol(2))

def ran_check(num, low, high):
    if num in range(low, high):
        print(f'{num} is in the range between {low} and {high}')

ran_check(3,1,10)

def ran_bool(num, low, high):
    if num in range(low, high):
        return True
    return False

print(ran_bool(3,1,10))

def up_low(s):
    upper_case_chars = 0
    lower_case_chars = 0
    for char in s:
        if char.isupper():
            upper_case_chars += 1
        elif char.islower():
            lower_case_chars += 1
    print(f'No. of Upper case characters :  {upper_case_chars}')
    print(f'No. of Lower case Characters :  {lower_case_chars}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply([1, 2, 3, -4]))

def palindrome(s):
    if s == s[::-1]:
        return True
    return False

print(palindrome('helleh'))

def ispangram(str1, alphabet=string.ascii_lowercase):
    count = 0
    lowered_str1 = str1.lower().replace(' ', '')
    for j, char2 in enumerate(alphabet):
        for i, char in enumerate(lowered_str1):
            if char[i] == char2[j]:
                count += 1
            if count == len(alphabet):
                return True
    return False

def ispangram_powered(str1, alphabet=string.ascii_lowercase):
    alphabet_set = set()
    lowered_str1 = str1.lower().replace(' ', '')
    unique_chars_from_word = set(lowered_str1)
    for char in alphabet:
        alphabet_set.add(char)
    if len(unique_chars_from_word) == len(alphabet_set):
        return True
    return False



print(ispangram_powered('The quick brown fox jumps over the lazy dog')) #True

print(ispangram_powered('Glib jocks quiz nymph to vex dwarf')) # True

print(ispangram_powered('aaaaiiiihhh ss')) # False