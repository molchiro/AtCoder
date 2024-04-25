N, Q = list(map(int, input().split()))
imoss = [[] for _ in range(N)]
size = 0
accum = 0
S = set()
X = list(map(lambda x: int(x) - 1, input().split()))

for x in X:
    if x in S:
        imoss[x].append(accum)
        S.remove(x)
        size -= 1
    else:
        imoss[x].append(-accum)
        S.add(x)
        size += 1
    accum += size
    # print(imoss)

for e in S:
    imoss[e].append(accum)

# print(imoss)

print(*[sum(imos) for imos in imoss])