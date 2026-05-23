M, A, B = list(map(int, input().split()))

ok = set()
ng = set()

ans = 0
for i in range(1, M):
    for j in range(1, M):
        s3 = A*j + B*i
        s3 %= M
        s4 = A*s3 + B*j
        s4 %= M
        # print(i, j, s3, s4)

        if s3 == 0 or s4 == 0:
            # print((i, j), 'is NG')
            continue

        prepre = s3
        pre = s4



        if (prepre, pre) in ok:
            ans += 1
            # print((i, j), 'is OKK')
            continue
        if (prepre, pre) in ng:
            # print((i, j), 'is NGG')
            continue

        test = set()

        while True:
            # print((prepre, pre))
            if (prepre, pre) in test:
                ans += 1
                # print((i, j), 'is OKKK')
                ok |= test
                break

            test.add((prepre, pre))
            
            now = A*pre + B*prepre
            now %= M
            if now == 0:
                ng |= test
                break

            prepre = pre
            pre = now
    

# print('ok', ok)
# print('ng', ng)
print(ans)