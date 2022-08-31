#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    files = dir()
    for i in range(0, len(files)):
        if files[i][0:2] != "__":
            print("{}".format(files[i]))
