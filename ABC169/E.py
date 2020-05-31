N = int(input())
left = []
right = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    left.append(A)
    right.append(B)
left.sort()
right.sort(reverse=True)
if N%2 == 0:
    n = (N+1)//2-1
    A_med2 = (left[n]+left[n+1])
    B_med2 = (right[n]+right[n+1])
    print(B_med2-A_med2+1)
else:
    n = (N+1)//2-1
    print(right[n]-left[n]+1)