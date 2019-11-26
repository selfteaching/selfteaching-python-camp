#计算器支持加减乘除
	operator= input("pls input character (+,-,*,/):")#()内内容为提示内容
	first_number=input("first_number:")
	second_number=input("second_number:")
	
	a=float(firs_tnumber)
	b=float(second_number)
	
	print("operator:",operator,type(operator))
	print("first_number:",first_number,type(first_number),type(a))
	print("second_number:",second_number,type(second_number),type(b))
	
	if operator=="+":
	    print(a,"+",b,"=",a+b)
	elif operator=="-":
	    print(a,"-",b,"=",a-b)
	elif operator=="*":
	    print(a,"*",b,"=",a*b)
	elif operator=="/":
	    print(a,"/",b,"=",a/b)
	else:
	    print("not found")