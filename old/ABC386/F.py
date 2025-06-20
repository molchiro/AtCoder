from collections import deque

K = int(input())
S = input()
T = input()
sl = len(S)
tl = len(T)

def solve():
    dq = deque()
    dq.append((0, 0, 0))

    seen = set()

    while dq:
        i, j, k = dq.popleft()
        if (i, j) in seen:
            continue
        seen.add((i, j))
        # print(i, j, k)

        if k > K:
            continue

        if i == sl and j == tl:
            return True

        if i < sl and j < tl and S[i] == T[j]:
            # なにもしない
            dq.appendleft((i + 1, j + 1, k))
        else:
            # 操作を加える場合
            if i < sl:
                # Sの削除操作またはTの追加
                dq.append((i + 1, j, k + 1))
            if j < tl:
                # Tの削除操作またはSの追加
                dq.append((i, j + 1, k + 1))
            if i < sl and j < tl:
                # S[i]とT[j]を合わせる操作
                dq.append((i + 1, j + 1, k + 1))

    return False

print('Yes' if solve() else 'No')
