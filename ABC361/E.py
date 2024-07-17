from collections import defaultdict, deque

class TreeWithWeight:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def farthest(self, start):
        dq = deque([start])
        weight = [-1] * len(self.graph)
        weight[start] = 0
        
        while dq:
            u = dq.popleft()
            w_u = weight[u]
            
            for v, w in self.graph[u]:
                if weight[v] != -1:
                    continue

                weight[v] = w_u + w
                dq.append(v)

        f_node = -1
        f_weight = 0

        for i, w in enumerate(weight):
            if w > f_weight:
                f_weight = w
                f_node = i    
        return f_node, f_weight
    
    def tree_diameter(self):
        f1, _ = self.farthest(0)
        _, w2 = self.farthest(f1)   
        return w2

N = int(input())
TWW = TreeWithWeight()
ans = 0
for _ in range(N-1):
    A, B, C = list(map(int, input().split()))
    TWW.add_edge(A-1, B-1, C)
    ans += C*2

print(ans - TWW.tree_diameter())