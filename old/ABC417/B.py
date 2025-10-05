N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for b in B:
    try:
        A.remove(b)
    except:
        pass
print(*A)