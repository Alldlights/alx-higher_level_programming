#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0")
    else:
        for i in range(1, num_args + 1):
            total += int(sys.argv[i])
        print(total)
