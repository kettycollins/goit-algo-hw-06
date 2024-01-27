import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs_recursive(graph, vertex, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(vertex)
    path = path + [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            path = dfs_recursive(graph, neighbor, visited, path)
    return path

def bfs_recursive(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    queue = deque([(start, path)])

    while queue:
        vertex, current_path = queue.popleft()
        visited.add(vertex)
        current_path = current_path + [vertex]

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, current_path))
                visited.add(neighbor)

    return current_path

# Створення графа
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "B"), ("A", "D"), ("B", "E"), ("B", "F"), ("C", "F"), ("D", "E")])

# DFS
start_node = "A"
end_node = "C"
dfs_path = dfs_recursive(G, start_node)
print(f"DFS Paths from {start_node} to {end_node}: {dfs_path}")

# BFS
bfs_paths = bfs_recursive(G, start_node)
print(f"BFS Paths from {start_node} to {end_node}: {bfs_paths}")

# Візуалізація графа
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")
plt.show()
