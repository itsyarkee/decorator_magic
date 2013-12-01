#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A decorator is used time estimating.
"""

import functools
import time

def time_est(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        beg = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print "%s costs %f" % (func.func_name, end - beg)
        return res
    return wrapper


@time_est
def do_something():
    time.sleep(1)
    print "hello"


if __name__ == "__main__":
    do_something()
