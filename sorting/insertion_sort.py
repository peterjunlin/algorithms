# Insertion sort algorithm

def insertion_sort(lst):
    # Sort list, by shifting and inserting elements to sorted position.

    # init
    length = len(lst)

    # Loop through the list from left to right, insert the element to sorted position
    i = 1  # index of next element to be sorted
    while i < length:
        k = i  # index after the sorted group
        key = lst[i]

        # loop backward through sorted group to find the position for current element
        while (lst[k - 1] > key) and (k > 0):
            lst[k] = lst[k - 1]  # shift to right
            k = k - 1
        lst[k] = key  # set current element to the position

        # go to next element
        i += 1

    return lst
