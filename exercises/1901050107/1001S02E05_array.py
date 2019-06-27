text = [0,1,2,3,4,5,6,7,8,9]
#将数组[0,1,2,3,4,5,6,7,8,9]翻转
text.reverse()
# 翻转后的数组拼接成字符串串
str1 = ''.join(str(i) for i in text)
print(str1)
# 用字符串切片的方式取出第三到第八个字符
str2 = str1[2:8]
# 将获得的字符串串进⾏行行翻转
str2 = list(str2)
str2.reverse()
# 将结果转换为int类型
for index in range(len(str2)):
    str2[index]  = int(str2[index])
print (str2)    