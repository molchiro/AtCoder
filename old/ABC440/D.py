from bisect import bisect_left, bisect_right

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A.append(10**18)
A.append(0)
A.sort()

amounts = []
for i in range(N+1):
    amounts.append(A[i+1]-A[i]-1)
# print(amounts)

cumsum = [0]
for i in range(N+1):
    cumsum.append(cumsum[-1]+amounts[i])
# print(cumsum)

leader = [None]*(N+1)
leader[-1] = N
for i in range(N-1, -1, -1):
    if amounts[i] > 0:
        leader[i] = i
    else:
        leader[i] = leader[i+1]
# print(leader)

for _ in range(Q):
    X, Y = list(map(int, input().split()))
    # どのグループに属するところから始まるか
    idx = leader[bisect_right(A, X)-1]
    # その中の先頭をいくつ捨てるか
    trash = max(0, X-A[idx]-1)
    # 全体から見て左から何番目から始めるのか
    offset = cumsum[idx]+trash
    # それはどのグループに属するか
    g = bisect_left(cumsum, Y+offset) - 1
    # print([idx, X, A[idx], trash, offset, g])
    print(A[g]+Y+offset-cumsum[g])