N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


dd = [0]*(10**6+1)

for a in A:
    # 各整数 i が N の約数かどうかを調べる
    for i in range(1, a + 1):
        # √N で打ち切り
        if i * i > a:
            break
        
        # i が N の約数でない場合はスキップ
        if a % i != 0:
            continue

        # i は約数である
        dd[i] += 1

        # N ÷ i も約数である (重複に注意)
        x = a//i
        if x != i:
            dd[x] += 1

ans = [1]*(10**6+1)

for j in range(10**6+1):
    for i in range(1, j + 1):
        # √N で打ち切り
        if i * i > j:
            break
        
        # i が N の約数でない場合はスキップ
        if j % i != 0:
            continue

        # i は約数である
        if dd[i] >= K:
            ans[j] = max(ans[j], i)

        # N ÷ i も約数である (重複に注意)
        x = j//i
        if x != i:
            if dd[x] >= K:
                ans[j] = max(ans[j], x)

for a in A:
    print(ans[a])