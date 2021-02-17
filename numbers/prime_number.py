"""Prime number is a positive natural number that has only two positive natural number divisors
 - one and the number itself."""


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    # all primes > 3 are of the form 6n ± 1
    f = 5
    n_upper_limit = int(n ** 0.5)
    while f <= n_upper_limit:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def is_prime_brute_force(x):
    """Determine if x is a prime number"""
    if x <= 1:
        return False
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True


def prime_in_range_brute(x1, x2):
    """find prime number in range(x1, x2)"""
    lst = []
    for i in range(x1, x2):
        if is_prime(i):
            lst.append(i)
    return lst


def eulers_sieve(x):
    if x < 2:
        return []

    prime_list = [2]
    first_value = 3
    working_list = [i for i in range(first_value, x, 2)]
    len_working_list = len(working_list)

    for idx_prime, p in enumerate(working_list):
        if p == 0:
            continue

        # marking elements to be sieved
        marking_list = []
        idx_working = idx_prime
        while idx_working < len_working_list:
            value_to_multi = working_list[idx_working]
            if value_to_multi > 0:
                value_to_sieve = p * value_to_multi
                idx_to_sieve = (value_to_sieve - first_value) // 2
                if idx_to_sieve >= len_working_list:
                    break
                marking_list.append(idx_to_sieve)
            idx_working += 1

        # remove marked elements
        for idx in marking_list:
            working_list[idx] = 0

        prime_list.append(p)
    return prime_list


def segmented_sieve(x):
    """segmented sieve.
    This method is not working, problem is - sieved values are still needed for next segment."""

    # Validate parameter
    if x <= 1:
        return []

    # Init local variables
    value_size_segment = 10  # size of each segment
    if x < value_size_segment:
        value_size_segment = x
    segment_list = [0] * (value_size_segment // 2)
    prime_list = []

    # Calculate number of segments
    num_segments = int(x / value_size_segment + 0.5)
    if x % value_size_segment > 0:
        num_segments += 1

    # Loop through segments
    first_value = 3  # number of first element in segment
    for idx_segment in range(0, num_segments):
        # Fill in segment
        len_segment = 0
        for idx, p in enumerate(range(first_value, first_value + value_size_segment, 2)):  # only odd number
            if p > x:
                break
            segment_list[idx] = p
            len_segment += 1
            if len_segment == value_size_segment:
                break
        last_value = segment_list[len_segment - 1]

        print("segment #{0}, length = {1}".format(idx_segment, len_segment), segment_list)  # debug
        print("prime_list = ", prime_list)  # debug

        # sieve the segment by value in prime_list
        len_prime_list = len(prime_list)
        if len_prime_list > 1:
            for idx_p, p in enumerate(prime_list):
                idx_to_multi = len_prime_list - 1
                while idx_to_multi >= idx_p:
                    value_to_sieve = prime_list[idx_p] * prime_list[idx_to_multi]
                    if value_to_sieve < first_value:
                        break
                    if value_to_sieve <= last_value:
                        idx_to_sieve = (value_to_sieve - first_value) // 2
                        segment_list[idx_to_sieve] = 0
                    idx_to_multi -= 1

        # sieve the segment by value in prime list multiply value in segment
        if len_prime_list > 0:
            for value_in_prime_list in prime_list:
                idx_to_multi = 0
                while idx_to_multi < len_segment:
                    if segment_list[idx_to_multi] > 0:
                        value_to_sieve = value_in_prime_list * segment_list[idx_to_multi]
                        idx_to_sieve = (value_to_sieve - first_value) // 2
                        if idx_to_sieve >= len_segment:
                            break
                        segment_list[idx_to_sieve] = 0
                    idx_to_multi += 1

        # sieve the segment by value in segment
        for idx_p, p in enumerate(segment_list):
            if p == 0:
                continue
            idx_to_multi = idx_p
            while idx_to_multi < len_segment:
                if segment_list[idx_to_multi] > 0:
                    value_to_sieve = p * segment_list[idx_to_multi]
                    idx_to_sieve = (value_to_sieve - first_value) // 2
                    if idx_to_sieve >= len_segment:
                        break
                    segment_list[idx_to_sieve] = 0
                idx_to_multi += 1

        # add remaining number in segment to prime_list
        for p in segment_list:
            if p != 0:
                prime_list.append(p)

        # Go to next segment
        first_value += value_size_segment

    prime_list = [2] + prime_list
    return prime_list


if __name__ == '__main__':
    assert not is_prime(-2)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(20)
    assert not is_prime(21)
    #
    # assert prime_in_range_brute(-10, 10) == [2, 3, 5, 7]
    #
    # print(prime_in_range_brute(1000, 1100))
    # print(prime_in_range_brute(10000, 10100))
    # print(prime_in_range_brute(100000, 100100))
    # print(prime_in_range_brute(1000000, 1000100))
    # print(prime_in_range_brute(10000000, 10000100))
    print("Primes in range of (100000000, 100000100)", prime_in_range_brute(100000000, 100000100))

    r = 1000
    print("Brute force divide ------- ", prime_in_range_brute(0, r))
    # print("Method 2: ", prime_list_before(r))
    print("Euler's Sieve ------------ ", eulers_sieve(r))
