"""
Searches for a value within an array and returns its index if it is present or
NIL if it is not, using Linear Search
"""

def linear_search(A, n, x):
    """
    Search for an element in a list

    Arguments
    A -- a list or numpy array
    n -- length of A
    x -- a value of the same type as the array
    """

    for i in range(n):
        if A[i] == x:
            return i
    return None

if __name__ == "__main__":

    import numpy as np

    # Repeating terms
    list1 = [1, 3, 4, 5, 4, 4]
    X1 = 4
    index = linear_search(list1, len(list1), X1)
    print("Repeating terms")
    print(index == list1.index(X1))

    # Empty list
    list2 = []
    X2 = 4
    index = linear_search(list2, len(list2), X2)
    print("Empty list")
    print(index is None)

    # Negative number
    list3 = [12, -34, 3, 4]
    X3 = -34
    index = linear_search(list3, len(list3), X3)
    print("Negative number")
    print(index == list3.index(X3))

    # Floats and ints
    list4 = [23, 44, 3.5, 4, 8.4]
    X4 = 3.5
    index = linear_search(list4, len(list4), X4)
    print("Floats and ints")
    print(index == list4.index(X4))

    # Large array
    array1 = np.array(range(1000))
    X5 = 345
    index = linear_search(array1, len(array1), X5)
    print("large array")
    print(index == X5)
