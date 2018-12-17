## Exceptions

def avoid_indexerror(lst, index, missing=None):
    """Return lst[index] if it exists, otherwise missing.

    >>> avoid_indexerror([1,2,3], 1)
    2
    >>> avoid_indexerror([1,2,3], 4)
    >>> avoid_indexerror([1,2,3], 4, "Index out of range.")
    'Index out of range.'
    """
    try:
        lst[index]
    except IndexError:
        return missing
    return lst[index]

def avoid_keyerror(dictionary, key):
    """ Returns the value associated with key in dictionary. If key 
    does not exist in the dictionary, print out 'Avoid Exception' and
    map it to the string 'no value'.

    >>> d = {1: 'one', 3: 'three', 5: 'five'}
    >>> avoid_keyerror(d, 3)
    'three'
    >>> avoid_keyerror(d, 4)
    Avoid Exception
    >>> d[4]
    'no value'
    """
    try:
        dictionary[key]
    except KeyError:
        print('Avoid Exception')
        return dictionary.update({key:"no value"})
    return dictionary[key]


## Generators

def char_gen(s):
    """
    >>> for char in char_gen("hello"):
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    """
    i=0
    while i < len(s):
        yield (s[i])
        i+=1


def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    i=n
    while i>=0:
        yield i
        i=i-1


from math import sqrt

def is_prime(n):
    """
    Return True if n is prime, false otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(19)
    True
    """
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if(n % i==0):
                return False
        return True 

def primes():
    """
    An infinite generator that outputs primes. 

    >>> p = primes()
    >>> for i in range(3):
    ...     print(next(p))
    ...
    2
    3
    5
    """
    i=2
    while True:
        if is_prime(i):
            yield i
        i+=1
        
        
                


## Sequences

def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    a= filter(lambda x: x.lower() == x[::-1].lower(), L)
    return len(list(a))
 
## Naturals generator, needed for doctests

def naturals():
    i = 1
    while True:
        yield i
        i += 1