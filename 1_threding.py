'''
1. Threading is used to run multiple function concurrently(at the same time)
2. Using threading module we can achive threading in python.

## target: the function to be executed by thread
## args: the arguments to be passed to the target function
## name: We can specify a name to the thread
## join: Using join function we keep a thread to wait till ending the thread
'''
import threading
import time

def first_thread():
    print(' \n first_thread started')
    time.sleep(3)
    print(' \n first_thread is ended')

def second_thread(a,b):
    print(' \n second_thread started', a , b)
    time.sleep(2)
    print(' \n second_thread is ended')

ft = threading.Thread(name='worker', target=first_thread)
st = threading.Thread(name='sriram', target=second_thread, args=('sriram','chowdary'))

ft.start()
ft.join()
st.start()

########################
'''
# Error:

1.AttributeError: module 'threading' has no attribute 'thread

Solutin: we need to give the thread in capital letter - Thread
'''
