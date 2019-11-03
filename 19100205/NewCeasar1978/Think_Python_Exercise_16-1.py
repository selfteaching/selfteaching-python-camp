class Time:    
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        

def print_time(time):
    print('%.2d : %.2d : %g' %(time.hour,time.minute,time.second))

def time_to_int(time):
    seconds = time.hour*3600 + time.minute*60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    time.hour,time.minute = divmod(seconds,3600)
    time.minute,time.second = divmod(time.minute,60)
    return time


def mul_time(time,number):
    seconds = time_to_int(time) * number
    time = int_to_time(seconds)
    return time

time = Time(4,4,4)
print_time(mul_time(time,0.5))

