import time, timeit

def func1(number):
    return [str(num) for num in range(number)]

def func2(number):
    return list(map(str, range(number)))

print(func1(10))
print(func2(10))

# CURRENT TIME BEFORE
start_time = time.time()
# RUN CODE
result = func1(100)
# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time)

# CURRENT TIME BEFORE
start_time = time.time()
# RUN CODE
result = func2(100)
# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
# ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time)


# With TIMEIT
stmt = '''
func1(100)
'''

setup = '''
def func1(number):
    return [str(num) for num in range(number)]
'''

print(timeit.timeit(stmt,setup, number=1000000))

stmt2 = '''
func2(100)
'''

setup2 = '''
def func2(number):
    return list(map(str, range(number)))
'''

print(timeit.timeit(stmt2,setup2, number=1000000))