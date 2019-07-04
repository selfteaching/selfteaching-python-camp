def multiplication_tables():
    for a in range(1, 10):
        for b in range(1, 10):
            print(a, '*', b, '=', a*b, end='\t')
            if a == b:
                print()
                break

def multiplication_tables_without_even():
    for a in range(1, 10):
        if a % 2 == 0:
            continue

        for b in range(1, 10):
            print(a, '*', b, '=', a*b, end='\t')
            if a == b:
                print()
                break

if __name__ == '__main__':
    print("Multiplication tables:")
    multiplication_tables()
    print("Multiplication tables without even:")
    multiplication_tables_without_even()