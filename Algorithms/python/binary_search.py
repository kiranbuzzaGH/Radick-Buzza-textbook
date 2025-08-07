"""
Searches for a value within an sorted list or array and returns its index if it is present or
NIL if it is not, using Binary Search
"""

def binary_search(A, p, q, x):
    """
    Search for an element in a sorted list or array

    Arguments
    A -- a sorted list or numpy array
    p -- index of first element in array being searched
    q -- index of final element in array being searched
    x -- a value of the same type as the array
    """

    if p > q:
        return None

    m = (int) ((q + p) / 2)

    if x == A[m]:
        return m
    if x > A[m]:
        return binary_search(A, m + 1, q, x)
    else:
        return binary_search(A, p, m - 1, x)

if __name__ == "__main__":

    import numpy as np

    # Repeating terms
    list1 = [1, 3, 4, 5, 4, 4]
    X1 = 4
    index = binary_search(list1, 0, len(list1) - 1, X1)
    print("Repeating terms")
    print(index == list1.index(X1))

    # Empty list
    list2 = []
    X2 = 4
    index = binary_search(list2, 0, len(list2) - 1, X2)
    print("Empty list")
    print(index is None)

    # Negative number
    list3 = [12, -34, 3, 4]
    X3 = -34
    index = binary_search(list3, 0, len(list3) - 1, X3)
    print("Negative number")
    print(index == list3.index(X3))

    # Floats and ints
    list4 = [23, 44, 3.5, 4, 8.4]
    X4 = 3.5
    index = binary_search(list4, 0, len(list4) - 1, X4)
    print("Floats and ints")
    print(index == list4.index(X4))

    # Large array
    array1 = np.array(range(100))
    X5 = 34
    index = binary_search(array1, 0, len(array1) - 1, X5)
    print(array1)
    print(index == X5)
