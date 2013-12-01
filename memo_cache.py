#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A decorator is used as cache.
"""


def memo(func):
    cache = {}
    def wrapper(*args):
        res = cache.get(args, None)
        if res is None:
            res = func(*args)
            cache[args] = res
        return res
    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print fib(100)
