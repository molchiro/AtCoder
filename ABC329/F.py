N, Q = list(map(int, input().split()))
C = list(map(int, input().split()))
boxies = [set([x]) for x in C]
for _ in range(Q):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    if len(boxies[a]) > len(boxies[b]):
        boxies[a], boxies[b] = boxies[b], boxies[a]
    boxies[b] |= boxies[a]
    boxies[a] = set()
    print(len(boxies[b]))