N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
solved = []
scores = [i+1 for i in range(N)]
for j in range(N):
    S = input()
    solved.append(S)
    for i in range(M):
        if S[i] == 'o':
            scores[j] += A[i]
top = max(scores)



for i, score in enumerate(scores):
    if score == top:
        print(0)
        continue

    unsolved = []
    for j, s in enumerate(solved[i]):
        if s == 'x':
            unsolved.append(A[j])
    unsolved.sort(reverse=True)
    tmp = 0
    for j, x in enumerate(unsolved):
        tmp += x
        if score+tmp > top:
            print(j+1)
            break
