N, K, C = list(map(int, input().split()))
S = input()
cal = ['' for i in range(N)]
Q = []
for i in range(N):
    if S[i] == 'x':
        cal[i] = 'x'
    else:
        Q.append(i)

ans = []
for q in Q:
    # q+1日目を休んだ場合に成立するかを調べて背理法を使う
    temp = cal[:]
    temp[q] = 'x'
    total = 0
    i = 0
    # 貪欲に出社
    while total < K and i < N:
        if temp[i] == 'x':
            i += 1
        else:
            total += 1
            i += C + 1
    # 出社日数が足りないなら、q+1日目は必ず出社
    if total < K:
        ans.append(q+1)
        for j in range(max(0, q-C), min(N, q+C)):
            cal[j] = 'x'
        cal[q] = 'o'
if len(ans) > 0:
    print(*ans, sep='\n')
    