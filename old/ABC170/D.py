from collections import Counter
 
N = int(input())
A_raw = Counter(list(map(int, input().split())))
A = [x[0] for x in A_raw.items() if x[1] == 1]
A.sort()
B = [x[0] for x in A_raw.items() if x[1] > 1]
B.sort()
seen = [0]*(1000000+1)
for b in B:
    if seen[b] == 0:
        x = b
        j = 1
        while x <= 1000000:
            seen[x] = 1
            j += 1
            x = b*j
ans = 0
for a in A:
    if seen[a] == 0:
        ans += 1
        x = a
        j = 1
        while x <= 1000000:
            seen[x] = 1
            j += 1
            x = a*j
print(ans)
