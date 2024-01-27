import networkx as nx
import matplotlib.pyplot as plt

def create_weighted_graph():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=1)
    G.add_edge('A', 'D', weight=3)
    G.add_edge('B', 'E', weight=4)
    G.add_edge('B', 'F', weight=2)
    G.add_edge('C', 'F', weight=5)
    G.add_edge('D', 'E', weight=1)
    return G

def dijkstra_shortest_paths(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        current_node = min((node for node in distances if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            potential_distance = distances[current_node] + weight

            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance

    return distances

def visualize_weighted_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

def main():
    weighted_graph = create_weighted_graph()

    start_node = 'A'
    distances = dijkstra_shortest_paths(weighted_graph, start_node)

    for target_node, distance in distances.items():
        if distance != float('infinity'):
            print(f"Найкоротший шлях між {start_node} та {target_node}: Довжина: {distance}")
            
    visualize_weighted_graph(weighted_graph)

if __name__ == "__main__":
    main()
