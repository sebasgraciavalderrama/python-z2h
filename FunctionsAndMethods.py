def name_of_function(name):
    '''
    Docstring explains function
    '''
    print("Hello " + name)

def add_function(num1, num2):
    return num1+num2

def say_hello():
    print("Hello")
    print("Hello")
    print("Hello")

def say_hello(name='Default'):
    print(f'Hello {name}')

myName = "Sebas"
name_of_function(myName)
say_hello()
result = add_function(9887, 88.43)
print(result)