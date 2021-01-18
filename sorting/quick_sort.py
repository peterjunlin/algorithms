# Quick sort algorithm
# Put pivot in between less-than group and more-than group.

def swap(lst, i, j):
    # swap two elements - i, j
    k = lst[j]
    lst[j] = lst[i]
    lst[i] = k


def find_pivot(lst):
    # find pivot to avoid worst scenario, by selecting middle of 3 - lst[p], lst[(p+q)//2], lst[q]

    # choose left, middle and right as pivot candidates
    p = 0
    q = len(lst) - 1
    m = (p + q) // 2

    # Find middle one by going through all combinations - pmq, pqm, qpm, mpq, mqp, qmp
    if lst[p] < lst[m]:
        if lst[m] < lst[q]:
            return m
        elif lst[p] < lst[q]:
            return q
        else:
            return p
    else:
        if lst[p] < lst[q]:
            return p
        elif lst[q] < lst[m]:
            return m
        else:
            return q


def partition(lst, p, q):
    # partition list as -- [less than pivot, pivot, great than pivot]

    k = lst[q]  # Pivot, the last element
    i = p - 1  # tail index of less-than group
    j = q - 1  # tail index of not-sorted group

    # Loop to partition until not-sorted group exhausted
    while i != j:
        if lst[i+1] > k:
            swap(lst, i+1, j)  # swap great-than element to the right.
            j -= 1
        else:
            i += 1

    # Put the pivot in the middle of less-than group and great-than group
    swap(lst, i + 1, q)

    return i + 1  # index of pivot


def quick_sort(lst):
    # sort the list by using quick-sort algorithm.

    # Check list is not empty
    length = len(lst)
    if length == 0:
        return lst

    # push index range to stack, which will be sorted next.
    stack = [x for x in range(0, length + 1)]  # stack is used to store index range to be sorted.
    sp = -1
    p = 0
    q = length - 1
    sp += 1
    stack[sp] = p
    sp += 1
    stack[sp] = q

    # Find and move pivot to the end of list
    k = find_pivot(lst)
    swap(lst, k, q)

    # Loop to sort, until stack is empty
    while sp > 0:
        # Pop index range to be sorted
        q = stack[sp]
        sp -= 1
        p = stack[sp]
        sp -= 1

        # partition list as -- [less than pivot, pivot, great than pivot]
        k = partition(lst, p, q)

        # Push index range of both left and right group to stack
        if p < k - 1:
            sp += 1
            stack[sp] = p
            sp += 1
            stack[sp] = k - 1
        if k + 1 < q:
            sp += 1
            stack[sp] = k + 1
            sp += 1
            stack[sp] = q

    return lst
