import sys

sys.setrecursionlimit(10**9)

S = input()

G = [[] for _ in range(len(S)+1)]

p = [0]

for i, s in enumerate(list(S)):
    if s == '(':
        G[p[-1]].append(i+1)
        p.append(i+1)
    elif s == ')':
        p.pop()
    else:
        G[p[-1]].append(i+1)

# print(G)

ans = []
flip = 0

def toggle(s: str):
    if s.isupper():
        return s.lower()
    else:
        return s.upper()

def dfs(u=0, flip=0):
    global S, G, ans
    if G[u] == []:
        s = S[u-1]
        if s == '(':
            return
        ans.append(s if flip else toggle(s))

    if flip:
        for v in G[u][::-1]:
            dfs(v, abs(1-flip))
    else:
        for v in G[u]:
            dfs(v, abs(1-flip))

dfs()

print(''.join(ans))