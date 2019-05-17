# Filename : 1001S02E04_control_flow
# author by : 张金磊

for i in range(1,10):
    # print(i,end = ' ')
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end = '\t')
    print("")
    
print('\n')
print('-'*26+'神奇的分割线'+'-'*26)
print('\n')

###########################################################
i = 1
while i<=9:
    j = 1
    while j<=i:
        print("{}*{}={}".format(i,j,i * j),end = '\t')
        j += 1
    i += 2
    print("")

###########################################################
"""一句话打印出九九乘法表。注意，两个乘数后边的是不变的那个。
"""
###########################################################
print('\n')
print('-'*26+'神奇的分割线'+'-'*26)
print('\n')

print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
