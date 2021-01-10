N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
people.sort(key=lambda x: x[0]*2+x[1], reverse=True)
aoki = sum([x for x, y in people])

ans = 0
takahashi = 0

for i in range(N):
    ans += 1
    A, B = people[i]
    takahashi += A + B
    aoki -= A
    if takahashi > aoki:
        print(ans)
        exit()