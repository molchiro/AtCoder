from collections import deque

class Graph:
    '''無向グラフを扱うクラス'''
    def __init__(self, nodes_number, paths) -> None:
        self.nodes_number = nodes_number
        self.to_nodes = [[] for _ in range(nodes_number)]
        for a, b in paths:
            self.to_nodes[a].append(b)
            self.to_nodes[b].append(a)

    def farthest(self, start_node):
        '''node s からみて一番遠いnodeとその距離を返す'''

        # bfsにより最遠nodeを探す
        dq = deque([(start_node, 0)])
        seen = [0]*self.nodes_number
        seen[start_node] = 1
        while dq:
            from_node, dist = dq.popleft()
            for to_node in self.to_nodes[from_node]:
                if seen[to_node]:
                    continue
                dq.append((to_node, dist+1))
                seen[to_node] = 1

        return from_node, dist

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

