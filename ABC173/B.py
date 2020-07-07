N = int(input())
S = [input() for _ in range(N)]
for x in ['AC', 'WA', 'TLE', 'RE']:
    print(x + ' x ' + str(S.count(x)))