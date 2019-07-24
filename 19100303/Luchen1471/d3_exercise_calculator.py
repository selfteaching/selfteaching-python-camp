# Fibonacci series:
#a, b = 0, 1
#print('\nThe fibonacci series is:')
#while a<100:
#    print(a, end=" ")
#   a, b=b, a+b
#print('...\n')

print('\nHello! I\'d like to help you to do the math homework. Feel free to try me!') 
x=float(input("Please tell me a float number here:"))
#A=input("please tell me what kind of operation you want:")
y=float(input("Please tell me another float number here:"))
print('\nTa-daaa! The resaults are:')
#print('x+y=',round(x+y,2))
#print('x-y=',round(x-y,2))
#print('x*y=',round(x*y,2))
#print('x/y=',round(x/y,2))
li = [x+y,x-y,x*y,x/y]
i = 0
for op in ["+", "-", "*", "/"]:
  print('x{}y'.format(op),'=',li[i] )
  i += 1
print('\n')
