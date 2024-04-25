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
    return max(nxt, crr+x)

# sample
L = 50
M = 50
N = 50
id_el = 0
ndp = Next_DP_2d(M+1, N+1, id_el, transition_function)
C = [i for i in range(L)]
for i in range(L):
    for j in range(M):
        for k in range(N):
            ndp.transition(j, 1, k, 1, C[i])
    
    ndp.next()