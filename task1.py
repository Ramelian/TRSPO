import threading
import time

def hello():
    time.sleep(2)
    print("hello")

def name(name):
    time.sleep(1)
    print(name)

def wish():
    time.sleep(3)
    print("Have a good day")

threading_one = threading.Thread(target=hello, args = ())
personName = "John"
threading_two = threading.Thread(target=name, args = (personName,))
threading_three = threading.Thread(target=wish, args = ())

threading_one.start()
threading_two.start()
threading_three.start()

threading_one.join()
threading_two.join()
threading_three.join()

print("Threading finished!")