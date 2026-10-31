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


from collections import deque

class Tree:
    '''0-indexedの木構造を扱うクラス'''

    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self._diameter = None
        self._centroids = None

    def add_edge(self, u, v, w=1):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
        self._diameter = None
        self._centroids = None

    def farthest(self, s):
        '''sから最も遠い頂点と距離を返す'''
        dist = [None] * self.n
        dist[s] = 0
        stack = [(s, -1)]

        while stack:
            u, p = stack.pop()

            for v, w in self.graph[u]:
                if v == p:
                    continue
                dist[v] = dist[u] + w
                stack.append((v, u))

        return max(
            range(self.n),
            key=lambda v: dist[v]
        ), max(dist)

    def diameter(self):
        '''木の直径（辺重みは非負）'''
        if self._diameter is None:
            u, _ = self.farthest(0)
            _, self._diameter = self.farthest(u)

        return self._diameter

    def centroids(self):
        '''木の重心をすべて返す'''
        if self._centroids is None:
            n = self.n
            parent = [-1] * n
            order = [0]
            parent[0] = 0

            for u in order:
                for v, _ in self.graph[u]:
                    if v == parent[u]:
                        continue
                    parent[v] = u
                    order.append(v)

            size = [1] * n
            centroids = []

            for u in reversed(order):
                mx = n - size[u]

                for v, _ in self.graph[u]:
                    if v == parent[u]:
                        continue
                    size[u] += size[v]
                    mx = max(mx, size[v])

                if mx * 2 <= n:
                    centroids.append(u)

            self._centroids = sorted(centroids)

        return self._centroids

    def centroid(self):
        '''木の重心を1つ返す'''
        return self.centroids()[0]
