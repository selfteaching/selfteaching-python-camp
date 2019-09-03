print("Multiplication Table1: ")
for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='\t')
    print(end='\n')

print("Multiplication Table2: ")
x = -1
while x < 9:
    x = x + 2
    y = 1
    while y < x+1:
        print(x,'*',y,'=',x*y,end='\t') 
        y = y + 1           
    print(end='\n')