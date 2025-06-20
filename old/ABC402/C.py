N, M = list(map(int, input().split()))
dishes = []
for _ in range(M):
    ipt = list(map(int, input().split()))
    dishes.append(ipt[1:])
B = list(map(int, input().split()))
d = {}
for i, v in enumerate(B):
    d[v] = i

dishes = [sorted([d[x] for x in dish])[-1] for dish in dishes]
dishes.sort()

# print(dishes)

idx = 0
for i in range(N):
    while idx < M and dishes[idx] <= i:
        idx += 1
    
    print(idx)