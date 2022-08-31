#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for nb in set(my_list):
        res += nb
    return res
