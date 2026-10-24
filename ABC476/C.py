N = int(input())
A = list(map(int, input().split()))
B = [A[0], A[1], A[2]]
B.sort(reverse=True)
print(B[-1])
for i in range(3, N):
    B.append(A[i])
    B.sort(reverse=True)
    B.pop()
    print(B[-1])
