print('九九乘法表For+for')
for a in range(1,10):
    for b in range(1,a+1):
        print('{}*{}={}\t'.format(a, b, a*b), end='')
        b=b+1
    print('')
print('')
#分割线
print('九九乘法表For+while')
for a in range(1,10):
    b=1
    while a>=b:
        print('{}*{}={}\t'.format(a, b, a*b), end='')
        b=b+1
    print('')
print('')
#分割线
print('九九乘法表While+while')
a=1
while a<10:
    b=1
    while a>=b:
        print('{}*{}={}\t'.format(a, b, a*b), end='')
        b=b+1
    a=a+1
    print('')
print('')
#分割线
print('九九乘法表去偶数While+if')
a=1
while a<10:
    b=1
    c=a%2
    if c==1:
        while a>=b:
            print('{}*{}={}\t'.format(a, b, a*b), end='')
            b=b+1
        print('')
    a=a+1
print('')
#分割线
print('九九乘法表去偶数For+while')
for a in range(1,10,2):
    b=1
    while a>=b:
        print('{}*{}={}\t'.format(a, b, a*b), end='')
        b=b+1
    print('')
print('')
#分割线
print('九九乘法表去偶数for+if')
for a in range(1,10):
    b=1
    c=a%2
    if c==1:
        while a>=b:
            print('{}*{}={}\t'.format(a, b, a*b), end='')
            b=b+1
        print('')
print('')
#分割线
print('九九乘法表去偶数while+while')
a=1
while a<10:
    b=1
    while a>=b:
        print('{}*{}={}\t'.format(a, b, a*b), end='')
        b=b+1
    a=a+2
    print('')

