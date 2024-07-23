from collections import defaultdict, deque

class Tree:
    '''木構造を扱うクラス'''
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, w=1):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def farthest(self, s):
        '''node s からみて一番遠いnodeとその距離を返す'''
        dq = deque([s])
        costs = [-1] * len(self.graph)
        costs[s] = 0
        
        while dq:
            u = dq.popleft()
            c = costs[u]
            
            for v, w in self.graph[u]:
                if costs[v] != -1:
                    continue

                costs[v] = c + w
                dq.append(v)
        node, cost = max(enumerate(costs), key=lambda x: x[1])
        return node, cost
    
    def diameter(self):
        '''木の直径'''
        f1, _ = self.farthest(0)
        _, w2 = self.farthest(f1)   
        return w2

N = int(input())
tree = Tree()
ans = 0
for _ in range(N-1):
    A, B, C = list(map(int, input().split()))
    tree.add_edge(A-1, B-1, C)
    ans += C*2

print(ans - tree.diameter())