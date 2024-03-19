#!/usr/bin/python3


def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght < 0:
        return "None"
    else:
        f_s = sentence[0]
        return (lenght, f_s)
