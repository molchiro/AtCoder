from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

def f(a, b, c):
    return len(set([a, b, c])) == 3 and a+b>c and b+c>a and c+a>b

ans = 0
for a, b, c in combinations(L, 3):
    if f(a, b, c):
        ans += 1
print(ans)