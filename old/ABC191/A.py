V, T, S, D = list(map(int, input().split()))
if V*T <= D <= V*S:
    print('No')
else:
    print('Yes')