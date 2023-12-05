N = int(input())
hours = [0]*24
for _ in range(N):
    W, X = list(map(int, input().split()))
    for i in range(24):
        if 9 <= (i+X)%24 < 18:
            hours[i] += W
    
    # print(hours)

print(max(hours))