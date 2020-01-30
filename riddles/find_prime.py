# https://programmers.co.kr/learn/courses/30/lessons/42839/

from itertools import permutations


def solution(numbers):
    _numbers = list(numbers)
    permuts = set()
    count = 0

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for i in range(len(_numbers) + 1):
        for p in permutations(_numbers, i):
            if p:
                permuts.add(int("".join(p)))

    for x in permuts:
        if is_prime(x):
            count += 1

    return count
