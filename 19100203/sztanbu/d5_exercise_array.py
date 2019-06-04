

#翻转数组
array = [0,1,2,3,4,5,6,7,8,9]
array.reverse()

#数组转为字符串
def array_to_str(array):
    array_str = ['']*len(array) 
    for index in range(len(array)): 
        array_str[index] = str(array[index])
    s = ''
    return s.join(array_str) 

#字符串翻转
def str_reverse(string):
    array_list=['']*len(string) 
    for i in range(len(string)): 
        array_list[i]=string[i]
    array_list.reverse() #翻转字符串列表
    s=''
    return s.join(array_list) #合并为一个字符串


array_int=int(array_to_str(array))
print('二进制数为：',bin(array_int))
print('八进制数为：',oct(array_int))
print('十六进制数为：',hex(array_int))