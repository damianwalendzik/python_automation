import threading

#Threading allows us to spped up programs by executing multiple tasks at the same time.
#Each task will run on its own thread
#Each thread can run simultaneously and share data with each other.

#Every thread when you start it must do something, which we can define with a function.
#Our threads will then target these functions.
#When we start the threads, the target functions will be run.

def function1():
    for x in range(10):
        print("ONE ")


def function2():
    for x in range(10):
        print("TWO ")

def function3():
    for x in range(10):
        print("THREE ")

#If we call these functions, we see the first function call must complete before the next
#They are executed linearly
function1()
function2()
function3()

#We can execute these function concurrently using threads. We must have a target for a thread.
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

t1.start()
t2.start()
t3.start()

#Threads can only be run once. If you want to reuse, you must redefine

#If you want to pause the main program until a thread is done - you can.

t1 = threading.Thread(target=function1)
t1.start()
t1.join() #This pauses the main program until the thread is complete
print("Threading is great.")