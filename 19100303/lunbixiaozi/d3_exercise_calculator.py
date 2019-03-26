import operator
ops = { '+': operator.add, '-': operator.sub, '*' : operator.mul,  '/' : operator.truediv} 

print('Enter the first element: ')
first = int(input ())
print('Enter the operator: ')
operator = input ()
print('Enter the second element: ')
second = int(input ())
result = ops[operator](first,second)
print (result)



#print (ops[operator](3,5))
# result = operator.add(first,second)
# print (result)