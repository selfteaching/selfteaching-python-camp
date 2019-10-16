tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#翻转数组
list1 = list(tuple1)
list1.reverse()
tuple2 = tuple(list1)
#拼接字符串
string1 = ""
string1 = "".join([str(i) for i in list1])
#特定字符串切片
string2 = string1[2:8]
#翻转切片后的字符串
string3 = string2[::-1]
#字符串转换为整形
value1 = int(string3)
value2 = bin(value1)
value3 = oct(value1)
value4 = hex(value1)
print(value2, "  ", value3, "  ", value4)