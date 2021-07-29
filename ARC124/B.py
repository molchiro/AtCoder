N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

ans = set()
for b in B:
    x = A[0]^b
    if sorted([a^x for a in A]) == B:
        ans.add(x)

print(len(ans))
print(*sorted(list(ans)), sep='\n')