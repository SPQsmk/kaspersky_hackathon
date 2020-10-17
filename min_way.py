class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] | w < dist[v]:
                    dist[v] = dist[u] | w

        return [dist[k] for k in range(self.V)]


nodes_count_str, rows_count_str = input().split()
n, m = int(nodes_count_str), int(rows_count_str)

g = Graph(n)

for _ in range(m):
    str_data = input().split()
    first_node = int(str_data[0])
    second_node = int(str_data[1])
    delay = int(str_data[2])
    g.addEdge(first_node - 1, second_node - 1, delay)

node_a_str, node_b_str = input().split()
node_a, node_b = int(node_a_str), int(node_b_str)
min_weights = g.BellmanFord(first_node - 1)
min_way = min_weights[node_b - 1]

if min_way == float('Inf'):
    print(-1)
else:
    print(min_way)
