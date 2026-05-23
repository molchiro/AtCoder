Q = int(input())
playing = 0
volume = 0
for _ in range(Q):
    A = int(input())
    if A == 1:
        volume += 1
    elif A == 2:
        volume -= 1
        volume = max(volume, 0)
    else:
        playing = (playing+1)%2
    
    print('Yes' if playing and volume >= 3 else 'No')