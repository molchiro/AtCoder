
class Imos3D:
    def __init__(self, N, a):
        # aは https://atcoder.jp/contests/abc366/tasks/abc366_d の形式
        self.grid = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    self.grid[i+1][j+1][k+1] = a[i*N+j][k]

        """ 3次元累積和を計算 """
        for x in range(N + 1):
            for y in range(1, N + 1):
                for z in range(1, N + 1):
                    self.grid[x][y][z] += self.grid[x][y][z-1]

        for x in range(N + 1):
            for y in range(1, N + 1):
                for z in range(N + 1):
                    self.grid[x][y][z] += self.grid[x][y-1][z]

        for x in range(1, N + 1):
            for y in range(N + 1):
                for z in range(N + 1):
                    self.grid[x][y][z] += self.grid[x-1][y][z]

    """ 部分和を返す関数 """
    """ [x1, x2]のように閉区間とする"""
    def query(self, x1, y1, z1, x2, y2, z2):
        result = self.grid[x2+1][y2+1][z2+1]
        result -= self.grid[x1][y2+1][z2+1]
        result -= self.grid[x2+1][y1][z2+1]
        result -= self.grid[x2+1][y2+1][z1]
        result += self.grid[x1][y1][z2+1]
        result += self.grid[x1][y2+1][z1]
        result += self.grid[x2+1][y1][z1]
        result -= self.grid[x1][y1][z1]
        return result

N = int(input())
A = [list(map(int, input().split())) for _ in range(N*N)]

imos = Imos3D(N, A)

Q = int(input())
for _ in range(Q):
    lx, rx, ly, ry, lz, rz = list(map(lambda x: int(x) - 1, input().split()))
    print(imos.query(lx, ly, lz, rx, ry, rz))
