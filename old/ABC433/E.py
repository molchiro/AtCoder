T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    if len(set(X)) < N or len(set(Y)) < M:
        print('No')
        continue

    # 各セルが取りうる最大値を記録
    matrix = [[10**18]*M for _ in range(N)]
    for h in range(N):
        for w in range(M):
            matrix[h][w] = min(matrix[h][w], Y[w], X[h])
    
    # 各数字を置く候補を記録
    address = [[] for _ in range(N*M)]
    for h in range(N):
        for w in range(M):
            address[matrix[h][w]-1].append((h, w))

    # matrixで調べた候補地が足りているか判定
    cumsum = [0]
    for i in range(N*M):
        cumsum.append(cumsum[-1] + len(address[i]))

    f = 0
    for i in range(1, N*M+1):
        if cumsum[i] > i:
            f = 1
    if f:
        print('No')
        continue

    ans = [[None]*M for _ in range(N)]
    # 縦横一致の場所をまず確定
    seen_n = set()
    for h in range(N):
        for w in range(M):
            if X[h] == Y[w]:
                ans[h][w] = X[h]
                seen_n.add(X[h])

    # 次点で代表を一つ決める
    for n, adr in enumerate(address, 1):
        if n in seen_n:
            continue
        if len(adr) == 0:
            continue

        h, w = adr.pop()
        ans[h][w] = n
        seen_n.add(n)
        
    # 確定済みの場所を避けながら残りを下から配置
    k = 1
    for adr in address:
        for h, w in adr:
            while k in seen_n:
                k += 1
            if ans[h][w] == None:
                ans[h][w] = k
                k += 1
    
    print('Yes')
    for row in ans:
        print(*row)