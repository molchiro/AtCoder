N, M = map(int, input().split())
friendships = [list(map(int, input().split())) for i in range(M)]
friends_list = [[]for i in range(N)]

for f in friendships:
    friends_list[f[0]-1].append(f[1]-1)
    friends_list[f[1]-1].append(f[0]-1)

for i in range(N):
    friends = friends_list[i]
    friends_friends = set()
    for f in friends:
        friends_friends |= set(friends_list[f])
    friends_friends -= set([i] + friends)
    print(len(friends_friends))
