from sys import stdin
from collections import defaultdict, deque

class Graph(object):
    def __init__(self, N, M):
        self.N, self.M = N, M
        self.g = defaultdict(set)

    def add_edge(self, u, v):
        self.g[u].add(v)
        self.g[v].add(u)

    def is_connected(self):
        return self.M == self.N-1 and self._check_connectivity()

    def _check_connectivity(self):
        """Apply breadth-first search to check for connectivity."""
        Q = deque([self.g.keys()[0]])
        visited_nodes = set()
        while Q:
            u = Q.pop()
            visited_nodes.add(u)
            Q.extend([v for v in self.g[u] if not (v in visited_nodes)])
        return len(visited_nodes) == self.N


if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    if M == N-1:
        G = Graph(N, M)
        for uv in stdin.readlines():
            G.add_edge(*map(int, uv.split())) 
        print 'YES' if G.is_connected() else 'NO'
    else:
        print 'NO'
