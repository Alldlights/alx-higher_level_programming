#!/usr/bin/python3


def multiple_returns(sentence):
    lenght = len(sentence)
    for i in sentence:
        if lenght > 0:
            return (lenght, i[0])
        else:
            return "None"
