shuzu = [0,1,2,3,4,5,6,7,8,9]
shuzu.reverse()
print(shuzu)

s = '' #翻转后的数组拼接成字符串方法一
for i in range(0,10):
    shuzu[i]=str(shuzu[i])
zifucuan=s.join(shuzu)
print(zifucuan)

r1=zifucuan[2:8] #用切片方式取出第三到第八个字符
print(r1)

zhengshu=int(r1[::-1]) #将字符串进行反转，并转换为int类型
print(zhengshu)
print(bin(zhengshu),oct(zhengshu),hex(zhengshu))  #转换成二进制，八进制，十六进制 