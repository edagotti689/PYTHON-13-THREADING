'''
1. threading.active_count(): Returns the number of total Python thread that are active. 
2. threading.currentThread(): Returns the currentThread object
'''
import threading
import time

def first_thread():
    print(' \n First thread name is :::::', threading.currentThread().getName())
    time.sleep(5)

def second_thread(a,b):
    print(' \n Second thread name is :::::', threading.currentThread().getName())
    print(' \n Active thread count is :', threading.active_count())
    time.sleep(3)

ft = threading.Thread(name='Add', target=first_thread)
st = threading.Thread(name='sriram', target=second_thread, args=('sriram','chowdary'))

ft.start()
st.start()

