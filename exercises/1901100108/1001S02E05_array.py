
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#方法1
alist=sorted(array, reverse=True) 
print(alist)
#方法2，注意reversed返回的是一个迭代器
blist = list(reversed(array))
print (blist)
#方法3
clist=array[::-1] 
print(clist)

#完成拼接，首先要完成字符串格式的转换
array_str = ''.join([str(i) for i in clist])
print(array_str)

slice_str = array_str[2:8]
print(array_str[2:8]) #试试有什么表达式或方法不能print吗

reslice = slice_str[::-1]
print('这是字符串', reslice)
inslice = int(reslice)
print('转化为int', inslice)

print('转化为二进制', bin(inslice))
print('转化为八进制', oct(inslice))
print('转化为十六进制', hex(inslice))
