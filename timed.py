import time 

def timeme(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f'Total time {(t2-t1)}')
    return wrapper
  
#@timme this in leu of calling test_time = ........
#def test_time():
  # time.sleep(2)
   
#test_time = timer_func(test_time)
#test_time()
