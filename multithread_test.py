import _thread
import time
import random

#this demostration is similar to creating thread using Runnable interface in java.

def run_fun(threadName):
    loopCount = 5
    while loopCount >0:
        time.sleep(random.randint(0, 10))
        print(f'{threadName} is excuting at {time.ctime(time.time())}')
        loopCount -=1

try:
    _thread.start_new_thread(run_fun, ("first_thread",))
    _thread.start_new_thread(run_fun, ("second_thread",))
except:
    print('unable to start new thread')
