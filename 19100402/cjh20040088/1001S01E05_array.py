list=[0,1,2,3,4,5,6,7,8,9]

list.reverse()
print(list)

list1="".join('%s'%id for id in list)
print(list1)

list2=list1[2:8]
print(list2)

list3=list2[::-1]
print(list3)

list4=int(list3)
print(list4)

print('二进制：'+bin(list4)+'\n八进制：'+oct(list4)+'\n十六进制：'+hex(list4))




