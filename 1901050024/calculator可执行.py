print("Easy Calculator")
number_1 = float(input('请输入数字：'))
formula = input('请输入公式+、-、*、/：')
number_2 = float(input('请输入数字：'))
if formula == str('+'):
    print(number_1+number_2)
elif formula == str('-'):
    print(number_1-number_2)
elif formula == str('*'):
    print(number_1*number_2)
elif formula == str('/'):
    print(number_1/number_2)
else: 
    print("please enter 1the right formula")
print("Thank you") 
