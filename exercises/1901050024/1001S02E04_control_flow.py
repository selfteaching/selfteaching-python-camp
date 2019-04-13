print("multiplication table1(for statements type)")
for x in range(1,10):
    for y in range(1,x+1):
        z = x * y
        print(x,'*',y,'=',z,'',end='\t')
    print(end='\n')


print("multiplication table2((for statements type)")
for x in range(1,10,2):
    for y in range(1,x+1):
        z = x * y
        print(x,'*',y,'=',z,'',end='\t')
    print(end='\n')

print("multiplication table1(while statements type)")
x = 1
while x < 10:
    y = 1
    while y <= x:
        print(x,'*',y,'=',x*y,end='\t')
        y += 1
    print(end='\n')    
    x += 1

print('multiplication table2(while statements type)')
x = -1
while x < 9:
    x = x + 2
    y = 1
    while y <= x:
        print(x,'*',y,'=',x*y,end=';')
        y += 1
    print(end='\n')
