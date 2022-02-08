try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Cannot multiply letters with numbers")

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Cannot divide by 0!")
finally:
    print("All done!")

def ask():
    while True:
        try:
            result = int(input("Input an integer: "))
        except:
            print("An error has occurred, Please try again!")
            continue
        else:
            print("Thank you, your number squared is: " + str(result**2))
            break


ask()