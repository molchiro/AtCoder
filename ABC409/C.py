N, L = list(map(int, input().split()))
D = list(map(int, input().split()))

pos = [0]*L

if L%3 != 0:
    print(0)
    exit()

now = 0
pos[now] += 1
for d in D:
    now += d
    now %= L
    pos[now] += 1

ans = 0
l = L // 3
for i in range(l):
    ans += pos[i] * pos[i+l] * pos[i+l+l]
print(ans)
