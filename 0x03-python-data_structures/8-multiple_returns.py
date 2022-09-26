#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        sentence = (length, sentence[0])
        return (sentence)
    else:
        sentence = (0, None)
        return (sentence)
