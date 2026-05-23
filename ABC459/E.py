from atcoder.modint import Modint

mod = 998244353

# https://algo-logic.info/combination/
fact_inv = [None]*10**7
inv = [None]*10**7
fact_inv[0] = 1
fact_inv[1] = 1
inv[1] = 1
for i in range(2, 10**7):
    inv[i] = mod - inv[mod%i] * (mod // i) % mod
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod

def nCk(n, k):
    ans = 1
    for i in range(n, n-k, -1):
        ans *= i
        ans %= mod
    return ans * fact_inv[k] % mod

N = int(input())
P = [-1] + list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

nodes = [(k, 1) for k in C]

Q = [0]*N
for p in P[1:]:
    Q[p] += 1
# print(Q)

stack = []
for i in range(N):
    if Q[i] == 0:
        stack.append(i)

# print(stack)
# print(nodes)

while stack:
    i = stack.pop()

    k, n = nodes[i]
    d = D[i]
    # 次ノードの処理
    # kCd通りの選び方
    tmp = 0
    if d <= k:
        tmp = nCk(k, d)
    k = max(0, k-d)
    n *= tmp
    n %= mod
    nodes[i] = (k, n)
    
    # 親に伝播
    p = P[i]
    if p == -1:
        break
    k_p, n_p = nodes[p]
    k_p += k
    n_p *= n
    n_p %= mod
    nodes[p] = (k_p, n_p)
    Q[p] -= 1
    if Q[p] == 0:
        stack.append(p)
    
    # print(stack, nodes)

print(nodes[0][1])
