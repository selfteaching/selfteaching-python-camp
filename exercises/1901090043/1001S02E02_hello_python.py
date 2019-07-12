print("hello world!")

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)
    
print(f(5))