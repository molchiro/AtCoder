from collections import deque

class Tree:
    def __init__(self, nodes_number, paths) -> None:
        self.nodes_number = nodes_number
        self.G = [[] for _ in range(nodes_number)]
        for a, b in paths:
            self.G[a].append(b)
            self.G[b].append(a)
    
    def farthest(self, s):
        '''node s からみて一番遠いnodeとその距離を返す'''

        # dfsにより最遠nodeを探す
        dq = deque([(s, 0)])
        seen = [0]*self.nodes_number
        while dq:
            node, dist = dq.popleft()
            seen[node] = 1
            for to in self.G[node]:
                if seen[to]:
                    continue
                dq.append((to, dist+1))
        
        return node, dist

N = int(input())
PATHS = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N-1)]
tree = Tree(N, PATHS)
# 適当なnodeからの最遠nodeを求める
u, _ = tree.farthest(0)
# uからの最遠nodeとその距離を求める
v, d = tree.farthest(u)

print(d+1)