def suc(n):
   
    DP=[1000]*2000
    S=["0"]*2000
    T=[-1]*2000
    DP[0]=1
    DP[10]=2
    DP[110]=3
    DP[1110]=4
    S[0]="1"
    S[10]="11"
    S[110]="111"
    S[1110]="1111"
    T[0]=0
    T[10]=0
    T[110]=0
    T[1110]=0

    A=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
    for i in range(2000):
        for j in range((1+i)//2):
            if DP[i]>DP[j]+DP[i-j-1]+1:
                DP[i]=DP[j]+DP[i-j-1]+1
                S[i]=S[j]+"+"+S[i-j-1]
                T[i]=1
        for j in range(len(A)):
            if A[j]<=(i+1)//2 and (i+1)%A[j]==0:
                if T[A[j]-1]==0 and T[(i+1)//A[j]-1]==0:
                    if DP[i]>=DP[A[j]-1]+DP[(i+1)//A[j]-1]+1:
                        DP[i]=DP[A[j]-1]+DP[(i+1)//A[j]-1]+1
                        S[i]=S[A[j]-1]+"*"+S[(i+1)//A[j]-1]
                        T[i]=0
                elif T[A[j]-1]==1 and T[(i+1)//A[j]-1]==1:
                    if DP[i]>=DP[A[j]-1]+DP[(i+1)//A[j]-1]+5:
                        DP[i]=DP[A[j]-1]+DP[(i+1)//A[j]-1]+5
                        S[i]="("+S[A[j]-1]+")*("+S[(i+1)//A[j]-1]+")"
                        T[i]=0
                elif T[A[j]-1]==0 and T[(i+1)//A[j]-1]==1:
                    if DP[i]>=DP[A[j]-1]+DP[(i+1)//A[j]-1]+3:
                        DP[i]=DP[A[j]-1]+DP[(i+1)//A[j]-1]+3
                        S[i]=S[A[j]-1]+"*("+S[(i+1)//A[j]-1]+")"
                        T[i]=0
                else:
                    if DP[i]>=DP[A[j]-1]+DP[(i+1)//A[j]-1]+3:
                        DP[i]=DP[A[j]-1]+DP[(i+1)//A[j]-1]+3
                        S[i]="("+S[A[j]-1]+")*"+S[(i+1)//A[j]-1]
                        T[i]=0
    # print(S[i-1])
    return len(S[n-1])

def fail(N):


    dp = ["1"*100 for _ in range(2001)]
    dp[1] = '1'
    dp[11] = '11'
    dp[111] = '111'
    dp[1111] = '1111'

    for i in range(1, 2000):
        for j in range(1, i+1):
            if i+j > 2000 and i*j > 2000:
                break

            # i + j
            if i+j <= 2000:
                if len(dp[i]) + len(dp[j]) + 1 < len(dp[i+j]):
                    dp[i+j] = dp[i] + "+" + dp[j]

            # (i)*(j)
            if i*j <= 2000:
                if eval(dp[i] + "*" + dp[j]) == i*j:
                    if len(dp[i]) + len(dp[j]) + 1 < len(dp[i*j]):
                        dp[i*j] = dp[i] + "*" + dp[j]
                elif eval("(" + dp[i] + ")" + "*" + dp[j]) == i*j:
                    if len(dp[i]) + len(dp[j]) + 3 < len(dp[i*j]):
                        dp[i*j] = "(" + dp[i] + ")" + "*" + dp[j]
                elif eval("(" + dp[j] + ")" + "*" + dp[i]) == i*j:
                    if len(dp[i]) + len(dp[j]) + 3 < len(dp[i*j]):
                        dp[i*j] = "(" + dp[j] + ")" + "*" + dp[i]
                else:
                    if len(dp[i]) + len(dp[j]) + 5 < len(dp[i*j]):
                        dp[i*j] = "(" + dp[j] + ")" + "*" +  "(" + dp[i] + ")"

    # print('ready')

    # N = int(input())
    # print(dp[N])
    return len(dp[N])


for n in range(1, 2001):
    if suc(n) != fail(n):
        print(n)
        break
        
