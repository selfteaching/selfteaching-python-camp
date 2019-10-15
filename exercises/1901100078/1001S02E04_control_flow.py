def forin_multiply():
    for num in range(1,10):
        for i in range(1,num+1):
            print(f'{num} * {i} = {num*i}', end='\t')
        print('\n')
            
def while_multiply():
    limit = 10
    num = 1
    while num < limit:
        if num % 2 == 1:
            start = 1
            while start <= num:
                print(f'{num} * {start} = {num*start}', end = '\t')
                start += 1
            print('\n')
        num += 1


forin_multiply()
while_multiply()