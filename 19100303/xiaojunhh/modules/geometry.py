# 在 geometry 模组中定义集合运算功能
# 计算两点的距离
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)