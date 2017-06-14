#!/usr/bin/python
# -*-coding:Utf-8-*

import random

def give_away(people, couples):
    '''
    The give_away function is used to make a gift distribution.
    It takes a list of names and a list of couples in parameter and returns a dictionary containing as key
     the name of the person offering the gift and as value the person receiving the gift.
    Your list must contain more than three elements or three items but with no pairs.
    '''
    def _is_couple_(toOffer, person, couples):
        '''
        The _is_couple_ function allows to know if two people are in a couple.
        '''
        for couple in couples:
            if toOffer in couple and person in couple:
                return False
        return True

    def _loop_(people, couples, result, toOffer):
        '''
        The function _loop_ makes it possible to verify if two person are in couple or
        if they are already to send presents and especially to know if they are indeed two different person.

        '''
        for person in reversed(people):
            print(person)
            if person not in result.values() and _is_couple_(toOffer, person, couples)\
                            and result[person] != toOffer and toOffer != person:
                return True, person
        return False, person

    def _working_(people, couples):
        result = {}
        for person in people:
         result[person] = ''
        for toOffer in result:
            ret, person = _loop_(people, couples, result, toOffer)
            if ret is True:
                result[toOffer] = person
            else:
                saveElem = people.pop(random.randrange(people.__len__()))
                people.append(saveElem)
                return False
        return result

    if people.__len__() < 3 or people.__len__() == 3 and couples.__len__():
        print('Error check that your list contains more than three items')
        return
    result = _working_(people, couples)
    while result is False:
        result = _working_(people, couples)
    return result