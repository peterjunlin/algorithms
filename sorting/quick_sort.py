def swap(lst, i, j):
    k = lst[j]
    lst[j] = lst[i]
    lst[i] = k


def partition(lst, p, q):
    k = lst[q]
    i = p - 1
    j = q - 1
    while i != j:
        if lst[i+1] > k:
            swap(lst, i+1, j)
            j -= 1
        else:
            i += 1
    swap(lst, i + 1, q)
    return i + 1


def quick_sort(lst):
    length = len(lst)
    if length == 0:
        return lst

    stack = [x for x in range(0, length + 1)]
    sp = -1
    p = 0
    q = length - 1
    sp += 1
    stack[sp] = p
    sp += 1
    stack[sp] = q

    while sp > 0:
        q = stack[sp]
        sp -= 1
        p = stack[sp]
        sp -= 1
        k = partition(lst, p, q)
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
