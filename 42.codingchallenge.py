def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError :
        print("Divide by zero exception")

a = 4
b = 2
print(divide(a,b))
