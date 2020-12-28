import main as m
import time
from threading import *
m.create("one",1)
m.create("one",0)#duplicate key
m.create("two",2,2)# with time-to-live value
print(m.read("two"))
#after time-to-live
time.sleep(2) #after 2 min
print('After 2 sec:')
m.read("two")
m.read("three")#key not found error
m.modify("one",11)
m.read("one")
m.delete("one")
m.read("one")
m.delete("one")
thread1= Thread(target=m.create,args=("four",4,))
thread1.start()
thread2= Thread(target=m.delete,args=("four",))
thread2.start()
thread1.join()
thread2.join()


