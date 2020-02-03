# https://programmers.co.kr/learn/courses/30/lessons/42860/
name = "JARED"


def solution(name):
    count = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {}
    indexes = []
    current_idx = 0
    n = len(name)

    # map vertical costs
    for i in range(len(alpha)):
        d[alpha[i]] = min(i, 26 - i)

    # calculate vertical costs
    for i in range(n):
        num = d[name[i]]
        count += num
        if num != 0:
            indexes.append(i)

    # calculate horizontal costs
    while True:
        if len(indexes) == 0:
            break
        min_dist = 99
        min_idx = 0
        for idx in indexes:
            dist = min(abs(idx - current_idx), n - abs(idx - current_idx))
            if dist < min_dist:
                min_dist = dist
                min_idx = idx
        count += min_dist
        indexes.remove(min_idx)
        current_idx = min_idx

    return count
