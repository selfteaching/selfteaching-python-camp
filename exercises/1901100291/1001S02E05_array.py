print("2.将数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 翻转")
'''
def Reverse(lst): 
    return [ele for ele in reversed(lst)]  
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Reverselsts=print(Reverse(lst)) 
'''
lst=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[::-1]  #此处为字符串反转
reversed_list=lst[::-1]
print(reversed_list)

print("3.翻转后的数组拼接成字符串")
reverselsts_str=''.join([str(i) for i in reversed_list])
print(reverselsts_str)

print("4.将字符串切片式取出第三到第八个字符")
lstte=reverselsts_str[2:8]
print(lstte)

print("5.将结果转换为 int 类型")
reverselsts_int=int(lstte)
print(reverselsts_int)

print("转换成二进制")
print(bin(reverselsts_int))

print("转换成八进制")
print(oct(reverselsts_int))

print("转换成十六进制")
print(hex(reverselsts_int))
