#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    c = int(sys.argv[3])

    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, op, c, add(a, c)))
    elif op == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, op, c, sub(a, c)))
    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, op, c, mul(a, c)))
    elif op == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, op, c, div(a, c)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
