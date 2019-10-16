#print nine nine multiplication table with for.
def f():
    for i in range(1,10):
        for j in range(1,i+1):
            k = i * j
            print(i,'*',j,'=',k,end='\t')
        print()

#print nine nine multiplication table with while.
def w():
    a = 1
    while a < 10:
        if a % 2 == 1:
            for b in range(1,a+1):
                m = a * b
                print(a,'*',b,'=',m,end='\t')
            print()
        a += 1

# Now call the function we just defined:
f()
print()
w()