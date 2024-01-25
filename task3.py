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

def dijkstra_shortest_paths(graph, source):
    shortest_paths = dict(nx.single_source_dijkstra_path(graph, source))
    length_paths = nx.single_source_dijkstra_path_length(graph, source)
    return shortest_paths, length_paths

def visualize_weighted_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def main():
    weighted_graph = create_weighted_graph()

    # Знаходження найкоротших шляхів та їх довжин
    start_node = 'A'
    shortest_paths, length_paths = dijkstra_shortest_paths(weighted_graph, start_node)

    # Вивід результатів
    for target_node, path in shortest_paths.items():
        if start_node != target_node:
            distance = length_paths[target_node]
            print(f"Найкоротший шлях між {start_node} та {target_node}: {path}, Довжина: {distance}")

    # Візуалізація графа
    visualize_weighted_graph(weighted_graph)

if __name__ == "__main__":
    main()