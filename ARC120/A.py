N = int(input())
A = list(map(int, input().split()))
cumsum = [A[0]]
for i in range(N-1):
    cumsum.append(cumsum[i]+A[i+1])
S = 0
max_el = 0
for i in range(N):
    S += cumsum[i]
    max_el = max(max_el, A[i])
    print(S+max_el*(i+1))