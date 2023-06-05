#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv):
            print(f"{i:0}: {arg}")
