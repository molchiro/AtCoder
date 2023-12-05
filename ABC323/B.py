N = int(input())
players = []
for i in range(N):
    S = input()
    players.append((i+1, S.count('o')))

players.sort(key=lambda x:(-x[1], x[0]))

print(*[n for n, c in players], sep=' ')