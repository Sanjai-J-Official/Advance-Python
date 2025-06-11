from threading import Thread

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello,python")
class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hii,python")
t1=hello()
t2=hi()
t1.start()
t2.start()