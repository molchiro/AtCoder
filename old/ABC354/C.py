from sortedcontainers import SortedSet
offset = 10**6
N = int(input())
cards = []
sc = SortedSet()
for i in range(N):
    a, c = list(map(int, input().split()))
    cards.append((a, c, i))
    sc.add(c*offset+i)

# print(sc)
cards.sort(reverse=True)
remained = [1]*N
ans = [0]*N
for i in range(N):
    a, c, idx = cards[i]
    if remained[idx]:
        ans[idx] = 1
        while sc[-1]//offset > c:
            e = sc.pop()
            remained[e%offset] = 0
    # print(a, c, idx)
    # print(ans)
    # print(sc)

print(sum(ans))
for i in range(N):
    if ans[i]:
        print(i+1, end=' ')

