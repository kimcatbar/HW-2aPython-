from time import time 

def timeme(func):#define decorator functio 
	def wrapper(time1,time2):#insinde of wrapper actaully does something
		t0=time.time()
		call_func = func(time1,time2)
		t1=time.time()
		print (f"Total time {(t1-t0)}")
		return call_func 
	return wrapper


