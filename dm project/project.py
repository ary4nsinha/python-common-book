import networkx as nx
import matplotlib.pyplot as plt

def eulerian_path(graph):
    # Check if the graph has an Eulerian path
    odd_degree_nodes = [node for node, degree in graph.degree() if degree % 2 != 0]
    if len(odd_degree_nodes) != 2:
        print("The graph does not have an Eulerian path.")
        return None
    
    # Find the Eulerian path
    start_node = odd_degree_nodes[0]
    path = list(nx.eulerian_path(graph, source=start_node))
    return path

def visualize_graph(graph, path=None):
    pos = nx.spring_layout(graph)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1200)
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title("Graph Visualization")
    plt.show()

# Example graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])

# Visualize the graph
visualize_graph(G)

# Find and visualize Eulerian path
eulerian_path_result = eulerian_path(G)
if eulerian_path_result:
    print("Eulerian Path:", eulerian_path_result)
    visualize_graph(G, path=[node for node, _ in eulerian_path_result] + [eulerian_path_result[-1][1]])
