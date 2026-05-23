S = input()

def find_leftest(start, c):
    global S

    if start >= len(S):
        return len(S)

    for i in range(start, len(S)):
        if S[i] == c:
            return i
    
    return len(S)


A_l = find_leftest(0, 'A')
C_l = find_leftest(A_l, 'C')
ans = 0
for i in range(1, len(S)):
    if S[i] == 'B' and A_l < i:
        r = find_leftest(max(C_l, i+1), 'C')
        if A_l < i < r < len(S):
            ans += 1
            A_l = find_leftest(A_l+1, 'A')
            C_l = r+1




print(ans)