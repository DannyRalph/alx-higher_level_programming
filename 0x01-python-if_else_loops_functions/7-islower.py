#!/usr/bin/python3

def islower(c):
    '''
    islower - check for lowercase
    c: character to be checked
    Return: True if lowercase, else False
    '''
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
