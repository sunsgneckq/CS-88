######################
# Required Questions #
######################

def sine(x):
    """Returns the value of sine(x), where x is a value in radians.

    >>> from math import pi
    >>> sine(pi) #Notice how the value is very small but not quite 0.
    -1.482085565385205e-09 
    >>> sine(pi/2)
    1.0
    >>> sine((7 * pi)/2)
    -1.0
    >>> sine(1.5)
    0.9974949867067586
    """
    if abs(x) < 0.0001:
         return x
    else: 
         return 3 * sine(x / 3) - 4 * pow(sine(x / 3), 3) 


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n in (1,2,3):
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

# Iterative solution, if you're curious
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c


def hailstone_iterative(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_iterative(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2 
        else: 
            n= 3*n+1
        length = length +1
    print(n)
    return length
    


def hailstone_recursive(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone_recursive(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    list = []
    print(n)
    list. append(n)
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            list. append(n)
        else:
            n = 3 * n + 1
            print(n)
            list. append(n)
    y = len(list)
    return (y)


def first(s):
    """Return the first element in a sequence."""
    return s[0]

def rest(s):
    """Return all elements in a sequence after the first"""
    return s[1:]

def remove(x, s):
    """Remove first element equal to x from sequence s.

    >>> remove(1,[])
    []
    >>> remove(1,[1])
    []
    >>> remove(1,[1,1])
    [1]
    >>> remove(1,[2,1])
    [2]
    >>> remove(1,[3,1,2])
    [3, 2]
    >>> remove(1,[3,1,2,1])
    [3, 2, 1]
    >>> remove(5, [3, 5, 2, 5, 11])
    [3, 2, 5, 11]
    """
    try:
        s.remove(x);
        return s
    except ValueError:
        return s
    
     



def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# Iterative solution, if you're curious
def gcd_iter(a, b):
    """Returns the greatest common divisor of a and b, using iteration.

    >>> gcd_iter(34, 19)
    1
    >>> gcd_iter(39, 91)
    13
    >>> gcd_iter(20, 30)
    10
    >>> gcd_iter(40, 40)
    40
    """
    if a < b:
        return gcd_iter(b, a)
    while a > b and not a % b == 0:
        a, b = b, a % b
    return b



###################
# Extra Questions #
###################

def summation(n, term):
    """Return the sum of the first n terms of a sequence.

    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"

