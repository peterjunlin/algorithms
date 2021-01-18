# Merge sort algorithm
# Sorting by merging neighbor sorted-groups.

def merge(lst, m1, n1, m2, n2):
    # Copy two groups.
    lst1 = list(lst[m1:n1+1])
    lst2 = list(lst[m2:n2+1])

    # Merge two groups
    k0 = m1
    k1 = 0
    k2 = 0
    len1 = len(lst1)
    len2 = len(lst2)
    while (k1 < len1) and (k2 < len2):
        if lst1[k1] < lst2[k2]:
            lst[k0] = lst1[k1]
            k1 += 1
        else:
            lst[k0] = lst2[k2]
            k2 += 1
        k0 += 1

    # Merge remaining elements.
    while k1 < len1:
        lst[k0] = lst1[k1]
        k1 += 1
        k0 += 1
    while k2 < len2:
        lst[k0] = lst2[k2]
        k2 += 1
        k0 += 1


def merge_sort(lst):
    length = len(lst)
    interval = 1

    # Loop to merge, interval as 1, 2, 4, 8, ...
    while interval < length:
        # Loop to merge two adjacent groups
        m1 = 0
        n1 = m1 + interval - 1
        if n1 >= length:
            n1 = m1
        m2 = m1 + interval
        n2 = n1 + interval
        if n2 >= length:
            n1 = m2
        while m1 < length:
            # Get range of two groups to be merged.
            n1 = m1 + interval - 1
            if n1 >= length:
                break
            m2 = n1 + 1
            if m2 >= length:
                break
            n2 = m2 + interval - 1
            if n2 >= length:
                n2 = length - 1
            # Merge two groups.
            merge(lst, m1, n1, m2, n2)
            # Go to next two groups.
            m1 += interval * 2
        # Go to next interval.
        interval *= 2
    return lst


# lst0 = [5, 4, 3, 2, 1]
# merge_sort(lst0)
# print(lst0)
