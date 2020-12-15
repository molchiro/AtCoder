N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
A_ = []
prev = 0
for a in A:
    A_.append(a-prev-1)
    prev = a
A_.append(N-prev)
A_ = [x for x in A_ if x > 0]
if A_ == []:
    print(0)
    exit()
k = min(A_)
ans = 0
for a_ in A_:
    ans += (a_+k-1)//k
print(ans)