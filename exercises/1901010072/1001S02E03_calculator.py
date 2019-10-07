
# 实现一个简单的计算器
# 1 接收用户输入的第一个数字(字符串类型)，并转化为整数类型int
  first_num = input('请输入第一个数字:')
  first_num = int(first_num)
# 2 接收用户输入的运算符
  symbol = input('请输入运算符（+,-,*,/):')
# 3 接收用户输入的第二个数字(字符串类型)，并转化为整数类型int
  sec_num = input('请输入第二个数字:')
  sec_num = int(sec_num)
# 4 代码进行判断，计算
  if symbol == '+':
    result = first_num + sec_num
    print(f'{first_num}{symbol}{sec_num}={result}')
  
  elif symbol == '-':
    result = first_num - sec_num
    print(f'{first_num}{symbol}{sec_num}={result}')
  
  elif symbol == '*':
    result = first_num * sec_num
    print(f'{first_num}{symbol}{sec_num}={result}')
  
  elif symbol == '/':
    if sec_num == 0：
       result = '除数不能为0'
       print(result)
    else:
       result = first_num / sec_num
       print(f'{first_num}{symbol}{sec_num}={result}')
  
  else:
      result = '输入错误'
      print(result)
  
# 5 显示计算的结果，以及完整的等式
# 格式化输出 format
  # print(result)
  print(f'{first_num}{symbol}{sec_num}={result}')

