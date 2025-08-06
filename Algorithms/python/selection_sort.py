""" Sort an array of n elements by Selection Sort."""

def selection_sort(A, n):
    """ Sort a list.

    Arguments:
    A -- a list
    n -- length of A
    """
    # Traverse list from 0 to n - 2 (where n - 1 is the index of the final value)
    for i in range(n - 1):
        smallest = i

        # Traverse list from the index after the current ith value to the end
        # Recall that python's range is not inclusive for the upper bound
        for j in range(i + 1, n):
            if A[j] < A[smallest]:
                smallest = j

        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp

if __name__ == "__main__":

    import numpy as np

    # Repeating terms
    list1 = [11, 1, 51, 1, 5, 3]
    list1test = list(list1)
    selection_sort(list1, len(list1))
    print(list1)
    print(list1 == sorted(list1test))

    # Empty list should return empty list
    list2 = []
    selection_sort(list2, len(list2))
    print(list2)
    print(not list2)

    # Negative number
    list3 = [11, -1, 51, 1, 5, 3]
    list3test = list(list3)
    selection_sort(list3, len(list3))
    print(list3)
    print(list3 == sorted(list3test))

    # Float and int. Numpy array
    array1 = np.array([11, -4, 20, 15, 13.5, -20])
    array1test = np.copy(array1)
    selection_sort(array1, len(array1))
    print(array1)
    print(np.array_equal(array1, np.sort(array1test)))

    # Already sorted array
    array2 = np.array(range(50))
    array2test = np.copy(array2)
    selection_sort(array2, len(array2))
    print(array2)
    print(np.array_equal(array2, np.sort(array2test)))

    # Reversed sorted array
    array3 = np.array([50, 0, -5])
    array3test = np.copy(array3)
    selection_sort(array3, len(array3))
    print(array3)
    print(np.array_equal(array3, np.sort(array3test)))

    # Large array
    array4 = np.random.randint(-5000, 5000, size=1000)
    array4test = np.copy(array4)
    selection_sort(array4, len(array4))
    print("Large array")
    print(np.array_equal(array4, np.sort(array4test)))
