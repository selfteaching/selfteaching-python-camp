gr=[0,1,2,3,4,5,6,7,8,9]
gr.reverse()
print(gr)

s = ''
for i in range(0,10):
    gr[i]=str(gr[i])
string=s.join(gr) #翻转后的数组拼接成字符串
print(string)

r1=string[2:9] #取出第三到第八个字符（包含第三和第八个字符）
print(r1)
number=int(r1[::-1])#将字符串进行反转,将结果转换为int类型
print(number)
print(bin(number))#转换成二进制并输出
print(oct(number))#转换成八进制并输出
print(hex(number))#转换成十六进制并输出
