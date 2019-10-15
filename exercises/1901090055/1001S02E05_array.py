list = [0,1,2,3,4,5,6,7,8,9]

#翻转数组
list1 = list[::-1]
print(list1)

#取出第三个到第八个
list2 = list1[2:8]
print(list2)

#再翻转

list3 = list2[::-1]
print(list3)

#转换为int类型
for i in list3:
    list4 = int(i)
    print(list4)

#转换成二进制
for i in list3:
    list4 = int(i)
    print(bin(list4))

#转换成八进制
for i in list3:
    list4 = int(i)
    print(oct(list4))

#转换成十六进制
for i in list3:
    list4 = int(i)
    print(hex(list4))