N = int(input())
l = [input() for _ in range(N)]
M = max([len(x) for x in l])

field = [ list((x+'*'*M)[:M]) for x in l]
field = field[::-1]
field = list(map(list, zip(*field)))

for i in range(M):
    while field[i][-1] == '*':
        field[i].pop()

for i in range(M):
    print(''.join(field[i]))