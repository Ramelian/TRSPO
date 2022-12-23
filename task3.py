import threading
import time
import os
from queue import Queue

class CollatzNumber:
    def __init__(self, value):
        self.initialValue = value
        self.step = 1
        self.currentValue = value

    def getInitialValue(self):
        return self.initialValue

    def getSteps(self):
        return self.step

    def getCurrentValue(self):
        return self.currentValue

def collatz(el):
    el.step += 1
    if el.currentValue % 2 == 0:
        el.currentValue = el.currentValue / 2
    else:
        el.currentValue = 3 * el.currentValue + 1


def collatzSolution():
    while True:
        print(len(collatzNumbers))

        if len(collatzNumbers) == N and newQueue.qsize() == 0:
            break

        element = newQueue.get()
        if element.currentValue == 1:
            lock.acquire()
            collatzNumbers.append(element)
            lock.release()

        else:
            collatz(element)
            newQueue.put(element)


if __name__ == '__main__':
    N = 1000
    newQueue = Queue()
    collatzNumbers = []
    lock = threading.Lock()


    for i in range(1, N + 1):
        newQueue.put(item=CollatzNumber(i))

    threads = []
    cpuThreads = os.cpu_count()
    startTime = time.time()
    print("Started")

    for i in range(cpuThreads):
        threads.append(threading.Thread(target=collatzSolution, args=()))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("Is finished in %s seconds" % (time.time() - startTime))