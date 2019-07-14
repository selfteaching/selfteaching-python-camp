
#1
number=[0,1,2,3,4,5,6,7,8,9]      
number_1=number[::-1]         
print('翻转列表-->',number_1)


#2
number_str=''.join([str(a) for a in number_1])
print('连接字符-->',number_str)

#3
cut=number_str[2:8]
print('切片-->',cut)

#4
cut_reversed=cut[::-1]
print('再次翻转-->',cut_reversed)

#5
int_cut=int(cut_reversed)
print('转为int类型-->',int_cut)

#6
print('二进制',bin(int_cut))
print('八进制',oct(int_cut))
print('十六进制',hex(int_cut))