#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A decorator is used singleton pattern.
"""


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Counter():
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1
    
    def getvalue(self):
        return self.value


if __name__ == "__main__":
    Counter().add()
    print Counter().getvalue()
    Counter().add()
    print Counter().getvalue()
    Counter().add()
    print Counter().getvalue()
