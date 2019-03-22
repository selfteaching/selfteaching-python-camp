 # Filename : test.py
# author by : www.runoob.com
 
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()


    #use while
print("this is printing 9×9 multiplication table except even line using...... ")
x = 0                                              
while x < 9:                                        
    y=1                                             
    x=x+1                                           
    while y <= x:                                  
        if x % 2 != 0:                              
            if y < x:                               
                  print(x,'*',y,'=',x*y,end='\t')   
                  y = y+1                           
            else:
                print(x,'*',y,'=',x*y,end='\n')     
                y = y+1                             
        else:
            y=y+1                                  
