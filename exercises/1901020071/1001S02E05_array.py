arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

#翻转数组
arr.reverse()
print(arr)

#把列表拼接为字符串
str1=''
for ss in arr:
    str1+=str(ss)

print(str1)

#切片去除第三个到第八个字符
str2=str1[2:8]
print(str2)

#将获得的字符串进行翻转
str3=''
i=0
while i <len(str2):
    str3+=str2[len(str2)-i-1]
    i+=1
print(str3)   

#将str3转换为int类型
num1=int(str3)
print(num1)

#将num1转换为二进制，八进制，十六进制
binaryNum=bin(num1)
print(binaryNum)

octNum=oct(num1)
print(octNum)

hexNum=hex(num1)
print(hexNum)


