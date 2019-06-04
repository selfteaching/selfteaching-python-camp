def array_to_str(array):
    array_str = ['']*len(array) 
    for i in range(len(array)): 
        array_str[i] = str(array[i])
    s = ''
    return s.join(array_str) 

def str_reverse(string):
    array_list=['']*len(string) 
    for i in range(len(string)): 
        array_list[i]=string[i]
    array_list.reverse() 
    s=''
    return s.join(array_list) 

array = [0,1,2,3,4,5,6,7,8,9]
array.reverse() 
array_str = array_to_str(array)
array_str = array_str[2:8] 
array_str = str_reverse(array_str) 
array_int = int(array_str) 
print('二进制数为：',bin(array_int))
print('八进制数为：',oct(array_int))
print('十六进制数为：',hex(array_int))