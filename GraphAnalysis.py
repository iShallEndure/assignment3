import networkx as nx

# Create a graph
traffic_graph = nx.Graph()

# Add nodes (intersections)
nodes = ["A", "B", "C", "D", "E"]
traffic_graph.add_nodes_from(nodes)

# Add edges (roads)
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "A")]
traffic_graph.add_edges_from(edges)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(traffic_graph)

# Print degree centrality of each intersection
for node, centrality in degree_centrality.items():
    print(f"Intersection {node}: Degree Centrality = {centrality}")

# Visualize the graph (optional)
import matplotlib.pyplot as plt

nx.draw(traffic_graph, with_labels=True)
plt.show()