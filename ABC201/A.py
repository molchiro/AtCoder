A, B, C = list(map(int, input().split()))
if B-A == C-B or C-A == B-C or C-A == A-B:
    print('Yes')
else:
    print('No')