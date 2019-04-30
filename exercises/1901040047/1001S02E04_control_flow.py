print('《九九乘法表》')
for i in range(1,10):
    for j in range(1,i+1):
       
        print(j,"*",i,"=",i*j,end='\t')
        
    print('')




print("\n《九九乘法表-奇数行》")
for x in range(1, 10):
	    for y in range(1, x+1):
	        while x % 2 != 0:
	            print(y, 'x', x, '=', x*y, end='\t')
	            if x == y:
	                print()
	            break
