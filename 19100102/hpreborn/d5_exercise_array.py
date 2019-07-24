#将数组[0,1,2,3,4,5,6,7,8,9]翻转
arr=[0,1,2,3,4,5,6,7,8,9]
arrTemp=[]
for i in range(0,len(arr)):
    arrTemp.append(arr[len(arr)-i-1])

#翻转后的数组拼接成字符串
arrTemp=map(str,arrTemp)
strTemp=""
strTemp=strTemp.join(arrTemp)

#用字符串切片方式去取第三个到第八个字符（包含第三和第八个字符）
strTemp=strTemp[2:8]

#将获得的字符串进行翻转
strTemp=strTemp[::-1]

#将结果转换为int类型
intTemp=0
intTemp=int(strTemp)

#分别转换成二进制，八进制，十六进制
intBin=0
intOct=0
intHex=0
intBin=bin(intTemp)
intOct=oct(intTemp)
intHex=hex(intHex)

#最后输出三种进制的结果
print(intTemp)
print(intBin)
print(intTemp)
print(intHex)