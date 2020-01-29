def quick_sort(S):
    """Sort the elements of queue S using the quick sort algorithm"""
    n = len(S)
    if n < 2:
        return

    # divide
    p = S[0]
    L = []
    E = []
    G = []

    while not len(S) == 0:
        if S[0] < p:
            L.append(S.pop())
        elif p < S[0]:
            G.append(S.pop())
        else:
            E.append(S.pop())

    # conquer
    quick_sort(L)
    quick_sort(G)

    # concatenate results
    while not len(L) == 0:
        S.append(L.pop())
    while not len(E) == 0:
        S.append(E.pop())
    while not len(G) == 0:
        S.append(G.pop())
