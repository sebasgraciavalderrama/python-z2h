def even_check(a):
    return a % 2 == 0

# Return true if any number is even inside a list
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass #Do not do anything
            #return False WRONG!!!!!!
    return False

def return_check_even_list(num_list):
    #Return even numbers in a list
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            pass #Do not do anything
    return even_list

myList = [1,3,5,7]
print(check_even_list(myList))

myList = [2,3,5,7]
print(check_even_list(myList))

myList = [1,3,5,2]
print(check_even_list(myList))

evenList = return_check_even_list(myList)
print(evenList)

print(even_check(2975))
