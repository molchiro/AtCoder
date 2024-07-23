import dataclasses

@dataclasses.dataclass
class MyClass:
    l: int
    r: int

N = int(input())
A = list(map(int, input().split()))

# 番兵を挿入
A = [None, 0] + A + [-1, None]

d = {}
for i in range(N+2):
    d[A[i+1]] = MyClass(A[i], A[i+2])

Q = int(input())
for _ in range(Q):
    t, *args =list(map(int, input().split()))
    if t == 1:
        x, y = args
        r = d[x].r
        d[y] = MyClass(x, r) 
        d[x].r = y
        d[r].l = y
    else:
        x = args[0]
        l = d[x].l
        r = d[x].r
        d[l].r = r
        d[r].l = l
        
ans = []

now = d[0].r
while now > 0:
    ans.append(now)
    now = d[now].r

print(*ans)