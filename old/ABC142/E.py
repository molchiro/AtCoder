def min_keys(box):
    ans = 13
    for box

N, M = list(map(int, input().split()))
keys = []
for i in range(M):
    a, b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    keys.append([a, b, c])
print(keys)
boxes = [[] for i in range(N)]
for i, key in enumerate(keys):
    for c in key[2]:
        boxes[c-1][0].append(i)

print(boxes)

if [] in boxes:
    print(-1)
else:
    ans = 0
    unopend = [[boxes[:], 0]]
    while unopend:
        for x in unopend:


