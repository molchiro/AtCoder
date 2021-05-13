N = int(input())
A = [0]*(1000001)
for a in list(map(int, input().split())):
    A[a] += 1

# MFPF = Most Frequent Prime Factor
MFPF_n = 0
# 範囲内のすべての素数について、割り切れるようなAiがいくつ存在するか数える
# エラトステネスの篩で計算量削減
seen = [0]*(1000001)
for i in range(2, 1000001):
    if seen[i]:
        continue
    n = i
    ct = 0
    while n < 1000001:
        ct += A[n]
        seen[n] = 1
        n += i
    MFPF_n = max(MFPF_n, ct)

if MFPF_n < 2:
    print('pairwise coprime')
elif MFPF_n - A[1] < N:
    print('setwise coprime')
else:
    print('not coprime')