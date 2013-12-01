#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A decorator is used tag manager.
"""


def makespan(func):
    def wrapper():
        return "<span>" + func() + "</span>"
    return wrapper


def makepara(func):
    def wrapper():
        return "<p>" + func() + "</p>"
    return wrapper


@makepara
@makespan
def sayHello():
    return "hello world"


if __name__ == "__main__":
    print sayHello()
