from threading import *
import time

class abi(Thread):
    def run(self):
        for i in range(1,6):
            print('abi proposes sambath')
            time.sleep(1)


class roshini(Thread):
    def run(self):
        for i in range(1,6):
            print('roshini proposes sambath')
            time.sleep(1)

t1=abi()
t2=roshini()


t1.start()
time.sleep(0.3)
t2.start()

t1.join()
t2.join()
print(t1.isAlive())
print(t1.getName())
print(t2.getName())


