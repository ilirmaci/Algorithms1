'''Sort a list of entries using the Quick Sort Algorithm with
various pivot selection procedures.'''

# pivot selection procedure
def select_first(L, start, end):
    '''(list, int, int) -> int
    Return index of first element to be used as pivot for
    partitioning L[start:end].

    Prerequisites: 0 <= start, end <= len(L); start <= end.
    '''
    assert (0 <= start), "Starting index lower than 0."
    assert (start <= len(L)), "Starting index greater than length."
    assert (0 <= end), "Ending index lower than 0."
    assert (end <= len(L)), "Ending index greater than length."
    assert (start <= end), "Starting index greater than ending index."

    return start    # pick first element

def select_last(L, start, end):
    '''(list, int, int) -> int
    Return index of last element to be used as pivot for
    partitioning L[start:end].

    Prerequisites: 0 <= start, end <= len(L); start <= end.
    '''
    assert (0 <= start), "Starting index lower than 0."
    assert (start <= len(L)), "Starting index greater than length."
    assert (0 <= end), "Ending index lower than 0."
    assert (end <= len(L)), "Ending index greater than length."
    assert (start <= end), "Starting index greater than ending index."

    return end - 1    # pick last element

def select_middle(L, start, end):
    '''(list, int, int) -> int
    Return index of middle element to be used as pivot for
    partitioning L[start:end].

    Prerequisites: 0 <= start, end <= len(L); start <= end.
    '''
    assert (0 <= start), "Starting index lower than 0."
    assert (start <= len(L)), "Starting index greater than length."
    assert (0 <= end), "Ending index lower than 0."
    assert (end <= len(L)), "Ending index greater than length."
    assert (start <= end), "Starting index greater than ending index."

    return (end + start - 1) // 2    # pick middle element

def select_random(L, start, end):
    '''(list, int, int) -> int
    Return index of random element to be used as pivot for
    partitioning L[start:end].

    Prerequisites: 0 <= start, end <= len(L); start <= end.
    '''
    assert (0 <= start), "Starting index lower than 0."
    assert (start <= len(L)), "Starting index greater than length."
    assert (0 <= end), "Ending index lower than 0."
    assert (end <= len(L)), "Ending index greater than length."
    assert (start <= end), "Starting index greater than ending index."

    from random import choice
    return choice(range(start, end))    # pick random element

# partitioning procedure
def qs_partition(L, start, end, pivot):
    '''(list, int, int) -> NoneType
    Partition L[start:end] in place using pivot as index and return
    new position of pivot.

    Prerequisites: 0 <= start, end <= len(L); start <= end
        start <= pivot < end.
    >>> L = [1, 5, 2, 3, 7, 4, 8]
    >>> qs_partition(L, 0, len(L), 1)
    4
    >>> L[4]
    5
    >>> sum(L[:4])
    10
    '''
    assert pivot >= start, "Pivot is lower than start index: {0} < {1}".format(pivot, start)
    assert pivot < end, "Pivot is higher than end index: {0} >= {1}".format(pivot, end)

    (L[start], L[pivot]) = (L[pivot], L[start]) # bring pivot to front

    j = start + 1  # item being considered
    while j < end and L[j] < L[start]:
        j += 1
    k = j - 1    # end of section smaller than pivot (split pointer)

    for i in range(j, end):
        if L[i] < L[start]:
            (L[i], L[k+1]) = (L[k+1], L[i])  #swap places with split pointer
            k += 1

    (L[start], L[k]) = (L[k], L[start])  #swap places with pivot
    return k
    
def quick_sort(L, start, end):
    '''(list, int, int) -> NoneType
    Sort L[start:end] in place using recursive Quick Sort algorithm.

    Prerequisites: 0 <= start, end <= len(L); start <= end.
    >>> L = [1, 5, 2, 3, 7, 4, 8]
    >>> quick_sort(L, 0, len(L))
    >>> L
    [1, 2, 3, 4, 5, 7, 8]
    '''
    if end - start < 2:
        return

    # choose pivot
    pivot = select_random(L, start, end)

    # partition around pivot
    new_pivot_position = qs_partition(L, start, end, pivot)

    # run recursions on both sides of partitioned list
    quick_sort(L, start, new_pivot_position)
    quick_sort(L, new_pivot_position+1, end)


######### MAIN BODY ##########
if __name__ == "__main__":
    #import doctest
    #doctest.testmod()

    unsorted = open('QuickSort_data.txt')
    L = []
    for x in unsorted.readlines():
        L.append(int(x))
    unsorted.close()
    
    quick_sort(L, 0, len(L))
    
    


