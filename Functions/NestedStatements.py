x =50
def func():
    global x
    print(f'X is {x}')

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    #return x
print(x)
func()

'''
Output:
50
X is 50
I JUST LOCALLY CHANGED GLOBAL X TO NEW VALUE
'''