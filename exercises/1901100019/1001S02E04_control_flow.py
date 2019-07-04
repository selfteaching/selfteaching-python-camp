def multiplication_tables():
    for a in range(1, 10):
        for b in range(1, 10):
            print(a, '*', b, '=', a*b, end='\t')
            if a == b:
                print()
                break

def multiplication_tables_without_even():
    a = 1
    while a < 10:
        if a % 2 != 0:
            b = 1
            while b < 10:
                print(a, '*', b, '=', a*b, end='\t')
                if a == b:
                    print()
                    break
                b += 1
        a += 1

if __name__ == '__main__':
    print("Multiplication tables:")
    multiplication_tables()
    print("Multiplication tables without even:")
    multiplication_tables_without_even()