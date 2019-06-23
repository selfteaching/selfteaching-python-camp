#for in 循环
for num1 in range(1,10):
    for num2 in range(1,(num1+1)):
        if num2==num1:
            print('%s*%s=%s' %(num1,num2,num2*num1))
        else:
            print('%s*%s=%s' %(num1,num2,num2*num1), end='\t')

#while 循环
counter1 = 1
while counter1 <= 9:
    counter2 = 1
    if (counter1 %2)!=0:
        while counter2 <= counter1:
            if counter2==counter1:
                 print('%s*%s=%s' %(counter1,counter2,counter2*counter1))
            else:
                print('%s*%s=%s' %(counter1,counter2,counter2*counter1), end='\t')
            counter2 += 1
    counter1 += 1

