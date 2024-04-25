class Next_DP_2d:
    def __init__(self, u: int, v: int, id_el: any, transition_function) -> None:
        self._create_initial_dp = lambda: [[id_el]*v for _ in range(u)]
        self.crr = self._create_initial_dp()
        self.nxt = self._create_initial_dp()
        self.transition_function = transition_function

    def next(self):
        self.crr = self.nxt
        self.nxt = self._create_initial_dp()

    def transition(self, u: int, du: int, v: int, dv: int, x):
        # func(n, c, x=None): nが遷移先の要素、cが遷移元の要素
        self.nxt[u+du][v+dv] = self.transition_function(self.nxt[u+du][v+dv], self.crr[u][v], x)
    
# ここから下を毎回実装する
def transition_function(nxt, crr, x):
    if nxt:
        return nxt
    elif crr == None:
        return None
    else:
        return x+crr

# dp[i][j][k]: 下位iビットまで見て、Xのpopcountがj,　YのpopcountがkとなるようなXの文字列

a, b, C = list(map(int, input().split()))

lim = 60
id_el = None
ndp = Next_DP_2d(lim+1, lim+1, id_el, transition_function)
ndp.crr[0][0] = ''
for i in range(lim):
    c = C >> i & 1
    for j in range(lim):
        for k in range(lim):
            for x in range(2):
                ndp.transition(j, x, k, x^c, str(x))
    
    ndp.next()

if ndp.crr[a][b] == None:
    print(-1)
else:
    # print(ndp.crr[a][b])
    X = int(ndp.crr[a][b], 2)
    print(X, X^C)