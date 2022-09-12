#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_elem = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            nb_elem += 1
        except Exception:
            pass
    print()
    return nb_elem
