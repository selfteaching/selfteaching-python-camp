def infix_to_postfix_2(string):
    string = string.replace('(',' ( ')
    string = string.replace(')',' ) ')
    string = string.replace('+',' + ')
    string = string.replace('-',' - ')
    string = string.replace('*',' * ')
    string = string.replace('/',' / ')
    string = string.replace('^',' ^ ')
    ori_list = string.split()
    op_list , res_list = [] , []
    preference = {'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
    for chr in ori_list:                 
        if chr == '(':
            op_list.append(chr)
        elif chr == ')':
            while op_list[-1] != '(':
                res = op_list.pop()                
                res_list.append(res)
            op_list.pop()  
        elif chr in ['+','-','*','/','^']:              
            while len(op_list) > 0 and preference[op_list[-1]] >= preference[chr]:
                res = op_list.pop()                
                res_list.append(res)                  
            op_list.append(chr)            
        else:
            res_list.append(chr)  
    op_list.reverse()
    res_list += op_list
    return ' '.join(res_list)

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def infix_to_postfix_1(infix_expr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    infix_expr = infix_expr.replace('(',' ( ')
    infix_expr = infix_expr.replace(')',' ) ')
    infix_expr = infix_expr.replace('+',' + ')
    infix_expr = infix_expr.replace('-',' - ')
    infix_expr = infix_expr.replace('*',' * ')
    infix_expr = infix_expr.replace('/',' / ')
    infix_expr = infix_expr.replace('^',' ^ ')
    token_list = infix_expr.split()

    for token in token_list:
        if token[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
            (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

def postfix_eval(string):
    string = string.replace('(',' ( ')
    string = string.replace(')',' ) ')
    string = string.replace('+',' + ')
    string = string.replace('-',' - ')
    string = string.replace('*',' * ')
    string = string.replace('/',' / ')
    string = string.replace('^',' ^ ')
    exp_list = string.split()
    
    buf_list = []
    for chr in exp_list:
        if chr[0] in ['0','1','2','3','4','5','6','7','8','9']:            
            buf_list.append(int(chr))
            
        elif chr in ['+','-','*','/','^']:
            op1 = buf_list.pop()
            op2 = buf_list.pop()
            res = do_math(chr,op1,op2)
            buf_list.append(res)         
    return buf_list[0]

def do_math(op,op1,op2):
    if op == '+':
        return op2 + op1
    elif op == '-':
        return op2 - op1
    elif op == '*':
        return op2 * op1
    elif op == '/':
        return op2 / op1
    elif op == '^':
        return op2 ** op1
    


s1 = '( A + B ) * C - ( D - E ) * ( F + G )'
s2 = '( A + B ) * ( C + D )/(E+F*G-G^(Q-W/P))'
s3 = '10 +3*5 /(16 - 4)'
s4 =  '5 * 3^(4- 2 )'
s0 = '10 3 5 * 16  4 - / + '

#print(infix_to_postfix_1(s2))        

#print(infix_to_postfix_2(s2))     
#print(infix_to_postfix(s4))  
class Queue_2():
    def __init__(self):
        self.items = []        
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,item):
        self.items = [item] + self.items             
    def dequeue(self):
        return self.items.pop()        
    def size(self):
        return len(self.items)

def hot_potato_2(tot_num,constant):
    q = Queue_2()
    for i in range(1,tot_num+1):
        q.enqueue(str(i))    
    while q.size() > 1:
        for j in range(constant):
            temp = q.items[-1]
            q.dequeue()
            q.enqueue(temp)
        q.dequeue()
    return q.items.pop()



class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def hot_potato_1(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()
'''n=7
l = ["Bill", "David", "Susan", "Jane", "Kent", "Brad","Jack"]
print(hot_potato_2(40,7))
print(l[int(hot_potato_2(7,n))-1])
print(hot_potato_1(l, n))
'''

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False
    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

import random
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    def get_stamp(self):
        return self.timestamp
    def get_pages(self):
        return self.pages
    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size()))

def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
for i in range(10):
    simulation(3600, 10)
    
class Deque():
    def __init__(self):
        self.items = []
    def add_rear(self, item):
        self.items.insert(0, item)
    def add_front(self, item):
        self.items.append(item)
    def remove_rear(self):
        return self.items.pop(0)
    def remove_front(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self,new_next):
        self.next = new_next
    def __str__(self):
        if self.get_next() != None:
            return str(self.get_data()) +' '+ str(self.next.get_data())
        else:
            return str(self.get_data()) +' None'

class UnorderedList():
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = current.get_next()
            count += 1
        return count
    
    def __str__(self):
        string = ''
        current = self.head
        while current != None:
            string += str(current.get_data()) + ','
            current = current.get_next()
        return '['+ string[:-1] + ']'
    def search(self,item):
        current = self.head        
        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    def remove(self, item):
        current = self.head     
        previous = None
        found = False
        while not found:            
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()                
        if previous == None:
            self.head = current.get_next()                                
        else:
            previous.set_next(current.get_next())

class OrderedList():
    def __init__(self):        
        self.head = None     
    def search(self,item):
        current = self.head        
        while current != None:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            else:
                current = current.get_next()
        return False
    def add(self,item):
        previous = None
        current =self.head
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)
    def __str__(self):
        string = ''
        current = self.head
        while current != None:
            string += str(current.get_data()) + ','
            current = current.get_next()
        return '['+ string[:-1] + ']'
    def add1(self, item):
        previous = None
        current = self.head        
        
        while current != None:
            if current.get_data() > item:
                print(1)
                break
            else:
                print(2)
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            print(3)
            temp.set_next(self.head)
            self.head = temp
        else:
            print(4)
            previous.set_next(temp)
            temp.set_next(current)
        print('over')
import turtle
def snow(t,len,n):
    if n == 0:
        t.fd(len)
    else:
        snow(t,len/3,n-1)
        t.lt(60)
        snow(t,len/3,n-1)
        t.rt(120)
        snow(t,len/3,n-1)
        t.lt(60)
        snow(t,len/3,n-1)
        



t=turtle.Turtle()
snow(t,300,4)
m = turtle.Screen()
m.exitonclick()

import turtle
def tree(branch_len, t, n):
    if n > 0:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len-15, t, n-1)
        t.left(40)
        tree(branch_len-15, t, n-1)
        t.right(20)
        t.backward(branch_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100, t, 6)
    my_win.exitonclick()
