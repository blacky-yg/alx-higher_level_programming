#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp_list = []
    len_list = len(my_list)
    for i in range(len_list):
        if my_list[i] == search:
            cp_list.append(replace)
        else:
            cp_list.append(my_list[i])
    return cp_list
