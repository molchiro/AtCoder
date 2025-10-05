N, M = list(map(int, input().split()))
edges = set()
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    edges.add((min(A, B), max(A, B)))

from itertools import permutations

# print(edges)

ans = float('inf')
for pattern in permutations(range(N), N):
    test = set()
    for i in range(N-1):
        A, B = pattern[i:i+2]
        test.add((min(A, B), max(A, B)))
    A, B = pattern[0], pattern[-1]
    test.add((min(A, B), max(A, B)))
    ans = min(ans, len(edges.symmetric_difference(test)))


    if N == 6:
        test = set()
        A, B = pattern[0], pattern[1]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[1], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[0], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[4]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[4], pattern[5]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[5]
        test.add((min(A, B), max(A, B)))
        ans = min(ans, len(edges.symmetric_difference(test)))
    
    if N == 7:
        test = set()
        A, B = pattern[0], pattern[1]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[1], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[0], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[4]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[4], pattern[5]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[5], pattern[6]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[6]
        test.add((min(A, B), max(A, B)))
        ans = min(ans, len(edges.symmetric_difference(test)))
    
    if N == 8:
        test = set()
        A, B = pattern[0], pattern[1]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[1], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[0], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[4]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[4], pattern[5]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[5], pattern[6]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[6], pattern[7]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[7]
        test.add((min(A, B), max(A, B)))
        ans = min(ans, len(edges.symmetric_difference(test)))

        test = set()
        A, B = pattern[0], pattern[1]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[1], pattern[2]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[2], pattern[3]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[3], pattern[0]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[4], pattern[5]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[5], pattern[6]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[6], pattern[7]
        test.add((min(A, B), max(A, B)))
        A, B = pattern[4], pattern[7]
        test.add((min(A, B), max(A, B)))
        ans = min(ans, len(edges.symmetric_difference(test)))

    
print(ans)