main()

def tree_2(t, len, n):
    if n > 0:
        t.pensize(n+1)
        t.pencolor((0, 0.5-0.06*n, 0))
        t.fd(len)
        angle_1 = random.randrange(10,30)
        angle_2 = random.randrange(10,30)
        t.rt(angle_1)
        tree(t, len-random.randrange(10,20), n-1)
        t.lt(angle_1 + angle_2)
        tree(t, len-random.randrange(10,20), n-1)
        t.rt(angle_2)
        t.pencolor((0, 0.5-0.06*n, 0))
        t.bk(len)

def main2():
    t.pensize(7)
    t.lt(90)
    t.up()
    t.bk(200)
    t.down()
    #t.color('green')
    tree_2(t, 110, 7)
    m = turtle.Screen()
    m.exitonclick()
main2()

def triangle(t, points):
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
def get_mid(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]
def sierpinski(t, points, n):
    if n > 0:
        triangle(t,points)
        sierpinski(t,[points[0],\
        get_mid(points[0],points[1]),\
        get_mid(points[0],points[2])],\
        n-1)
        sierpinski(t,[points[1],\
        get_mid(points[1],points[0]),\
        get_mid(points[1],points[2])],\
        n-1)
        sierpinski(t,[points[2],\
        get_mid(points[2],points[0]),\
        get_mid(points[2],points[1])],\
        n-1)
import turtle
points = [[-200,-100],[0,200],[200,-100]]
t = turtle.Turtle()
#sierpinski(t, points, 3)

# 以下为迷宫程序
import turtle
PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        rows_in_maze = 0
        columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_file_name,'r')
        rows_in_maze = 0
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[: -1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze
        self.x_translate = - columns_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(- (columns_in_maze - 1) / 2 - .5,
                - (rows_in_maze - 1) / 2 - .5,
                (columns_in_maze - 1) / 2 + .5,
                (rows_in_maze - 1) / 2 + .5)
    def draw_maze(self):
        self.t.speed(10)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, - y + self.y_translate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):   
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate,- y + self.y_translate))
        self.t.goto(x + self.x_translate, - y + self.y_translate)
    def drop_bread_crumb(self, color):
        self.t.dot(10, color)
    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        if color:
            self.drop_bread_crumb(color)
    def is_exit(self, row, col):
        return (row == 0 or
            row == self.rows_in_maze - 1 or
            col == 0 or
            col == self.columns_in_maze - 1)
    def __getitem__(self,idx):
        return self.maze_list[idx]
def search_from(maze, start_row, start_column):
    # try each of four directions from this point until we find away out.
    # base Case return values:
    # 1. We have run into an obstacle, return false 
    maze.update_position(start_row, start_column)
    if maze.maze_list[start_row][start_column] == OBSTACLE :
        return False
    # 2. We have found a square that has already been explored

    if maze.maze_list[start_row][start_column] == TRIED or maze.maze_list[start_row][start_column] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row,start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = search_from(maze, start_row-1, start_column) or \
        search_from(maze, start_row+1, start_column) or \
        search_from(maze, start_row, start_column-1) or \
        search_from(maze, start_row, start_column+1)
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found
my_maze = Maze('maze2.txt')
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)
search_from(my_maze, my_maze.start_row, my_maze.start_col)

# 以上为迷宫程序
#以下为汉诺塔程序
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
        self.shaft.fd(300)
        self.shaft.bk(300)

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
#以上为汉诺塔程序




