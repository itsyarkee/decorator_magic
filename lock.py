#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A decorator is used for synchronization.
"""

import threading
glock = threading.Lock()

def sync(lock):
    def mydec(func):
        def wrapper(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)
        return wrapper
    return mydec


@sync(glock)
def sayHello(num):
    print "hello world, %d" % num
    print "hello decorator, %d" % num


if __name__ == "__main__":
    threads = []
    for i in range(0, 10):
        threads.append(threading.Thread(target=sayHello, args=(i,)))
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
    for i, thread in enumerate(threads):
        thread.join(1)
