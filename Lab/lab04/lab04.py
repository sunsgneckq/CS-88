import string

## Code to generate list of shakespear words
def word_generator(filename):
    """
    Returns a generator over the words in a txt file.
    """
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                yield word.lower().strip(string.punctuation)

## Shakespeare words list
shakespeare_list = list(word_generator("shakespeare.txt"))



## Mutation Mystery

## Case 3
from copy import deepcopy
def deep_copy(lst):
    """Returns a new list that is a deep copy of lst.
    >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
    >>> y = deep_copy(x)
    >>> y[0][1] = 'z'
    >>> y
    [[0, 'z'], [1, 'b'], [2, 'c']]
    >>> x
    [[0, 'a'], [1, 'b'], [2, 'c']]
    >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
    >>> z = deep_copy(x)
    >>> z[0][1] = 'z'
    >>> z
    [[0, 'z'], [1, 'b'], [2, 'c']]
    >>> x       #x should not change
    [[0, 'a'], [1, 'b'], [2, 'c']]
    """
    return [list(i)for i in lst]
       


## Explanation
def case3_explanation():
    return "Eve uses slice[:] to copy the list will be fine but in her case there's sublist. However, in python, if you change the element in one of the sublist, then both the content will be changed. Thus, here she needs deepcopy instead of slice copy."


## Dictionary Mutation 

def word_count_dictionary(word_list):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input list of words.

    >>> d = word_count_dictionary(shakespeare_list)
    >>> d["the"]
    51
    >>> d["but"]
    12
    >>> d["thy"]
    5
    """
    index = 0
    dictionary = {}
    while (index < len(word_list)):
        dictionary[word_list[index]] = word_list.count(word_list[index])
        index += 1
    return dictionary

## Nested List Mutation

def word_count_list(word_list):
    """ Returns a list of lists where each inner list is equal to
    [word, count].

    >>> lists = word_count_list(shakespeare_list)
    >>> lists[0]
    ['the', 51]
    >>> lists[183]
    ['but', 12]
    >>> lists[78]
    ['thy', 5]
    """
    index = 0
    dictionary = {}
    new_list = []
    while (index < len(word_list)):
        dictionary[word_list[index]] = word_list.count(word_list[index])
        index += 1
    for key, value in dictionary.items():
        temp = [key,value]
        new_list.append(temp)
    return new_list
        



## List/Tuple Mutation 

def word_count_tuple(word_list):
    """ Returns a list of tuples where each tuple is equal to
    (word, count).

    >>> tuples = word_count_tuple(shakespeare_list)
    >>> tuples[0]
    ('the', 51)
    >>> tuples[183]
    ('but', 12)
    >>> tuples[78]
    ('thy', 5)
    """
    index = 0
    dictionary = {}
    while (index < len(word_list)):
        dictionary[word_list[index]] = word_list.count(word_list[index])
        index += 1
    tuple = list(dictionary.items())
    return tuple



## get_word_count

def get_word_count(lists, word):
    """ Given a list of tuples or lists (such as those returned by
    word_count_tuple and word_count_list), returns the count of a word.

    >>> lists = word_count_list(shakespeare_list)
    >>> get_word_count(lists, "the")
    51
    >>> tuples = word_count_tuple(shakespeare_list)
    >>> get_word_count(tuples, "the")
    51
    """
    index = 0
    while (index < len(lists)):
        if word == lists[index][0]:
            return lists[index][1]
        else:
            index += 1

## Mutating function

import string

def word_count_fun(word_list):
    """ Returns a list of lists where each inner list is equal to
    [word, count].

    >>> word_count_fun(["one", "two", "two"])
    [['one', 1], ['two', 2]]
    """
    lists = []
    def add_word(word):
        nonlocal lists
        for element in lists:
            if element[0]== word:
                element[1]+=1
                return
        lists.append([word, 1])
    for word in word_list:
        add_word(word)
    return lists

