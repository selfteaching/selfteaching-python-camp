list_a=[0,1,2,3,4,5,6,7,8,9]
list_a.sort(reverse=True)  # Ture的第一个字母要大写！
print(list_a)

str_a="".join(str(i)for i in list_a)
print(str_a)  #用join方法的话，里面的参数你需要保证所有元素都是string的list

str_b=str_a[2:8]  #  slicing切片
print(str_b)
                  #str不能使用.sort()
                  #str是有序不可变类型，所以也不能用.sorted()
str_c=str_b[::-1] #其中第一个: 表示的是切片的区间，如果没有设定数值，默认是全部区间；
                  #第二个：表示的是切片的步数和方向，默认为切片方向为从前向后，默认步数为1.上面的-1，代表的就是从后向前，一次往前切一次，也就是刚好倒置列表。
print(str_c)

str_d=int(str_c)
print((str_d))

print(bin(str_d))  #转换为2进制
print(oct(str_d))  #转换为8进制
print(hex(str_d))  #转换为16进制
