def simple_func():
    return 1

def hello(name='Sebas'):
    print('The hello() function has been executed!!!')

    def greet():
        return '\t This is the greet func inside hello!!!'
    def welcome():
        return '\t This is the welcome func inside hello!!!'
    # print(greet())
    # print(welcome())
    # print('This is the end of the hello func!')
    print('I am going to return a function!')

    if name == 'Sebas':
        return greet
    else:
        return welcome

def cool():
    def super_cool():
        return 'I am very cool'
    return super_cool

# Passing a func as an argument
def hi():
    return 'Hi Sebas!'

def other(some_func):
    print('Other code runs here!!')
    print(some_func())




if __name__ == '__main__':
    my_new_func = hello()
    print(my_new_func)
    print(my_new_func())

    some_func = cool()
    print(some_func)
    print(some_func())

    other(hi)
    