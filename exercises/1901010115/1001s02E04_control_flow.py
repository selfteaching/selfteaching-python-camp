print("1)for...in 循环乘法表")
print("\n")
for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%-4d"%(x,y,x*y),end="")
    print("\n")
    print("")
print("\n")
print("2)while 循环乘法表")
print("\n")
a = 1
while a < 10:
    x = a
    a += 2
    for y in range(1,x+1):
        print("%d*%d=%-4d"%(x,y,x*y),end="")
    print("\n")
    print("")
