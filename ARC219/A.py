N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]

if N >= 2**M:
    print('No')
else:
    print('Yes')
    S.sort()
    # print(*S, sep='\n')
    from collections import deque
    dq = deque(S)

    ans = ''
    for i in range(M):
        if dq:
            n = len(dq)
            for j in range(n):
                if dq[j][i] == '1':
                    break
            else:
                j += 1
            
            l = j
            r = n-j
            if l > r:
                ans += '0'
                for _ in range(l):
                    dq.popleft()
            else:
                ans += '1'
                for _ in range(r):
                    dq.pop()

        else:
            ans += '0'        

    print(ans)