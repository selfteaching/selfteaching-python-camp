for x in range(1, 10):
   
for y in range(1, x+1):
        
print('{}x{}={}'.format(x, y, x*y), end='\t')
   
print()

i = 1
while i<=9:
    j = 1
    while j<=i:
        print("{}*{}={:<2}".format(i,j,i * j),end = "\t")
        j += 1
    i += 1
if i/2!=0:        
    print("")