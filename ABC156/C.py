N = int(input())
X_list = list(map(int, input().split()))
res = float('inf')
for i in range(101):
    tmp = sum([(X-i)**2 for X in X_list])
    res = min(res, tmp)
print(res)