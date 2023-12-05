from collections import deque

class Graph:
    '''グラフを扱うクラス'''
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
