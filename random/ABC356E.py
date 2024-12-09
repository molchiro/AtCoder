N = int(input())
A = list(map(int, input().split()))
A.sort()
A.append(10**18)

ans = 0
for i in range(N-1):
    a = A[i]
    prev = i
    ok = prev
    while ok+1 < N:
        ok += 1
        k = A[ok]//a
        ng = N+1

        while ng - ok > 1:
            test = (ng+ok)//2
            if A[test]//a == k:
                ok = test
            else:
                ng = test

        ans += k*(ok-prev)
        prev = ok

print(ans)