import time 
def timestamp(func):
    def wrapper():
        the_time = time.ctime()
        print(the_time)
        func()
    return wrapper
