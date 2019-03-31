# while True: 
#     try:
#         x = int(input('input int number'))
#         break
#     except ValueError:
#         print('Oops! That was no valid number, Try again...')

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass
# 3
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

import sys

try:
    f = open('README.md')
    s = f.readline()
    print(s)
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise