S = input()
L = len(S)

A = [ '0' if i%2 == 0 else '1' for i in range(L)]
ans = 0
for s, a in zip(S,A):
    if s == a: ans += 1
            
print(min(ans,L-ans))
