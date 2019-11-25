print()
print("1. 使用for…in循环打印九九乘法表，输出")

print()
for i in range(1,10):
    for j in range (1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print()
  
  
print()

print("2. 使用fwhile循环打印九九乘法表并用条件判断把偶数行删除，输出")
print() 
i=1
while i<10:
    if i%2==1:
        j=1
        while j<=i:
          print('%d * %d = %-2d'%(i,j,i*j),end='\t')      
        j=j+1
        print()
    i=i+1    

