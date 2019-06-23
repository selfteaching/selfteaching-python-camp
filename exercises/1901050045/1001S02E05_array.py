

number =[0,1,2,3,4,5,6,7,8,9]
number= sorted(number,reverse = True)
a = [str(i) for i in number]
#也可以这样写 a= [] ,for i in number: i = str(i), a.append(i)
b= ''.join(a) #将字符连接在一起
c=b[2:8]
d=c[::-1]#string reverse
d= int(d)# 整数化
binary = bin(d)
octonary= oct(d)
hexadecimal = hex(d)
print(binary,octonary,hexadecimal,sep='\n')

