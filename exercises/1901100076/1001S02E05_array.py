list1=[0,1,2,3,4,5,6,7,8,9]
list1.reverse()
print("",list1)

#拼接成字符串
string="".join([str(num) for num in list1])#空白链接符，这样不会有间隔
print("",string)

#⽤用字符串串切⽚片的⽅方式取出第三到第⼋八个字符(包含第三和第⼋八个字符) [2]-[9

new_string=string[2:8]
print(new_string)

#将获得的字符串串进⾏行行翻转
print(new_string[::-1])#字符串切片翻转
#将结果转换为int类型
int_string=int(new_string[::-1])
print(int_string)
print(bin(int_string))#转化二进制
print(oct(int_string))
print(hex(int_string))

