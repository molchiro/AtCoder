N, M, X = list(map(int, input().split()))
trains = []
stations = [[] for _ in range(N)]
for _ in range(M):
    A, B, S, T = list(map(int, input().split()))
    trains.append((A-1, B-1, S, T))
    stations[A-1].append((B-1, S, T))

nodes = []
for a, b, s, t in trains:
    nodes.append((a, s))

events = sorted(trains, key=lambda x: x[2])
for a, b, s, t in events:
    
    