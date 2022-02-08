def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("End of try/except/finally")

ask_for_int()



try:
    f = open('testfile', 'w')
    f.write("Write a test line!")
except TypeError:
    print("There was a TypError")
except OSError:
    print("Hey you have an OS Error")
except:
    # When there is no exception specified, it takes all exceptions
    print("All other exceptions!")
finally:
    print("I always run")


