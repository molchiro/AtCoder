N, M, K = list(map(int, input().split()))
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

n = 0
while H and B:
    if H[-1] <= B[-1]:
        n += 1
        H.pop()
        B.pop()
    else:
        H.pop()

print('Yes' if n >= K else 'No')