import math


def time_complexity_comparison():
    for i in range(1, 100):
        print("N={0}, O(1)=1, O(N)={1}, O(log N)={2:.1f}, O(NlogN)={3:.1f}, O(N²)={4}, O(2ⁿ)={5}, O(N!)={6}"
              .format(i, i, math.log2(i), i * math.log2(i), i*i, math.pow(2, i), math.perm(i)))


if __name__ == '__main__':
    time_complexity_comparison()
