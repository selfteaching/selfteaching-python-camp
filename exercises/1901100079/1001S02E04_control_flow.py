for a in range(1,10):
    for b in range(1,a+1):
        print(b,"*",a,"=",a*b,end="\t")
    print('')
print('''''')

i=1
while i<10:
    if i%2==0:
        print()
    else:
        for j in range(1,1+i):
            print('{}*{}={}'.format(j,i,i*j),end='\t')
    i+=1
print('''
''')

# 两种格式均可生成正确结果，但偶数行保留了
for a in range(1,10):
    for b in range(1,a+1):
        while a%2==0:
            break
        else:
            print(a,"*",b,"=",a*b,end="\t")
    print()
print('''
''')

for a in range(1,10):
    while a%2==0:
        break
    else:   
        for b in range(1,a+1):
            print(a,"*",b,"=",a*b,end="\t")
    print()
print()


