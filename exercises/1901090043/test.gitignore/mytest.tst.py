import os
path = os.path.abspath('mytest.tst.py')
print(path)
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        RuntimeError, TypeError, NameError