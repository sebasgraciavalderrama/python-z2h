'''
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
'''
def create_cubes(n):
    result = []
    for x in range(n):
        yield x ** 3

def gen_fibonacci(n):
    a = 1
    b = 1
    # output = []
    for i in range(n):
        # output.append(a)
        yield a
        a,b = b, a+b

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
'''
print(next(g))
Traceback (most recent call last):
  my/generic/path, line 34, in <module>
    print(next(g))
StopIteration
'''
print('\n')
print(create_cubes(10))
print(list(create_cubes(10)))
for x in create_cubes(10):
    print(x)
print('\n')
for number in gen_fibonacci(10):
    print(number)
print('\n')

s = 'hello'
for letter in s:
    print(letter)
print('\n')
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))