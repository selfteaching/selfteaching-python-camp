""" def ji_suan(a,b,fu_hao) :
    result = 0 
"""  # 定义函数的方式 一直出错 还要继续学习

a,b,fu_hao,result = 0,0,0,0  # 定义几个变量
print("""
hello ,这是一个极简计算器,
只能两个数的:加 减 乘 除 哟!
""")   #这里用三个引号 进行强制换行
a = float(input("请 输入第一个数字 :"))
fu_hao = input("请 输入运算符号 :")
b = float(input("请 输入第二个数字 :"))

if fu_hao == "+" :
    result = a + b

if fu_hao == "-" :
    result = a - b

if fu_hao == "*" :
    result = a * b

if fu_hao == "/" :
    result = a / b

print(result) 
