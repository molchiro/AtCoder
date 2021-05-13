n, k = list(map(int, input().split()))
S = input()

for _ in range(k-1):
    S = S+S
    T = ''
    for i in range(n):
        a, b = S[2*i:2*i+2]
        if a == 'S' and b == 'R':
            T += 'R'
        elif a == 'R' and b == 'P':
            T += 'P'
        elif a == 'P' and b == 'S':
            T += 'S'
        else:
            T += a
    S = T

print(S[0])