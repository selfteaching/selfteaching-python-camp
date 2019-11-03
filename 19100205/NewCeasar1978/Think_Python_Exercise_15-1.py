class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y


class Circle:
    def __init__(self,center,radius):
        self.center = Point()
        self.radius = radius

class Rectangle:
    def __init__(self,width,height,corner):
        self.width = width
        self.height = height
        self.corner = Point()



c = Circle(Point,75)
c.center = Point(150,100)
p = Point(76,100)
r = Rectangle(53,53,Point)
r.corner = Point(150,100)
import math
def point_in_circle(c,p):
    distance = math.sqrt((p.x - c.center.x)**2 + (p.y - c.center.y)**2)
    return distance <= c.radius

def rect_in_circle(c,r):
    r1 = r.corner
    r2 = Point(r.corner.x + r.width,r.corner.y)
    r3 = Point(r.corner.x + r.width,r.corner.y + r.height)
    r4 = Point(r.corner.x,r.corner.y + r.height)
    return point_in_circle(c,r1) and point_in_circle(c,r2) and point_in_circle(c,r3) and point_in_circle(c,r4)


#print(point_in_circle(c,p))
print(rect_in_circle(c,r))

#print(type(c),c.center.x,c.center.y,c.radius)