# -*- coding: UTF-8 -*-
while True:
	Equation = input('>')
	try:
		print(eval(Equation))
	except:
		print("Unknow equation %s" % Equation)