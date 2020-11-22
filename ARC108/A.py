S, P = list(map(int, input().split()))
for i in range(1, int(P**0.5)+1):
    if P%i != 0:
        continue
    if i + P//i == S:
        print('Yes')
        break
else:
    print('No')