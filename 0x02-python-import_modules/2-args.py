#!/usr/bin/python3

if __name__ = "__main__":
    import sys
    
    argv = sys.argv[1:]
    n = len(argv)
    i = 1
    if n == 0:
        print("{:d} arguments.".format(n))
    elif n == 1:
        print("{:d} argument.".format(n))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments.".format(n))
        while i < n:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
