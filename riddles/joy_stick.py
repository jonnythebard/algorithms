# https://programmers.co.kr/learn/courses/30/lessons/42860/
name = "JARRED"

from string import ascii_uppercase

l = len(ascii_uppercase)
a = ascii_uppercase


def solution(name):
    n = len(name)
    indice = []
    cost = 0

    for i, c in enumerate(name):
        c_idx = a.index(c)
        if c_idx == 0:
            continue
        cost += min(c_idx, l - c_idx)
        indice.append(i)

    current_idx = 0
    while True:
        if len(indice) == 0:
            break
        min_cost = n
        min_idx = 0
        for idx in indice:
            _cost = min(abs(current_idx - idx), n - abs(current_idx - idx))
            if _cost < min_cost:
                min_cost = _cost
                min_idx = idx
        cost += min_cost
        indice.remove(min_idx)
        current_idx = min_idx

    return cost
