"""
for  a in range (1,10):
    #print("第%d行"%a,end="\t")
     for i in range(1,a+1):
      print (a,'*',i,'=',a*i, end="\t")#end 表示用tab 结尾
     print()#表示换行的功能
"""

""" 
V1 之前出错尝试 cause：没有嵌套循环无法，继续执行  
a=1
for i in range(1,a+1):
  print (a,'*',i,'=',a*i, end="\t") 
  a=a+1
  if a%2==0:
    a=a+1
    if a==10:
        break

        """

a=1
while (a<10):
 for i in range(1,a+1):
    print (a,'*',i,'=',a*i, end="\t") 
    
 a=a+1
 if a%2==0:
    a=a+1
    print()


 