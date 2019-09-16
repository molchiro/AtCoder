import collections

N = int(input())
V = list(map(int, input().split()))
Ve = V[::2]
Vo = V[1::2]

Ve_common = collections.Counter(Ve).most_common(2)
Vo_common = collections.Counter(Vo).most_common(2)
if len(set(V)) == 1:
    print(N//2)
elif Ve_common[0][0] != Vo_common[0][0]:
    print(N - Ve_common[0][1] - Vo_common[0][1])
else:
    print(min(N - Ve_common[1][1] - Vo_common[0][1], N - Ve_common[0][1] - Vo_common[1][1]))