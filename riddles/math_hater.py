# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]

    for i, a in enumerate(answers):
        for j, p in enumerate(patterns):
            if a == p[i % len(p)]:
                scores[j] += 1

    answer = [i + 1 for i, s in enumerate(scores) if s == max(scores)]
    return answer
