import turtle
class Pole():
    def __init__(self, location):
        self.location = location
        self.disks_list = []        
        self.shaft = turtle.Turtle()
        self.shaft.up()
        self.shaft.goto(self.location, -100)
        self.shaft.lt(90)
        self.shaft.down()
        self.shaft.fd(500)
        self.shaft.bk(500)

    def initial_disks(self, num_disks):
        for i in range(num_disks, 0 , -1):
            name = 'd' + str(i)
            locals()[name] = Disk(i)
            self.add_disk(locals()[name])
            locals()[name].t.goto(self.location,-i*25 + num_disks*25 - 100)
    def add_disk(self, disk):
        self.disks_list.append(disk)
    def remove_disk(self):
        self.disks_list.pop()

class Disk():
    def __init__(self,size):
        self.size = size
        self.t = turtle.Turtle()
        self.t.up()
        self.t.speed(3)
        self.t.shape('square')
        self.t.shapesize(1, self.size)
    def move_disk(self, ori_pole, des_pole):
        ori_pole.remove_disk()
        des_pole.add_disk(self)
        self.t.goto(des_pole.location, len(des_pole.disks_list)*25 - 125)
        print(len(ori_pole.disks_list))
        print(len(des_pole.disks_list))

pa = Pole(-200)
pb = Pole(0)
pa.initial_disks(3)
pa.disks_list[-1].move_disk(pa,pb)
pa.disks_list[-1].move_disk(pa,pb)
m = turtle.Screen()
m.exitonclick()