import threading
import random
import time


class firstClass:
    def __init__(self):
        self.count = 0

    def read(self):
        return self.count

    def write(self, value):
        self.count += value


class secondClass:
    def __init__(self):
        self.count = 0

    def read(self):
        return self.count

    def write(self, value):
        self.count += value


def increaseFirst(K1):
    lock.acquire()
    try:
        print("Thread 1_1")
        for _ in range(K1):
            firstObject.write(random.uniform(0, 1000))
    finally:
        lock.release()

    lock.acquire()
    try:
        print("Thread 1_2")
        for _ in range(K1):
            secondObject.write(random.uniform(0, 1000))
    finally:
        lock.release()


def increaseSecond(K2):
    lock.acquire()
    try:
        print("Thread 2_1")
        for _ in range(K2):
            secondObject.write(random.randint(0, 1000))
    finally:
        lock.release()

    lock.acquire()
    try:
        print("Thread 2_2")
        for _ in range(K2):
            firstObject.write(random.randint(0, 1000))
    finally:
        lock.release()


firstObject = firstClass()
secondObject = secondClass()
lock = threading.Lock()
N = random.randint(10, 20)
K1 = random.randint(10000, 20000)
K2 = random.randint(10000, 20000)

threads = []
for i in range(N // 2):
    threads.append(threading.Thread(target=increaseFirst, args=(K1,)))
for i in range(N // 2):
    threads.append(threading.Thread(target=increaseSecond, args=(K2,)))

start = time.time()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# print("First Object number: ", firstObject.read())
# print("Second Object number: ", secondObject.read())
print("Spent time: ", time.time() - start)
