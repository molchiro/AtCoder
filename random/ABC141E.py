N = int(input())
S = input()

def z_algorithm(s):
    """Zアルゴリズムを実装する関数

    Args:
        s (str): 入力文字列

    Returns:
        list: 各インデックスにおけるZ値のリスト
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

ans = 0

for i in range(N-1):
    z = z_algorithm(S[i:])
    # print(z)
    for j in range(i, N):
        if j-i >= z[j-i]:
            ans = max(ans, z[j-i])

print(ans)