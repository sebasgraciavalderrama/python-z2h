def square (num):
    return num**2

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]

def check_even(num):
    return num % 2 == 0
'''
Lambda expression is known as an anonymous function, the reason for that is because
lambda expressions are meant to be used only once.
Hence, they don't need a name or the keyword def

1) lambda num: num**2

2) lambda num: num % 2 == 0
'''

my_nums = [1,2,3,4,5,6]
names = ['Andy', 'Eve', 'Sally']

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))
print(list(map(splicer, names)))
print(list(filter(check_even, my_nums)))
print(list(map(lambda num:num ** 2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))
print(list(map(lambda name: name[0], names)))
s
