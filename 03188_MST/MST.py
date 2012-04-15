from sys import stdin

N, M = map(int, stdin.readline().split())
graph = sorted([map(int, line.split()[::-1]) for line in stdin ])

mst_weight = 0
node = [0]*(N+1)
group = 1
for edge in graph:    # Kruskal's algorithm
    w, u, v = edge[0], edge[2], edge[1]
    if not node[u] and not node[v]:
        node[u], node[v], group = group, group, group+1

    elif not node[u] or not node[v]:
        node[u], node[v] = (node[v], node[v]) if not node[u] else (node[u], node[u])
    elif node[u] != node[v]:
        group_u, group_v = node[u], node[v]
        node = [group_u if (g == group_u or g == group_v) else g for g in node ]
    else:
        continue
    mst_weight += w

print mst_weight
