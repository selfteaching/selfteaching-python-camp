# This is d3_exercise_calculator.py
import string

# this is def of add, sub, mul, div, pow
def add(a,b):
	return a + b
def sub(a,b):
	return a - b
def mul(a,b):
	return a * b
def div(a,b):
	if b == 0:
		return "Dividend can't be zero. Please input again."
	else:
		return a / b
def pow(a,b):
	return a ** b


# this is seperate of input string.
def string_sep(input_str):
	if "+" in input_str:
		a = int(input_str.split("+")[0])
		b = int(input_str.split("+")[1])
		return add(a,b)
	if "-" in input_str:
		a = int(input_str.split("-")[0])
		b = int(input_str.split("-")[1])
		return sub(a,b)
	if "*" in input_str:
		a = int(input_str.split("*")[0])
		b = int(input_str.split("*")[1])
		return mul(a,b)
	if "/" in input_str:
		a = int(input_str.split("/")[0])
		b = int(input_str.split("/")[1])
		return div(a,b)
	if "^" in input_str:
		a = int(input_str.split("^")[0])
		b = int(input_str.split("^")[1])
		return pow(a,b)
	else:
		return "Please check the input."


input_str = input("Please input the calutor: ")

print(string_sep(input_str))

