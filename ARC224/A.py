T = int(input())
for _ in range(T):
    K = int(input())
    for i in range(1, 101):
        ans = K*i
        if '00' in str(ans):
            print(ans)
            break