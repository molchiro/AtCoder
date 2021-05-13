N = int(input())
A = list(map(int, input().split()))
pos = []
neg = []
for a in A:
    if a >= 0:
        pos.append(a)
    else:
        neg.append(-a)

ans = 0
pos.sort()
pos_n = len(pos)
c = -pos_n+1
for i in range(pos_n):
    ans += pos[i]*c
    c += 2
neg.sort()
neg_n = len(neg)
c = -neg_n+1
for i in range(neg_n):
    ans += neg[i]*c
    c += 2
ans += sum(pos)*neg_n
ans += sum(neg)*pos_n

print(ans)