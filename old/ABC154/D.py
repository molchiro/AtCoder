from itertools import accumulate

N, K = list(map(int, input().split()))
P = list(map(lambda x: int(x) + 1, input().split()))
P_cumsum = [0] + list(accumulate(P))
print(max([P_cumsum[i+K]-P_cumsum[i] for i in range(N-K+1)])/2)