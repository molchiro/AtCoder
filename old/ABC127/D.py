N, M = list(map(int, input().split()))
dic = {}
for e in map(int, input().split()):
    if e in dic:
        dic[e] += 1
    else:
        dic[e] = 1

for i in range(M):
    B, C = map(int, input().split())
    if C in dic:
        dic[C] += B
    else:
        dic[C] = B
keys = list(dic.keys())
keys.sort(reverse=True)

res = 0

for key in keys:
    n = dic[key]
    if n < N:
        res += key*n
        N -= n
    else:
        res += key*N
        break

print(res)