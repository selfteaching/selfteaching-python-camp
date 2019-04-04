#乘法表规律：第n行应该是n*1 n*2 n*3  ... n*(n-1) n*n
#定义i和j2个数，i为1~9,j为1~i，循环打印i*j
print('打印完整乘法表')
for i in range(1,10):  #i从1至9，注意不包括10
    for j in range(1,i):#j从1至i-1
      print(i,"*",j,"=",i*j,end='\t') #不换行打印
    print(i,"*",i,"=",i*i)      #最后一个换行打印

# 使用while判断，当i为奇数时才打印输出，打印完了需要break一下，不然无法进入下一个循环
# 用i除以2余数为1表示为奇数
print('不打印偶数行')
for i in range(1,10):
   while i%2==1:
      for j in range(1,i):
        print(i,"*",j,"=",i*j,end='\t')
      print(i,"*",i,"=",i*i)
      break

      
   
