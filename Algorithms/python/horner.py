"""
Evaluates a polynomial given an array/list of coefficients for a given value
of x using Horner's rule.
"""

def horner(A, x, n=None):
    """Evaluates a polynomial.

    Arguments
    A -- a list/array of the coefficients
    n -- the number of terms (non-zero or otherwise) (default = None)
    x -- the value with which the polynomial is being evaluated
    """
    if n is None:
        n = len(A) - 1

    p = 0

    # from n to 0 (zero indexed)
    for i in range(n, -1, -1):
        p = A[i] + x*p

    return p


# Testing
if __name__ == "__main__":

    import numpy as np

    # list of integers with integer value
    list1 = [1, 2, 3, 4, 5]
    X1 = 2
    result1 = horner(list1, X1)
    list1.reverse()
    result1test = np.polyval(list1, X1)
    print(result1)
    print(result1test)
    print(result1 == result1test)

    # Large array with negative ints and float value
    array1 = np.random.randint(-100, 100, size=100)
    X2 = 1.1
    result2 = horner(array1, X2)
    result2test = np.polyval(np.flip(array1), X2)
    print(result2)
    print(result2test)
    print(result2 == result2test)
