def func():
    print("FUNC() IN ONE.PY")

def function():
    pass

def function1():
    pass

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    # Run the script!
    function()
    function1()
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')
