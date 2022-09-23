from time import sleep
from queue import Queue
from random import randint
import threading

condition = threading.Condition(lock=None)
queue = Queue()


class ProducerThread(threading.Thread):
    def __init__(self, name, n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        global condition
        global queue

        name = int(self.name)
        while True:
            sleep(name)
            cnt = randint(2, 4)
            print("Продавец №%i принес на склад %i товара" % (name, cnt))
            for i in range(cnt):
                queue.put(name)
            for i in range(cnt):
                with condition:
                    condition.notify_all()
                sleep(0.5)
            sleep(2)


class ConsumerThread(threading.Thread):
    def __init__(self, name, n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        global condition
        global queue

        name = int(self.name)
        while True:
            for i in range(name):
                with condition:
                    condition.wait()
            name_good = queue.get()
            print("Покупатель №%i взял товар у Продавца №%i" % (name, name_good))
            for i in range(self.n - name):
                with condition:
                    condition.wait()


if __name__ == "__main__":
    producers = int(input("Введите количество продавцов: "))
    consumers = int(input("Введите количество покупателей: "))
    producers_threads = []
    consumer_threads = []
    for i in range(producers):
        producers_threads.append(ProducerThread(str(i + 1), producers))
        producers_threads[i].start()
    for i in range(consumers):
        consumer_threads.append(ConsumerThread(str(i + 1), consumers))
        consumer_threads[i].start()
