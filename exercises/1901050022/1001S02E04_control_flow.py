# Filename : 1001S02E04_control_flow.py
# author by : kidswonder

#九九乘数表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'. format(j, i, i*j), end='')
    print()

#九九乘数表去除偶数行
i = 0
while i < 9:
    j = 1
    i += 1
    while j <= i:
        if i % 2 != 0:
            if j < i:
                print(j, '*', i,'=',i*j, end='\t')
                j += 1
            else:
                print(j, '*', i,'=',i*j, end='\n')
                j += 1
        else:            
            j += 1