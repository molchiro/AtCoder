S, L ,R = list(map(int, input().split()))
if S < L:
    print(L)
elif S > R:
    print(R)
else:
    print(S)