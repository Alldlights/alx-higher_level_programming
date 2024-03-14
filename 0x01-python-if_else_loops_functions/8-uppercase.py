#!/usr/bin/python3


def uppercase(str):
    uppercase = ""
    for s in str:
        if s >= 'a' and s <= 'z':
            uppercase += chr(ord(s) - 32)
        else:
            uppercase += s
    print("{}".format(uppercase))
