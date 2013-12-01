#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
A decorator is used privilege management. 
"""


is_admin = False


def privilege_check(func):
    def wrapper(*args, **kwargs):
        if is_admin:
            res = func(*args, **kwargs)
        else:
            res = "Error:Your are not administrator."
        return res
    return wrapper 


@privilege_check
def add_user(user):
    print "You try to add user:%s" % user
    #Bla bla.
    return "Add user:%s successful." % user


if __name__ == "__main__":
    print add_user("Yarkee")
