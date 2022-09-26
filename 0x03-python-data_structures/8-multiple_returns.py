#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        sentence = (length, sentence[0])
        return (sentence)
    else:
        length = len(sentence)
        senctence = (length, None)
        return (sentence)
