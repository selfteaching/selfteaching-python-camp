
print()            
print('----------------------------------------------')
print('-                    for                     -')
print('----------------------------------------------')
for i in range(0,10):
    print()
    for j in range(1,i+1):
        result = int(i)*int(j)
        print(i,'*',j,'=',result,end='\t')
print()            
print('----------------------------------------------')
print('-                   while                    -')
print('----------------------------------------------')
i = 0
j = 1
while (i < 9):
    i += 1
    if i%2 == 0:
         continue
    print()
    j = 1
    while (j <= i):
        result = int(i)*int(j)
        print(i,'*',j,'=',result,end='\t')
        j += 1
             