N, K = list(map(int, input().split()))
treated = set()
for i in range(K):
    _ = input()
    
    treated = treated | (set(list(map(int, input().split()))))
print(len([x for x in range(N) if not x+1 in treated]))