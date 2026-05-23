S = list(input())
T = list(input())

ans = 0

while S and T:
    # print(ans, S, T)
    if S[-1] == T[-1]:
        S.pop()
        T.pop()
    elif S[-1] == 'A':
        S.pop()
        ans += 1
    elif T[-1] == 'A':
        T.pop()
        ans += 1
    else:
        break

if len(S) == 0 and len(T) == 0:
    print(ans)
elif S:
    if set(S) == set(['A']):
        print(ans+len(S))
    else:
        print(-1)
elif T:
    if set(T) == set(['A']):
        print(ans+len(T))
    else:
        print(-1)
else:
    print(-1) 
