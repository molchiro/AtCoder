X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

Ai = X-1
Bi = Y-1
Ci = Z-1

candidates = [[A[Ai], B[Bi], C[Ci]],
              [A[Ai-1], B[Bi], C[Ci]],
              [A[Ai], B[Bi-1], C[Ci]],
              [A[Ai], B[Bi], C[Ci-1]],
              [A[Ai-1], B[Bi-1], C[Ci]],
              [A[Ai], B[Bi-1], C[Ci-1]],
              [A[Ai-1], B[Bi], C[Ci-1]],
              [A[Ai-1], B[Bi-1], C[Ci-1]]
              ]
trigger_A = [A[Ai-1], B[Bi], C[Ci]]
trigger_B = [A[Ai], B[Bi-1], C[Ci]]
trigger_C = [A[Ai], B[Bi], C[Ci-1]]


for i in range(K):
    max_set = max(candidates, key=(lambda x: sum(x)))
    candidates.remove(max_set)
    print(candidates)
    print(sum(max_set))
    if Ai > 1 and not (trigger_A in candidates):
        Ai -= 1
        candidates.extend([
            [A[Ai-1], B[Bi], C[Ci]],
            [A[Ai-1], B[Bi-1], C[Ci]],
            [A[Ai-1], B[Bi], C[Ci-1]],
            [A[Ai-1], B[Bi-1], C[Ci-1]]
        ])
        trigger_A = min(filter((lambda x: x[0] == A[Ai]), candidates), key=(lambda x: sum(x)))
    if Bi > 1 and not (trigger_B in candidates):
        Bi -= 1
        candidates.extend([
            [A[Ai], B[Bi-1], C[Ci]],
            [A[Ai-1], B[Bi-1], C[Ci]],
            [A[Ai], B[Bi-1], C[Ci-1]],
            [A[Ai-1], B[Bi-1], C[Ci-1]]
        ])
        trigger_B = min(filter((lambda x: x[1] == B[Bi]), candidates), key=(lambda x: sum(x)))
    if Ci > 1 and not (trigger_C in candidates):
        Ci -= 1
        candidates.extend([
            [A[Ai], B[Bi], C[Ci-1]],
            [A[Ai], B[Bi-1], C[Ci-1]],
            [A[Ai-1], B[Bi], C[Ci-1]],
            [A[Ai-1], B[Bi-1], C[Ci-1]]
        ])
        trigger_C = min(filter((lambda x: x[2] == C[Ci]), candidates), key=(lambda x: sum(x)))

