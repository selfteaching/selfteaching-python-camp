# Filename : 1001S02E04_control_flow
# author by : �Ž���

for i in range(1,10):
    # print(i,end = ' ')
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end = '\t')
    print("")
    
print('\n')
print('-'*26+'����ķָ���'+'-'*26)
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
"""һ�仰��ӡ���žų˷���ע�⣬����������ߵ��ǲ�����Ǹ���
"""
###########################################################
print('\n')
print('-'*26+'����ķָ���'+'-'*26)
print('\n')

print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
