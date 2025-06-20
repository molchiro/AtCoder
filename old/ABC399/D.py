T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] + list(map(int, input().split())) + [-1]
    d = [[] for _ in range(N)]
    for i, a in enumerate(A):
        if 1 <= a <= N:
            d[a-1].append(i)
    
    ans = 0
    seen = set()
    # print(d)
    for i in range(N):
        l, r = d[i]

        if l + 1 == r:
            continue

        # print(i+1, A[l-1], A[l+1], A[r-1], A[r+1])
        if A[l-1] == A[r-1] and (min(i, A[l-1]-1), max(i, A[l-1]-1)) not in seen:
            ans += 1
            seen.add((min(i, A[l-1]-1), max(i, A[l-1]-1)))
        elif A[l-1] == A[r+1] and  (min(i, A[l-1]-1), max(i, A[l-1]-1)) not in seen:
            ans += 1
            seen.add((min(i, A[l-1]-1), max(i, A[l-1]-1)))
        elif A[l+1] == A[r+1] and  (min(i, A[l+1]-1), max(i, A[l+1]-1)) not in seen:
            ans += 1
            seen.add((min(i, A[l+1]-1), max(i, A[l+1]-1)))
        elif A[l+1] == A[r-1] and l+1 != r-1 and l+2 != r-1 and (min(i, A[l+1]-1), max(i, A[l+1]-1)) not in seen:
            ans += 1
            seen.add((min(i, A[l+1]-1), max(i, A[l+1]-1)))
    
    print(ans)
    # input()