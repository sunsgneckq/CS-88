"""Lab 2: FunArgs and Higher Order Functions. """

## Functions as Arguments

def twice(f,x):
    """Apply f to the result of applying f to x"
    >>> twice(square,3)
    81
    """
        
    return f(f(x))

def apply_n(f, x, n):
    """Apply function f to x n times.

    >>> apply_n(increment, 2, 10)
    12
    """ 
    for i in range(n):
        x=f(x)
    return x


## Returning Functions

def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> at_three = intersects(square, 3)
    >>> at_three(triple) # triple(3) == square(3)
    True
    >>> at_three(increment)
    False
    >>> at_one = intersects(identity, 1)
    >>> at_one(square)
    True
    >>> at_one(triple)
    False
    """
    def at_x(g):
        return  f(x)==g(x)
    return at_x


def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    def h(x):
        if x < b:
            return f(x)
        return g(x)
    return h 


def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    def buzz(m):
        i = 0
        while i < m:
            if i % n == 0:
                print('Buzz!')
            else:
                print(i)
            i += 1
    return buzz



## Map, Reduce, Accumulate


def map(f,s):
    return [f(x) for x in s]



def mapn(f, n):
    """Return the list resulting from applying function f to the seguence 0 to n-1.

    >>> mapn(square,4)
    [0, 1, 4, 9]
    """
    return [f(n) for n in range(n)]


def maxfun(f, g, low, high):
    """Return the list of the maximums of f and g applied to the low..high-1.

    >>> maxfun(four,square,-4,4)
    [16, 9, 4, 4, 4, 4, 4, 9]
    """
    return [max(f(x),g(x)) for x in range(low, high)]



def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    reduced = base
    for x in s:
        reduced = reducer(reduced,x)
    return reduced


from operator import add, mul

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    total = base
    k = 1
    while k <= n:
        total = combiner(total, term(k))
        k = k + 1
    return total

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    """
    return accumulate(mul, 1, n, term)


## Helper Functions for Doctests

def identity(x):
    return x

def four(x):
    return 4

def increment(x):
    return x + 1

def triple(x):
    return 3 * x

def square(x):
    return x * x

def sqrt(x):
    return x**(1/2)




