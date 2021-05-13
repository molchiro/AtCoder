N = int(input())
prev = int(input())
for _ in range(N-1):
    now = int(input())
    if prev == now:
        print('stay')
    elif prev > now:
        print('down ' + str(prev - now))
    else:
        print('up ' + str(now - prev))
    prev = now