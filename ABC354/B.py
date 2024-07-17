N = int(input())
winner = 0
players = []
for _ in range(N):
    S, C = input().split()
    players.append((S, int(C)))
    winner += int(C)
    winner %= N
players.sort()
print(players[winner][0])