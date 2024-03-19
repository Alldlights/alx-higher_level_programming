#!/usr/bin/python3


def multiple_returns(sentence):
    lenght = len(sentence)
    for i in sentence:
        if i[0] != None:
            return (lenght, i[0])
