N = int(input())
A = list(map(int, input().split()))
A_mod_n = [0]*200
for a in A:
    A_mod_n[a%200] += 1
ans = 0
for x in A_mod_n:
    ans += x*(x-1)//2
print(ans)