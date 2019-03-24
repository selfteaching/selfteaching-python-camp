#  支撑加减乘除功能的计计数器程序
#  第三天的作业
#  2019.3.22

# --------------
#  三大模块：输入模块、计算模块、输出模块
# 输入模块：采取人机交互方式，先输入选择功能，再输入两个数字
# 计算模块：根据选择功能，计算结果
# 输出模块：根据输入数据、打印计算结果


#  mode_calculators计算功能字典+,-,*,/,q,Q为退出
mode_calculators = [ '+', '-', '*', '/' ,'q','Q']

# 计算功能初始设置
mode_calculator = ''

# 功能输入提示
mode_input_prompt = "\nPlease select calculation mode( + - * / ) : "
mode_input_prompt  +=  "\nEnter ‘q’ to end the program。 "
#  数字1输入提示
number1_input_prompt = "\nPlease input_number 1 =  "
# 数字2输入提示
number2_input_prompt = "\nPlease input_number 2 =  "


# 大的计算功能循环
while True :

	# 输入计算模式
	while not(mode_calculator  in  mode_calculators):
		mode_calculator = input(mode_input_prompt)
     
    # q 退出计算器
	if (mode_calculator == 'q')  or  (mode_calculator == 'Q'):
		break
      
    # 数字1输入
	number1 = input(number1_input_prompt)
	while not( number1.isdigit() ) :
		number1 = input(number1_input_prompt)

    # 数字2输入
	number2 = input(number2_input_prompt) 
	while not( number2.isdigit() ) :
		number2 = input(number2_input_prompt)

	# 计算并打印结果
	if  (mode_calculator=='/') and ( int(number2)==0 ) :
		# 除数为0 非正常输出
		print( "\n error !  divisor =0 ")
	else:
		# +-*/正常输出	
		if mode_calculator=='+':
			outper_num = int(number1) + int(number2)
		if mode_calculator=='-':
			outper_num = int(number1) - int(number2)		
		if mode_calculator=='*':
			outper_num = int(number1) * int(number2)
		if mode_calculator=='/':
			outper_num = int(number1) / int(number2)	
		print(number1 + " " +  mode_calculator + " " +
			number2 + " = " + str(outper_num))
	#循环重新赋值计算模式
	mode_calculator = ''

