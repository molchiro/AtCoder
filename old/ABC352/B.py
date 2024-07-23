S = input()
T = input()
idx = 0
ans = []
for i, t in enumerate(T):
    if t == S[idx]:
        ans.append(i+1)
        idx += 1
    if idx >= len(S):
        break

print(*ans)