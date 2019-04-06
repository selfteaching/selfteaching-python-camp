list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
list1.reverse()#翻转数组
#print(list1)

list2=[]
for i in list1:
        i =str(i)
        list2.append(i)
#print(list2)

str1=''
str1=str1.join(list2)
#print(str1)       
str2 = str1[2:8]   #用字符串切片的方式，取出第三到第八个字符,这里有一个bug.
print(str2)
list3=list(str2)
#print(list3)
list3 = list3.reverse   #将列表进行反转
print(list3)
str3 = str(list3)
str3=int(str2)
print(str3)
