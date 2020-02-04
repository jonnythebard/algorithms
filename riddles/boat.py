# https://programmers.co.kr/learn/courses/30/lessons/42885

people = [70, 80, 50]
limit = 100


def solution(people, limit):
    _people = sorted(people)
    switch = True
    count = 0
    buffer = 0
    front_p = p = 0
    rear_p = len(people)

    while front_p != rear_p:
        w = _people[p]
        if buffer + w > limit:
            if not switch and _people[front_p] + _people[p] > limit:
                count += 1
                rear_p -= 1
                p = rear_p
                continue
            else:
                buffer = 0
                count += 1

        buffer += _people[p]

        if switch:
            rear_p -= 1
            p = rear_p
            switch = False
        else:
            front_p += 1
            p = front_p
            switch = True

    if buffer:
        count += 1

    return count
