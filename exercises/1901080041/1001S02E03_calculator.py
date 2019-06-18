#calculation
def add(x,y): 
    return x+y
def subtract(x,y):
    return x-y
def mutiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("please input number 1")
a=int(input(""))
print("choose:+,-,*,/")
c=int(input(""))
print("please input number 2")
b=int(input(""))
if c=="+":
    print(add(a,b))
elif c=="-":
    print(subtract(a,b))
elif c=="*":
    print(mutiply(a,b))
elif c=="/":
    print(divide(a,b))
else:
    print("Error")
