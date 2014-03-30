def count_inversions(L, count):
    """(list of int, int) -> (list of int, int)
    Return sorted list L and incremented number of inversions count
    using divide-and-conquer recursive algorithm.
    """
    # base-case: if list is singleton, return unchanged inputs
    if len(L) == 1:
        return (L, count)

    cutoff = len(L)//2
    # run self on first half, return sorted list and count
    (first, count) = count_inversions(L[:cutoff], count)
    (second, count) = count_inversions(L[cutoff:], count)

    # return output of merge and count algorithm on two sorted halves
    return merge_count(first, second, count)

def merge_count(A, B, count):
    """(list of int, list of int, int) -> (list of int, count)
    Return tuple of merged sorted list from A and B and incremented
    count of inversions.

    Prerequisite: A and B are sorted

    >>> A = [1, 2, 5]
    >>> B = [3, 4, 6]
    >>> merge_count(A, B, 3)
    ([1, 2, 3, 4, 5, 6], 5)
    """
    a = len(A)
    b = len(B)
    i = 0
    j = 0
    C = [] # empty list to be returned

    for k in range(a+b):
        if i < a:
            if j==b or A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
                count += (a - i)
        else:
            C.append(B[j])
            j += 1
    return (C, count)

# read file into list
file = open("IntegerArray.txt")
L = []

for line in file:
    L.append(int(line))


# run counting procedure on list
(A, n) = count_inversions(L, 0)

# print total number of inversions
#print(A)
print("{0} total inversions found".format(n))
