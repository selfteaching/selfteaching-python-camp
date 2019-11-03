class Point:
    '''
    点的类，其中
    x：横坐标；
    y：纵坐标
    '''
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y


class Circle:
    '''
    圆的类，其中
    center：圆心，为一个 Point 类；
    radius：半径
    '''
    def __init__(self,center,radius):
        self.center = Point()
        self.radius = radius

class Rectangle:
    '''矩形的类，其中
    width：矩形的宽；
    heigh：矩形的高；
    corner：矩形左下角的顶点，为一个 Point 类
    '''
    def __init__(self,width,height,corner):
        self.width = width
        self.height = height
        self.corner = Point()

def draw_rect(t,r):
    '''
    利用 turtle 绘制一个矩形
    t：turtle 对象；
    r：Rectangle 对象。
    '''
    t.pu()
    t.fd(r.corner.x)
    t.lt(90)
    t.fd(r.corner.y)
    t.pd()
    t.fd(r.height)
    t.rt(90)
    t.fd(r.width)
    t.rt(90)
    t.fd(r.height)
    t.rt(90)
    t.fd(r.width)

def draw_circle(t,c):
    '''
    利用 turtle 绘制一个圆形
    t：turtle 对象；
    c：Circle 对象。
    '''
    t.pu()
    t.fd(c.center.x)
    t.lt(90)
    t.fd(c.center.y)
    t.pd()
    circle(t,c.radius)

import turtle
from mymodule.Think_Python_modules import circle


t1 = turtle.Turtle()
#r1 = Rectangle(150,100,Point)
#r1.corner = Point(-100,100)
corner = Point(-100,100)
r1 = Rectangle(150,100,corner)


draw_rect(t1,r1)
turtle.mainloop()

'''
t1 = turtle.Turtle()
center = Point(-100,100)
c1 = Circle(center,100)

draw_circle(t1,c1)
turtle.mainloop()
'''

