from greenlet import greenlet
import time
def A():
    while 1:
        print("----------A-----------")
        time.sleep(0.5)
        g2.switch()

def B():
    while 1:
        print("--------B----------")
        time.sleep(0.5)
        g1.switch()

g1=greenlet(A)
g2=greenlet(B)
g1.switch()