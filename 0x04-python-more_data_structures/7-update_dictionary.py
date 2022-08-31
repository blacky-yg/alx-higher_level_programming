#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for nb in a_dictionary:
            if nb == key:
                a_dictionary[nb] = value
    return a_dictionary
