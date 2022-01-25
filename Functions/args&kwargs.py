def myfunc(a,b):
    return sum((a,b)) * 0.05

def myfunc(*args):
    return sum(args) * 0.05

def myfunc(*myargs):
    return sum(myargs) * 0.05

#tuple of arguments
def myfunc(*myargs):
    for item in myargs:
        print(item)

#dictionarie of arguments
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

def myfunc_text(*args):
    mystring = ''
    for i in args[0]:
        if i.isupper():
            mystring += i.lower()
        else:
            mystring += i.upper()
    return mystring

def myfunc_text_even(*args):
    mystring = ''
    for i,char in enumerate(args[0]):
        if i%2 == 0:
            mystring += char.lower()
        else:
            mystring += char.upper()
    return mystring


def myfunc(*args, **kwargs):
        print('I would like {} {}'.format(args[0], kwargs['food']))
#print(myfunc(40,60,51,48,15,48,11,845,845,18))

myfunc(10,20,30, fruit='orange', food='pizza', animal='chicken')

print(myfunc_text('Sumamamemima'))
print(myfunc_text_even('Sumamamemima'))