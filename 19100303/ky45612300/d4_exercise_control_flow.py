print()
x = 1
while x < 10:
    if x % 2 == 1:
        y = 1
        while y <= x:
           print(x,'*',y,'=',x*y,end='   ')
           if x == y: #条件换行
                print() 
           y += 1
    x += 1
print()