import pytest
import random
from insertion_sort import insertion_sort

num_lists = 100
max_length = 100
lo, hi = -100, 100
sort_algorithms = [
    insertion_sort,
]


def is_sorted(lst):
    for i in range(len(lst) - 1):
        assert lst[i] <= lst[i + 1]


def generate_unsorted_list():
    random_length = random.randint(0, max_length)
    return [random.randint(lo, hi) for _ in range(random_length)]


unsorted_lists = [generate_unsorted_list() for _ in range(num_lists)]


@pytest.mark.parametrize("sort_algorithm", sort_algorithms)
@pytest.mark.parametrize("unsorted_list", unsorted_lists)
def test_sort(sort_algorithm, unsorted_list):
    is_sorted(sort_algorithm(list(unsorted_list)))
