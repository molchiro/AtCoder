N = int(input())
A = list(map(int, input().split()))
s = set()
for a in A:
    if a in s:
        s.remove(a)
    else:
        s.add(a)
print(sum(s))