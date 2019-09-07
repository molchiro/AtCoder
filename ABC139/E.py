def list_up_next_games(players):
    games = set()
    for p in players:
        opponent = A[p] - 1
        if A[opponent] - 1 == p:
            if i < opponent:
                games.add((p, opponent))
            else:
                games.add((opponent, p))
    return(games)


N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    A[i].reverse()

remain_games = []
for i in range(N):
    for j in range(i+1,N):
        remain_games.append((i,j))

games = list_up_next_games(list(range(N)))

days = 0
while games:
    days += 1
    players = []
    for game in games:
        remain_games.remove(game)
        A[game[0]].pop()
        A[game[1]].pop()
        players.append(game[0])
        players.append(game[1])
    games = list_up_next_games(players)
print(days)