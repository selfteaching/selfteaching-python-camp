def add(x,y):
  return x + y
def subtract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  return x/y
print("welcome to use my calculator,pls select")
choice = input("your choice(1/2/3/4)")
numberA = int(input("your 1st number"))
numberB = int(input("your 2nd number"))

if choice == "1":
    print(add(numberA,numberB))
elif choice == "2":
    print(subtract(numberA,numberB))
elif choice == "3":
    print(multiply(numberA,numberB))
elif choice == "4":
    print (divide(numberA,numberB))
else:
    print("wrong choice")
