def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('error:Invalid argument.')

print(int(spam(2)))
print(int(spam(12)))
print(spam(0))
print(spam(0.1))
print(spam(1))