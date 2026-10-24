N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = [None]*N
for i, a in enumerate(A, start=1):
    ans[a-1] = i

print('Yes' if ans == B else 'No')