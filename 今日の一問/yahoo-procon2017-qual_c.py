N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
S_target = []
S_others = []
for i in range(N):
    if i + 1 in A:
        S_target.append(input())
    else:
        S_others.append(input())
if N == K:
    print('')
else:
    P = min(S_target, key=lambda x: len(x))
    if [s for s in S_target if not s.startswith(P)]:
        left = 0
        right = len(P)
        while right - left > 1:
            mid = (right + left)//2
            if [s for s in S_target if not s.startswith(P[:mid])] == []:
                left = mid
            else:
                right = mid
        P = P[:left]
    if [s for s in S_others if s.startswith(P)]:
        print(-1)
    else:
        left = 0
        right = len(P)
        while right - left > 1:
            mid = (right + left)//2
            if [s for s in S_others if not s.startswith(P[:mid])] == []:
                left = mid
            else:
                right = mid
        print(P[:right])
