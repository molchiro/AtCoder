N, M = list(map(int, input().split()))
m = [0]*M
F = list(map(lambda x: int(x) - 1, input().split()))
for f in F:
    m[f] += 1

print('Yes' if max(m) == 1 else 'No')
print('Yes' if min(m) > 0 else 'No')