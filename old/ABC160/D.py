import collections

N, X, Y = list(map(int, input().split()))
dists = [
        min(abs(j-i), abs(X-1-i)+1+abs(Y-1-j), abs(Y-1-i)+1+abs(X-1-j))
        for i in range(N-1) for j in range(i+1, N)
    ]
c = collections.Counter(dists)
ans = [c[K] for K in range(1,N)]
print(*ans, sep='\n')