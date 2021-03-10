N = int(input())
A = list(map(int, input().split()))
A_ct = [0]*401
for a in A:
    A_ct[a+200] += 1

ans = 0
for i in range(-200, 201):
    for j in range(i, 201):
        ans += (j-i)**2*A_ct[j+200]*A_ct[i+200]

print(ans)