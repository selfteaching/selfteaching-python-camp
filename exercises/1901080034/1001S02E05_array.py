array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
array.reverse()
ls1=[str(i) for i in array]
print(ls1)
ls2=''.join(ls1)
print(ls2)
ls3=ls2[2:8]
print(ls3)
ls4=ls3[::-1]
print(ls4)
ls5=int(ls4)
print("转换为二进制为：", bin(ls5))
print("转换为八进制为：", oct(ls5))
print("转换为十六进制为：", hex(ls5))

