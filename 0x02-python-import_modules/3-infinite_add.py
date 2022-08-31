#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    av = sys.argv
    ac = len(av)
    for i in range(1, ac):
        res += int(av[i])
    print("{}".format(res))
