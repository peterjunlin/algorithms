def insertion_sort(lst):
    l = len(lst)
    i = 1
    while i < l:
        k = i
        key = lst[i]
        while (lst[k - 1] > key) and (k > 0):
            lst[k] = lst[k - 1]
            k = k - 1
        lst[k] = key
        i += 1

    return lst


def test_insertion_sort(test_case):
    result = insertion_sort(list(test_case))
    print("------")
    print(f"Result: {result}")
    print(f"Expected: {sorted(test_case)}")
    print(f"Success: {result == sorted(test_case)}")


if __name__ == "__main__":
    test_insertion_sort([])
    test_insertion_sort([1])
    test_insertion_sort([3, 1, 5, 8, 2])
    test_insertion_sort([5, 4, 3, 2, 1, 0, -1, -2])
    test_insertion_sort([-1, 0, 1, 2, 3, 4, 5, 6])
