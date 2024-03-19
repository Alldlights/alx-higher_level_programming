#!/usr/bin/python3


def multiple_returns(sentence):
    lenght = len(sentence)
    for i in sentence:
        if lenght < 0:
            return "None"
        else:
            return (lenght, i[0])
