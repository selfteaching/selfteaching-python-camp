# -*- coding: UTF-8 -*-
symbol = ('+', '-', '*', '/', '(', ')', '1', '2', '3', 
	'4', '5', '6', '7', '8', '9', '0')
calc = True
while True:
	Equation = input('>')
	tester = list(Equation)
	for i in tester:
		if i not in symbol and calc:
			print("Unknow symbol %s" % i)
			calc = False
	if calc:
		try:
			print(eval(Equation))
		except:
			print("Unknow equation %s" % Equation)