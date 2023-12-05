N, T = input().split()
ans = []

def check(S, T):
    if len(S) == len(T) - 1:
        head = 0
        tail = len(T)-1
        while head < len(S) and S[head] == T[head]:
            head += 1
        while tail > head  and S[tail-1] == T[tail]:
            tail -= 1
        
        if head == tail:
            return True

    elif len(S) - 1 == len(T):
        S, T = T, S
        head = 0
        tail = len(T)-1
        while head < len(S) and S[head] == T[head]:
            head += 1
        while tail > head  and S[tail-1] == T[tail]:
            tail -= 1
        
        if head == tail:
            return True

    elif len(S) == len(T):
        ct = 0
        for s, t in zip(list(S), list(T)):
            # print(s, t)
            if s != t:
                ct += 1
        
        if ct <= 1:
            return True
    
    return False

for i in range(int(N)):
    S = input()
    if check(S, T):
        ans.append(i+1)


print(len(ans))
print(*ans)