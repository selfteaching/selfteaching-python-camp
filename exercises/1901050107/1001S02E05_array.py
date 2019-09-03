alist = [0,1,2,3,4,5,6,7,8,9]
# 第二步
print("将数组翻转：",alist.reverse())
alist = ''.join(str(i) for i in alist)
# 第三步
print("翻转后的数组拼接成字符串",alist) # join函数是把字符串中的字符一个一个连接进去的
# 第四步
alist = alist[2:8]
print("切片:",alist)
# 将获得的切片字符串翻转，可以有多重方法
#第五步： 将获得的字符串翻转
# 方法一
str1 = alist[::-1]
# 方法二
list(alist).reverse()
str1 = ''.join(str(i) for i in alist)
# print(str1)

# 方法三 
from functools import reduce
str2 = reduce(lambda x,y:y+x,alist)
# print(str2)

# 第六步：将结果转换为int类型
int_str = int(alist)
# 第七、八步
print('转换为 int 类型 ==>', int_str)
print('转换为 二进制==>', bin(int_str))
print('转换为 八进制==>', oct(int_str))
print('转换为 十六进制==>', hex(int_str))