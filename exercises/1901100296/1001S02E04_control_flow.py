'''
九九乘法表
'''

print("九九乘法表:")

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end='\t')
    print()
    i+=1

'''
九九乘法表，将偶数行去掉
'''
print("删除偶数行的九九乘法表:")
i=1
while i<10:
    for j in range(1,i+1):
        if i%2!=0:
            print(i,"*",j,"=",i*j,end='\t') 
    if i%2!=0:
        print() 
    i=i+1


