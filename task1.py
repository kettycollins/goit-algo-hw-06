import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "B"), ("A", "D"), ("B", "E"), ("B", "F"), ("C", "F"), ("D", "E")])

# Візуалізація графа
pos = nx.spring_layout(G)  # Розташування вершин
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))
