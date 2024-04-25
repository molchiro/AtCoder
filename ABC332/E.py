N, D = list(map(int, input().split()))
W = list(map(int, input().split()))

def solve_01():
    global N, D
    res = set()
    tmp = [1]*D
    tmp[0] = N-D+1
    res.add(tuple(tmp))
    while True:
        


