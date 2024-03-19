#!/usr/bin/python3


def multiple_returns(sentence):
    lenght = len(sentence)
    for i in sentence:
        return (lenght, i[0])
