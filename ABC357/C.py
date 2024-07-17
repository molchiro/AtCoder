N = int(input())

def c(level):
    if level == 0:
        return [['#']]
    
    res = []
    prev = c(level-1)
    # print(prev)
    prev3 = [ p[:]*3 for p in prev]
    # print(prev3)
    p3l = len(prev3)
    for i in range(len(prev3[0])):
        res.append(prev3[i%p3l][:])
    
    for h in range(p3l):
        for w in range(p3l):
            res[h+p3l][w+p3l] = '.'
    return res
    
# print(c(N))
for row in c(N):
    print(''.join(row))

