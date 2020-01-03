# peg = {0:[1,2,3,4,5], 1:[], 2:[]}

def move(n, peg):
    if n % 2 == 1:
        if n in peg[0]:
            disk = peg[0].pop(0)
            peg[1].insert(0, disk)
        elif n in peg[1]:
            disk = peg[1].pop(0)
            peg[2].insert(0, disk)
        else:
            disk = peg[2].pop(0)
            peg[0].insert(0, disk)

    else:
        if n in peg[0]:
            disk = peg[0].pop(0)
            peg[2].insert(0, disk)
        elif n in peg[1]:
            disk = peg[1].pop(0)
            peg[0].insert(0, disk)
        else:
            disk = peg[2].pop(0)
            peg[1].insert(0, disk)
    print()
    print(peg)

def fractal(n, peg):
    if n == 0:
        return
    else:
        fractal(n-1, peg)
        move(n, peg)
        fractal(n-1, peg)

def hanoi(n):
    peg = {0:list(range(1, n+1)), 1:list(), 2:list()}
    print(peg)
    fractal(n, peg)

hanoi(4)

# print(peg)
# fractal(len(peg[0]))