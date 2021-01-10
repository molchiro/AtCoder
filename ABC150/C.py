N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

kaijo = [1]
for i in range(1, 9):
    kaijo.append(kaijo[i-1]*i)

A = [i+1 for i in range(N)]
ans = 0
for i in range(N):
    ai = A.index(int(P[i]))
    ans += (ai-1)*kaijo[N-i-1]
    A.remove(int(P[i]))
A = [i+1 for i in range(N)]
for i in range(N):
    ai = A.index(int(Q[i]))
    ans -= (ai-1)*kaijo[N-i-1]
    A.remove(int(Q[i]))
print(abs(ans))