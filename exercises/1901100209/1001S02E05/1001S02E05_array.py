text=[0,1,3,4,5,6,7,8,9]
text.reverse()
print("数字反转",text)

joined_str="".join([str(i) for i in text])
print("拼接成字符串",joined_str)

slice_ed=joined_str[2:8]
print("切片",slice_ed)

reverse_str=slice_ed[::-1]
print("反转",reverse_str)
slice_int=int(reverse_str)
print("转换为int类型",slice_int)
print("转换为二进制",bin(slice_int))
print("转换为八进制",oct(slice_int))
print("转换为十六进制",hex(slice_int))
