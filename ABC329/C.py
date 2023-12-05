N = int(input())
S = input()
ans = [0]*26
prev = ''
combo = 0
for s in S:
    o = ord(s)-ord('a')
    if s == prev:
        combo += 1
    else:
        combo = 0
    ans[o] = max(ans[o], combo+1)
    prev = s

print(sum(ans))