list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
revlist = sorted(list1, reverse=True)  #列表也可以叫数组
print('翻转数组',revlist)

joinedstr = ''.join(str(i)for i in revlist)  #''为空字符串
print('翻转并拼接为字符串',joinedstr)

slicedstr = joinedstr[2:8]
print('取出第三到八个字符', slicedstr)

revstr=slicedstr[::-1]
print('翻转切片后的字符串',revstr) 
# python 可以取负值，表示从末尾提取，最后一个为 -1，倒数第二个为 -2，即程序认为可以从结束处反向计数。
# str[:-1] 获取从偏移为0的字符一直到最后一个字符（不包括最后一个字符串）: "strin"
# str[:] 获取字符串从开始到结尾的所有元素 : "string"
# 负号表示反向计数，数字仅表示步长，与从哪里开始取无关？

intvalue = int(revstr)
print('转换为int类型',intvalue)  #写成print('转换为int类型',int(revstr))就不行

print('二进制:',bin(intvalue))
print('八进制:',oct(intvalue))
print('十六进制:',hex(intvalue))