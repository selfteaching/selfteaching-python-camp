#创建一个包含0 ~ 9的数组
m_list = list(range(0,10))

#将数组翻转
m_list.reverse()  # reverse()只对当前序列操作，并不返回一个逆序列表；返回值是 None
print(m_list)

#将翻转后的数组拼接成字符串
m_list_str = [str(i) for i in m_list]
m = ''.join(m_list_str)
print(m)

#用字符串切片的方式取出第三到第八个字符
n = m[2:8]
print(n)

#将获得的字符串进行翻转
n1 = n[::-1]
print(n1)

#将结果转换为int型
n2 = int(n1)
print(n2,type(n2))

#分别转换成二进制、八进制、十六进制，并输出结果
print('二进制结果：',bin(n2))
print('八进制结果：',oct(n2))
print('十六进制结果：',hex(n2))
