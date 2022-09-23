import threading

cv = threading.Condition()
cur = 1

class MyThread(threading.Thread):
    def __init__(self, name, value, n):
        threading.Thread.__init__(self)
        self.name = name
        self.value = value
        self.n = n

    def run(self):
        global cv
        global cur
        for i in range(self.n):
            with cv:
                while cur != self.value:
                    cv.wait()
                print(self.name, end="")
                cur = (cur % 3) + 1
                cv.notify_all()

if __name__ == '__main__':
    n = int(input())
    thread1 = MyThread("1", 1, n)
    thread2 = MyThread("2", 2, n)
    thread3 = MyThread("3", 3, n)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

