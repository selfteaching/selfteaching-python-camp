x = input('please input a number x:')
y = input('please input a number y:')
op = input('please input an operator + - * /:')

if op == '+' : 
    print(float(x)+float(y))
elif op == '-':
    print(float(x)-float(y))
elif op == '*':
    print(float(x)*float(y))
else: #op == '\/'
    print(float(x)/float(y))

'''
几点练习感受和想法

1、数据输入与类型转换
接收输入，用的是input函数。
做+运算时，会发现x、y被当做字符串处理。所以上面用了float类型转换。

2、问题：除号字符常量 / 如何表达?  '/'会报错。 

3、条件控制语句  if  elif  else

4、calculator如何改进？
   比如，完整接收表达式输入  123 + 456 ，然后可以直接输出结果，而不需要上面输入提示。

5、calculator如何进一步改进？
   支持运算符优先级，比如  1 + (2-3)*4 + 5/2

6、其他
    1）多行注释 用3个引号
    2）作业先做到这个程度，先提交，再改进，想到 done is better than perfect.
    3）新学Python语言时，总会和已熟练的C语言做对比，比如变量类型、输入输出、控制结构...
    4）这篇参考资料挺好的：Learn X in Y minutes，Where X=python3
    5）python似乎只能用UTF-8存储，windows上，gb2312存储文件，运行会报错，报错信息：
    SyntaxError: (unicode error) 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte

练习时长：大概1个半小时。练习量不多，先这样，再慢慢加量。
2019年7月5日 早晨 5：38
'''
    