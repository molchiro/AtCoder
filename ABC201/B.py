N = int(input())
mountains = []
for _ in range(N):
    S, T = input().split()
    mountains.append((S, int(T)))
mountains.sort(key=lambda x: x[1])
print(mountains[-2][0])