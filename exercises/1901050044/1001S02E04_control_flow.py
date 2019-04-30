def multiply(x,y):
        return x * y
a = 1
while a < 10:
        for b in range (1, a+1):
                print(a,"*",b,'=',multiply(a,b),end='\t')
        a = a + 1
        print()

