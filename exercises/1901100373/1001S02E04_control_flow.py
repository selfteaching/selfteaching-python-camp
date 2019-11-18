for i in range(1, 10):
    for i_1 in range(1, i+1):
        if i_1 < i:
            print(i, '*', i_1, '=', i*i_1, sep='', end='\t')
        elif i_1 == i:
            print(i, '*', i_1, '=', i*i_1, sep='')
print('*'*40)
a = 0
while a < 9:
    a = a+1
    a_1 = 0
    while a_1 < a+1:
        a_1 = a_1+1
        if a % 2 == 0:
            continue
        if a_1 < a:
            print(a, '*', a_1, '=', a*a_1, sep='', end='\t')
        elif a_1 == a:
            print(a, '*', a_1, '=', a*a_1, sep='')
