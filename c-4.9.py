def find_min_max(S, index=0, minnum=999, maxnum=0):

    if minnum > S[index]:
        minnum = S[index]
    if maxnum < S[index]:
        maxnum = S[index]

    if index == len(S)-1:
        return minnum, maxnum
    else:
        target = find_min_max(S, index+1, minnum, maxnum)
        
    return target

list01 = [4,6,2,9,7,10]
print(find_min_max(list01))