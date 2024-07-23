N = int(input())
A = list(map(int, input().split()))

max_py_len_L = []
prev = 0
for i in range(N):
    max_py_len_L.append(min(prev+1, A[i]))
    prev = max_py_len_L[-1]

max_py_len_R = []
prev = 0
for i in range(N):
    max_py_len_R.append(min(prev+1, A[-i-1]))
    prev = max_py_len_R[-1]
max_py_len_R.reverse()

ans = 0
for i in range(N):
    ans = max(ans, min(max_py_len_L[i], max_py_len_R[i]))
print(ans)