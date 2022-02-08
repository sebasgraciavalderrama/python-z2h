def add(n1, n2):
    print(n1+n2)


number1 = 10

number2 = input("Please provide a number: ")
#add(number1, number2)
print("Print something!!")

try:
    # Want to attempt this code
    # may have an error
    #result = 10 + 10
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

