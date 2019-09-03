import time
def func():
    i = 1000
    while i > 0:
 
        i -= 1
i = 20
while i > 0:        
    t1 = time.process_time()
    func()
    t2 = time.process_time() - t1
    i -= 1  
    print(t2)
