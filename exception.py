# a = 10
# print(a)

a = int(input())
b = int(input())
try:
    def div(a, b):
        c = a / b
        print(c)
    div(a, b)
except:
    print("Exception Caught")


# multiple except
a = int(input())
b = int(input())
try:
    c = a / b
    print("SUCCESS: ", c)
except ZeroDivisionError:
    print("divide by zero error")
except ValueError:
    print("You didn't provided a value")
except:
    print("Exception Caught")


# ELSE
a = int(input())
b = int(input())
try:
    c = a / b
except ZeroDivisionError:
    print("divide by zero error")
except ValueError:
    print("You didn't provided a value")
except:
    print("Exception Caught")
else:
    print("SUCCESS: ", c)



#FINALLY

a = int(input())
b = int(input())
try:
    c = a / b
    # print("SUCCESS: ", c)
except ZeroDivisionError:
    print("divide by zero error")
except ValueError:
    print("You didn't provided a value")
except:
    print("Exception Caught")
else:
    print("SUCCESS: ", c)
finally:
    print("Processing Complete")