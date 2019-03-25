

#把数组翻转
array=[0,1,2,3,4,5,6,7,8,9]
array.reverse()
print(array)

#把翻转后字符拼接成字符串
s=''
t=['9','8','7','6','5','4','3','2','1','0']
array=s.join(t)
print(array)

#取出第三到第八个字符

s1=array[2:8]
print(s1)

#将字符串进行反转，并转换为int类型
fz=int(s1[::-1])  
print(fz)

#转换成二进制、八进制、十六进制
print(bin(fz),oct(fz),hex(fz)) 