#!/usr/bin/python3
# prints numbers from 0 to 99

for num in range(0, 100):
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
