"""Counts the number of inversions in an array."""

def merge_inversions(A, p, q, r):
    """
    Counts the number of times a value in the left subarray (A[p:q]) is greater
    than one in the right subarray (A[q + 1: r]).

    Arguments
    A -- an array/list
    p -- index of first element in the first subarray
    q -- index of last element in the first subarray
    r -- index of last element in the second subarray

    Return Value
    inversions -- the number of inversions between the left and right subarray
    """
    n_L = q - p + 1
    n_R = r - q
    L = A[p: q + 1]
    R = A[q + 1: r + 1]
    i = 0
    j = 0
    k = p
    inversions = 0

    while i < n_L and j < n_R:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inversions += n_L - i
        k += 1

    while i < n_L:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n_R:
        A[k] = R[j]
        j += 1
        k += 1

    return inversions


def count_inversions(A, p=0, r=None):
    """
    Counts the number of inversions in A.

    Arguments
    A -- an array/list
    p -- index of the first element in the array
    r -- index of the last element in the array

    Return value
    inversions -- number of inversions in A
    """
    if r is None:
        r = len(A) - 1

    inversions = 0
    if p < r:
        q = (p + r) // 2
        inversions += count_inversions(A, p, q)
        inversions += count_inversions(A, q + 1, r)
        inversions += merge_inversions(A, p, q, r)
    return inversions


# Testing
if __name__ == "__main__":

    import numpy as np

    # Repeating terms.
    list1 = [11, 1, 51, 1, 5, 3]
    inversions1 = count_inversions(list1)
    print(list1)
    print(inversions1)


    # Empty list should return empty list.
    list2 = []
    inversions2 = count_inversions(list2)
    print(list2)
    print(inversions2)

    # Negative number.
    list3 = [1, 1, -5, 6]
    inversions3 = count_inversions(list3)
    print(list3)
    print(inversions3)

    # Float and int, testing numpy array.
    array1 = np.array([11, -4, 20, 15, 13.5, -20])
    inversions4 = count_inversions(array1)
    print(array1)
    print(inversions4)

    # Already sorted array.
    array2 = np.array(range(50))
    inversions5 = count_inversions(array2)
    print(array2)
    print(inversions5)

    # Array in reversed sorted order.
    array3 = np.arange(50, 0, -5)
    inversions6 = count_inversions(array3)
    print(array3)
    print(inversions6)

    # Large array.
    array4 = np.random.randint(-5000, 5000, size=1000)
    inversions7 = count_inversions(array4)
    print("large array")
    print(inversions7)




