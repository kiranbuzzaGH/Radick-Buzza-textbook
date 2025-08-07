""" Sort an array of n elements recursively by Insertion Sort."""

def insertion_sort(A, p, q):
    """ Sort a list.

    Arguments:
    A -- a list
    p -- index of the first element in A
    q -- index of the final element in A
    """
    if p >= q:
        return

    insertion_sort(A, p, q - 1)

    key = A[q]
    i = q - 1
    while i >= p and key < A[i]:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key

# Testing
if __name__ == "__main__":

    import numpy as np

    # Repeating terms
    list1 = [11, 1, 51, 1, 5, 3]
    list1test = list(list1)
    insertion_sort(list1, 0, len(list1) - 1)
    print(list1)
    print(list1 == sorted(list1test))

    # Empty list should return empty list
    list2 = []
    insertion_sort(list2, 0, len(list2) - 1)
    print(list2)
    print(not list2)

    # Negative number
    list3 = [11, -1, 51, 1, 5, 3]
    list3test = list(list3)
    insertion_sort(list3, 0, len(list3) - 1)
    print(list3)
    print(list3 == sorted(list3test))

    # Float and int. Numpy array
    array1 = np.array([11, -4, 20, 15, 13.5, -20])
    array1test = np.copy(array1)
    insertion_sort(array1, 0, len(array1) - 1)
    print(array1)
    print(np.array_equal(array1, np.sort(array1test)))

    # Already sorted array
    array2 = np.array(range(50))
    array2test = np.copy(array2)
    insertion_sort(array2, 0, len(array2) - 1)
    print(array2)
    print(np.array_equal(array2, np.sort(array2test)))

    # Reversed sorted array
    array3 = np.array([50, 0, -5])
    array3test = np.copy(array3)
    insertion_sort(array3, 0, len(array3) - 1)
    print(array3)
    print(np.array_equal(array3, np.sort(array3test)))

    # Large array
    array4 = np.random.randint(-5000, 5000, size=100)
    array4test = np.copy(array4)
    insertion_sort(array4, 0, len(array4) - 1)
    print("Large array")
    print(np.array_equal(array4, np.sort(array4test)))
