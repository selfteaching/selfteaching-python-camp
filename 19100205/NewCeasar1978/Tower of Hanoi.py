import turtle
class Pole():
    def __init__(self, location):
        self.location = location
        self.disks_list = []        
        self.shaft = turtle.Turtle()
        self.shaft.up()
        self.shaft.goto(self.location, -100)
        self.shaft.pensize(5)
        self.shaft.lt(90)
        self.shaft.down()
        self.shaft.fd(300)
        self.shaft.bk(300)

    def initial_disks(self, num_disks):
        color_list = ['red','orange','yellow','green','cyan','blue','purple']
        for i in range(num_disks, 0 , -1):
            name = 'd' + str(i)
            locals()[name] = Disk(i, color_list[i % num_disks])
            self.add_disk(locals()[name])
            locals()[name].t.goto(self.location,-i*25 + num_disks*25 - 100)
    def add_disk(self, disk):
        self.disks_list.append(disk)
    def remove_disk(self):
        self.disks_list.pop()

class Disk():
    def __init__(self,size, color = 'blue'):
        self.size = size
        self.t = turtle.Turtle()
        self.t.up()
        self.t.speed(4)
        self.t.shape('square')
        self.t.color(color)
        self.t.shapesize(1, self.size)
    def move_disk(self, ori_pole, des_pole):
        ori_pole.remove_disk()
        des_pole.add_disk(self)
        self.t.goto(ori_pole.location, 230)
        self.t.goto(des_pole.location, 230)
        self.t.goto  (des_pole.location, len(des_pole.disks_list)*25 - 125) 

def tower_of_hanoi(n, ori_pole, des_pole, with_pole): 

    if n == 1:
        ori_pole.disks_list[-1].move_disk(ori_pole, des_pole)
    else:
        tower_of_hanoi(n - 1, ori_pole, with_pole, des_pole)
        ori_pole.disks_list[-1].move_disk(ori_pole, des_pole)
        tower_of_hanoi(n - 1, with_pole, des_pole, ori_pole)

n = 5
pa = Pole(-200)
pb = Pole(0)
pc = Pole(200)
pa.initial_disks(n)
tower_of_hanoi(n, pa, pc, pb)
m = turtle.Screen()
m.exitonclick()









    