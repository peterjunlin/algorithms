def insertion_sort(lst):
    length = len(lst)
    i = 1
    while i < length:
        k = i
        key = lst[i]
        while (lst[k - 1] > key) and (k > 0):
            lst[k] = lst[k - 1]
            k = k - 1
        lst[k] = key
        i += 1

    return lst
