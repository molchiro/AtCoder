from collections import defaultdict

S = input()


ans = 0
dd = defaultdict(int)
checked = 0
for i in range(len(S)-2):
    s2 = S[-1-i]
    s1 = S[-2-i]
    s0 = S[-3-i]
    dd[s2] += 1
    checked += 1
    if s0 == s1 and s0 != s2:
        ans += checked - dd[s0]
        # print(dd[s0], dd[s2])
        dd = defaultdict(int)
        dd[s0] = checked


print(ans)
