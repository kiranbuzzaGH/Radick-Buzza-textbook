""" Sort an array of n elements by Merge Sort."""

def merge_sort(A, p=0, q=None):
    """ Sort the elements in the sublist/subarray

    Arguments:
    A -- a list
    p -- index of first element in the sublist/subarray (default = 0)
    q -- index of last element in the sublist (default = None)
    """

    if q is None:
        q = len(A) - 1
    if p >= q:
        return

    mid = (p + q) // 2
    merge_sort(A, p, mid)
    merge_sort(A, mid + 1, q)
    merge(A, p, mid, q)


def merge(A, p, mid, q):
    """ Merge two sorted sublists/subarrays to a larger sorted sublist/subarray

    Arguments
    A -- a list/array containing the sublists/subarrays to be merged
    p -- index of first element in the first sublist/subarray
    mid -- index of last element in the first sublist/subarray
    (the second sublist/subarray starts at index q+1)
    q -- index of last element in the second sublist/subarray
    """
    # Recall that the right index is not inclusive in python
    if isinstance(A, list):
        left_array = A[p: mid+1]
        right_array = A[mid+1: q+1]
    # In this case A is an array
    else:
        left_array = list(A[p: mid+1])
        right_array = list(A[mid+1: q+1])

    len_left = len(left_array)
    len_right = len(right_array)

    i = 0
    j = 0
    k = p

    while i < len_left and j < len_right:
        if left_array[i] <= right_array[j]:
            A[k] = left_array[i]
            i += 1
        else:
            A[k] = right_array[j]
            j += 1
        k += 1

    if i < len_left:
        A[k: q+1] = left_array[i:]
    if j < len_right:
        A[k: q+1] = right_array[j:]



# Testing
if __name__ == "__main__":

    import numpy as np

    # Repeating terms.
    list1 = [11, 1, 51, 1, 5, 3]
    list1test = list(list1)
    merge_sort(list1)
    print(list1)
    print(list1 == sorted(list1test))

    # Empty list should return empty list.
    list2 = []
    merge_sort(list2)
    print(list2)
    print(not list2)

    # Negative number.
    list3 = [1, 1, -5, 6]
    list3test = list(list3)
    merge_sort(list3)
    print(list3)
    print(list3 == sorted(list3test))

    # Float and int, testing numpy array.
    array1 = np.array([11, -4, 20, 15, 13.5, -20])
    array1test = np.copy(array1)
    merge_sort(array1)
    print(array1)
    print(np.array_equal(array1, np.sort(array1test)))

    # Already sorted array.
    array2 = np.array(range(50))
    array2test = np.copy(array2)
    merge_sort(array2)
    print(array2)
    print(np.array_equal(array2, np.sort(array2test)))

    # Array in reversed sorted order.
    array3 = np.arange(50, 0, -5)
    array3test = np.copy(array3)
    print("Before sorting: ", end = '')
    print(array3)
    merge_sort(array3)
    print("After sorting: ", end = '')
    print(array3)
    print(np.array_equal(array3, np.sort(array3test)))

    # Large array.
    array4 = np.random.randint(-5000, 5000, size=1000)
    array4test = np.copy(array4)
    merge_sort(array4)
    print("large array")
    print(np.array_equal(array4, np.sort(array4test)))
