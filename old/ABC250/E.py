from random import randrange


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

table = dict()
for x in set(A+B):
    table[x] = randrange(1<<60)

def culc(array):
    res = [0]
    s = set()
    for x in array:
        if x not in s:
            res.append(res[-1]^table[x])
            s.add(x)
        else:
            res.append(res[-1])
    return res

hash_A = culc(A)
hash_B = culc(B)

Q = int(input())
for _ in range(Q):
    x, y = list(map(int, input().split()))
    print('Yes' if hash_A[x] == hash_B[y] else 'No')
    