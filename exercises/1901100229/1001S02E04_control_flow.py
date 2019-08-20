print("1. 使用for…in循环打印九九乘法表，输出")
for a in range(1,10):
   for b in range(1,a+1):
      print(a,'*',b,'=',a*b, end='\t')
   print()

print()
print("2. 使用while循环打印九九乘法表并用条件判断把偶数行删除，输出")
for a in range(1,10):
   for b in range(1,a+1):
      while a % 2 == 0:
         break
      else:
         print(a,'*',b,'=',a*b, end='\t')
   print()