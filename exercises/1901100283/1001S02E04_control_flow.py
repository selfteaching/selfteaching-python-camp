#Task1: for...in方法
for a in range(1,10):
    for b in range(1, a + 1):
        print("{}*{}={}".format(a, b ,a * b), end="\t")
    print()

#Task 2: while方法+条件判断
a = 1
while a <= 9:
    if a % 2 == 1:
        b = 1
        while b <= a:
            print("{}*{}={}".format(a, b ,a * b), end="\t")
            b = b + 1
        print()
    a= a + 1


#Task 2: while方法+另一解决方案
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print("{}*{}={}".format(a, b ,a * b), end="\t")
        b = b + 1
    print()
    a= a + 2


