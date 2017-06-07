#!/usr/bin/python
# -*-coding:Utf-8-*

def give_away(lst):
    '''
    The giveaway function takes a list or tuple in param and returns a dictionary
    with as a key the name of the person offering the gift and as a value
    the name of the person who receives the gift
    '''
    result = {}
    for i, elem in enumerate(lst):
        result[elem] = lst[i - 1]
    return(result)