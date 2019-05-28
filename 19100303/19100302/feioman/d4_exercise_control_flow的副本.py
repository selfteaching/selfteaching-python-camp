#任务１for语句
print("---"* 20)
print('<feioman乘法表1>')
for i in range(1,10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i ,x ,i*x) ,end = '  ' )
    print('  ')
#
print("---"* 20)
#

#任务2.1 while语句
print('《feioman乘法表2》')

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print('%d X %d = %2d' %(i ,j ,i*j) ,end = '  ')
        j += 1
    i += 1
    print(' ')


print("---"* 20)

#任务2.2 while语句　去偶１
print('*feioman乘法表3*')

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print('%d X %d = %2d' %(i ,j ,i*j) ,end = '  ')
        j += 1
    i += 2
    print(' ')

print("---"* 20)

#任务2.３ while语句　去偶２
print('*feioman乘法表４*')

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print('%d X %d = %2d' %(i ,j ,i*j) ,end = '  ')
        j += 1
    if (i % 2) == 1:
        i += 2
    print(' ')
    
print("---"* 20)
