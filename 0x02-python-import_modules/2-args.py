#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_num = len(argv) - 1
    if arg_num == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(arg_num, 's' if arg_num > 1 else ''))
        for i in range(1, arg_num + 1):
            print("{}: {}".format(i, argv[i]))
