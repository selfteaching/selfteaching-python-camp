print('尝试编写一个支持加、减、乘、除功能的计算器')

def add(x, y, c):    
    a = x * y      
    b = y / c        
    e = (a + b)/c
    return e

# 在运算的时候，给与X, Y, C不同的数值，就可以计算出e的结果。