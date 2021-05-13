N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
print(sum(sorted(H)[:max(0,N-K)]))