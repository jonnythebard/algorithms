play_list = [2, 3, 1, 4] * 2
listen_time = 3

encoded = "/".join(["o"*time for time in play_list])

l = len(encoded)
k = listen_time
patterns = []


def counter(encoded, i, k, c=0):
    e = encoded[i:i + k + c]
    if e.count("o") == k:
        return c
    c = e.count("/")
    return counter(encoded, i, k, c)


for i in range(l - k + 1):
    c = counter(encoded, i, k)
    patterns.append(encoded[i:i+k+c])

maxx = 0
for p in patterns:
    pp = p.strip("/")
    c = pp.count("/")
    if c > maxx:
        maxx = c


print(maxx + 1)