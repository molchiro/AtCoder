
import os
import subprocess

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "E.py")

from random import randint, shuffle

while True:
    N = randint(1, 2000 + 1)
    M = randint(1, 200000//N + 1)
    print(N, M)
    matrix = [[None]*M for _ in range(N)]
    pattern = [(h, w) for h in range(N) for w in range(M)]
    shuffle(pattern)
    for i, (h, w) in enumerate(pattern, 1):
        matrix[h][w] = i
    
    X = []
    for h in range(N):
        X.append(max(matrix[h]))
    Y = []
    for w in range(M):
        Y.append(max([row[w] for row in matrix]))

    process = subprocess.Popen(
        ["python3", FILE], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    process.stdin.write('1\n')
    process.stdin.write(str(N)+' '+str(M)+'\n')
    process.stdin.write(' '.join([str(e) for e in X])+'\n')
    process.stdin.write(' '.join([str(e) for e in Y])+'\n')
    process.stdin.flush()
    res_bool = process.stdout.readline().strip()
    if res_bool != 'Yes':
        print(res_bool)
        print('Noooooooo')
        break
    res = []
    for _ in range(N):
        row = process.stdout.readline().strip().split()
        res.append(list(map(int, row)))
    
    X_ = []
    for h in range(N):
        X_.append(max(res[h]))
    Y_ = []
    for w in range(M):
        Y_.append(max([row[w] for row in res]))
    
    if not (X == X_ and Y == Y_):
        print('found')
        break
