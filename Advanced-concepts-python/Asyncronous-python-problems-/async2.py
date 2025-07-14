import time
def a():
    value=b()
    print(value)
def b():
    time.sleep(5)
    return 5
a()