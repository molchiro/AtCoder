def list_up_next_games(players):
    games = set()
    for p in players:
        if A[p]:
            opponent = A[p][-1] - 1
            if A[opponent][-1] - 1 == p:
                if p < opponent:
                    games.add((p, opponent))
                else:
                    games.add((opponent, p))
    return(games)

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    A[i].reverse()

games = list_up_next_games(list(range(N)))

done_games = []
days = 0
while games:
    days += 1
    players = []
    for game in games:
        done_games.append(game)
        A[game[0]].pop()
        A[game[1]].pop()
        players.append(game[0])
        players.append(game[1])
    games = list_up_next_games(players)

if len(done_games) == N*(N-1)//2:
    print(days)
else:
    print(-1)
