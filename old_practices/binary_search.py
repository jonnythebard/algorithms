def binary_search(data, target, low=0, high=0, first=True):
    if first:
        high = len(data)
    mid = (low + high) // 2
    try:
        if target > data[mid]:
            binary_search(data, target, mid, high, False)
        elif target < data[mid]:
            binary_search(data, target, low, mid, False)
        else:
            return print('target:', mid)
    except RuntimeError:
        print("data not found")

list01 = list(x for x in range(0,50,3))
print(list(enumerate(list01)))
binary_search(list01, 21)