from sortedcontainers import SortedList

N, M, K = list(map(int, input().split()))
T = input()

sl = SortedList()
answers = []

for _ in range(N):
    S = input()
    s = ''.join(['0' if S[i] == T[i] else '1' for i in range(K)])
    sl.add(s)
    answers.append(s)

Q = int(input())

for _ in range(Q):
    i, j = list(map(lambda x: int(x) - 1, input().split()))

    old_ans = answers[i]
    new_ans = list(old_ans)
    new_ans[j] = '0' if old_ans[j] == '1' else '1'
    new_ans = ''.join(new_ans)
    answers[i] = new_ans

    sl.discard(old_ans)
    sl.add(new_ans)

    if N == M and new_ans == '1'*K:
        print('No')        
    elif sl.bisect_right(new_ans) > M:
        print('No')
    else:
        print('Yes')
