#!/usr/bin/python3
for l in range(ord('a'), ord('z') + 1):
    if l != ord('e') and l != ord('q'):
        print("{:c}".format(l), end="")
