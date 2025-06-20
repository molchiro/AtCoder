N, M = list(map(int, input().split()))
B = list(map(int, input().split()))
W = list(map(int, input().split()))
B.sort(reverse=True)
W.sort(reverse=True)

ans = 0
w_tail = -1

# 白を何個買うか先に決める
for i in range(min(N, M)):
    if W[i] > 0 and B[i] + W[i] > 0:
        ans += B[i] + W[i]
        w_tail = i
    else:
        break

# 黒をどこまで追加で買うか決める
for i in range(w_tail+1, N):
    if B[i] > 0:
        ans += B[i]
    else:
        break

print(ans)