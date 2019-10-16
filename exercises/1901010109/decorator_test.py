import time
def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("The func '{}' used {}s.".format(func.__name__, end-start))
        return result
    return wrapper

@log
def fuck(name):
    """Fuck someone"""
    print("Fuck", name)


def a_decorator(func):
    def wrapper():
        print("We can do sth. before calling a_func...")
        func()
        print("... and we can do sth. after it was called...")
    return wrapper
@a_decorator
def a_func():
    print("Hi, I'm a_func!")

a_func()
# a_decorator(a_func)