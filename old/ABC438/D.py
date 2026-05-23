N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [c-b for b, c in zip(B, C)]
E = [0]
for d in D[::-1]:
    E.append(E[-1]+d)
E = E[::-1]
E.pop()

B_cumsum = [0]
for b in B:
    B_cumsum.append(B_cumsum[-1]+b)

C_cumsum = [0]
for c in C:
    C_cumsum.append(C_cumsum[-1]+c)


max_y = N
max_v = -10**18
max_v_list = [None]*N
for x in range(N-2, -1, -1):
    if E[x+1] > max_v:
        max_v = E[x+1]
        max_y = x
    max_v_list[x] = max_y

# print(E)
# print(max_v_list)

ans = 0
A_accum = 0
for x in range(N-2):
    A_accum += A[x]
    y = max(x+1, max_v_list[x])

    # print(x, y)
    # print(A_accum, (B_cumsum[y+1]-B_cumsum[x+1]), (C_cumsum[-1]-C_cumsum[y+1]))

    v = A_accum + (B_cumsum[y+1]-B_cumsum[x+1]) + (C_cumsum[-1]-C_cumsum[y+1])
    ans = max(ans, v)
print(ans)
