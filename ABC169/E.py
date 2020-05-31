N = int(input())
left = []
right = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    left.append(A)
    right.append(B)
left.sort()
right.sort(reverse=True)
n = (N+1)//2-1
print(right[n]-left[n]+1)