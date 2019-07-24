# 使用for…in循环打印九九乘法表
   # 行号linenum为"第一个变量"：被乘数
   # i为"第二个变量"：乘数
   # 第一个变量*第二个变量=乘积
for linenum in range(1,10):
   for i in range(1,10):
      if i<=linenum:
         print(linenum,"*",i,"=",linenum*i,end='\t')
      else:
         print()
         break



# 以三个空行作为与上题的分隔
print("""


""")



# 使用while循环打印九九乘法表并用条件判断把偶数行去除掉
   # 行号linenum_2为"第一个变量"：被乘数
   # i为"第二个变量"：乘数
   # 第一个变量*第二个变量=乘积
linenum_2=1
i=1
while linenum_2<10:
   if linenum_2%2!=0:
      while i<10:
         if i<=linenum_2:
            print(linenum_2,"*",i,"=",linenum_2*i,end='\t')
            i+=1
         else:
            print()
            i=1
            break
      linenum_2+=1
   else:
      linenum_2+=1