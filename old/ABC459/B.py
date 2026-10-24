N = int(input())
S = input().split()

d = [2,2,2, 3,3,3, 4,4,4, 5,5,5, 6,6,6, 7,7,7,7, 8,8,8, 9,9,9,9,]
assert len(d) == 26
ans = []
for s in S:
    ans.append(d[ord(s[0])-ord('a')])

print(''.join([str(x) for x in ans]))