T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    
    # K-1種をN枚以下で並べ切れるケース
    if N >= K-1:
        K -= 1
        ct = 0
        d = 1
        ans = 0
        while int('0' + '9'*d) - int('0' + '9'*(d-1)) < K-ct:
            tmp = (int('0' + '9'*d) - int('0' + '9'*(d-1)))
            ans += d * tmp
            # print(d, K, ans)
            ct += tmp
            d += 1
        ans += d * (K - ct)
        print(ans)
    else:

        # まずはN種を埋める
        K -= 1
        ct = 0
        d = 1
        ans = 0
        while int('0' + '9'*d) - int('0' + '9'*(d-1)) < K-ct:
            tmp = (int('0' + '9'*d) - int('0' + '9'*(d-1)))
            ans += d * tmp
            # print(d, K, ans)
            ct += tmp
            d += 1
        rem = N-ct
        ans += d * rem
        ct += rem

        # L字に敷き詰める
        M = N-1
        while M >= 1 and ct < K:
            # ct..ct+M
            tmp = 0
            ct
            last = min(ct+M, K)
            d = len(str(ct))
            # まずはすう処理
            if int('0' + '9'*d) < last:
                rem = int('0' + '9'*d) - ct
                tmp += d * rem
                ct += rem
            
            print(ct)

            while int('0' + '9'*d) - int('0' + '9'*(d-1)) < last-ct:
                tmp = (int('0' + '9'*d) - int('0' + '9'*(d-1)))
                ans += d * tmp
                # print(d, K, ans)
                ct += tmp
                d += 1
            rem = last-ct
            ans += d * rem
            ct += rem
            


            ans += 2*tmp
            M -= 1

        if ct < K:
            print(-1)
        else:
            print(ans)