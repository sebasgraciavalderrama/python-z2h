import random

def gensquares(n):
    for num in range(n):
        yield num**2

for x in gensquares(10):
    print(x)

print('\n')

def rand_numb(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_numb(1, 10, 12):
    print(num)

print('\n')

s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print('\n')

'''
    Image a program to search files, instead of waiting for the search to be completed, and storing the result in memory, we could display the results as the
    program finds it.
'''

print('\n')

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

print(gencomp)
print(type(gencomp))

print(next(gencomp))
print(next(gencomp))

for item in gencomp:
    print(item)

'''
    A generator expression is like a list comprehension, but instead of finding all the items you're interested and 
    packing them into list, it waits, and yields each item out of the expression, one by one.

    Generator expressions make the most sense in scenarios where you need to take one item at a time, do a lot of 
    calculations based on that item, and then move on to the next item. If you need more than one value, you can also 
    use a generator expression and grab a few at a time. If you need all the values before your program proceeds, 
    use a list comprehension instead.
    
    https://stackoverflow.com/questions/364802/how-exactly-does-a-generator-comprehension-work
'''