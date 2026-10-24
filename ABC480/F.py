N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)
B = S//M

ans = 0
rem = []
for a in A:
    ans += a//B
    if a%B:
        rem.append(a%B)
# rem = A

# print(ans, rem)

def matching(array, target):
    # ビット全探索でちょうどいい組み合わせを探す
    for i in range(1 << len(array)):
        accum = 0
        for j in range(len(array)):
            if i >> j & 1:
                accum += array[j]
        if accum == target:
            res = []
            for j in range(len(array)):
                if i >> j & 1:
                    continue
                res.append(array[j])
            return 1, res

    return 0, array


def greedy(array, target):
    # 小さい方から貪欲に取って、余ったものを戻す
    sorted_array = sorted(array, reverse=True)
    accum = 0
    while accum < target:
        accum += sorted_array.pop()

    return sorted_array + [accum-target]

while rem:
    # print(ans, rem)
    # input()
    f, rem = matching(rem, B)
    if f:
        continue

    ans += 1
    rem = greedy(rem, B)

print(ans)