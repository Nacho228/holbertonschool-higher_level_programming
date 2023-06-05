#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    else:
        summ = sum(int(i) for i in sys.argv[1:])
        print(summ)
