from collections import Counter

N = int(input())
A = list(map(int, input().split()))
i_plus_A = Counter([i + A[i] for i in range(N)])
i_minus_A = [i - A[i] for i in range(N)]
print(sum(i_plus_A[x] for x in i_minus_A))