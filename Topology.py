import networkx as nx
import matplotlib.pyplot as plt
from nltk.metrics import edit_distance

def create_topology(words, threshold):
    G = nx.Graph()
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i < j:
                distance = edit_distance(word1, word2)
                if distance <= threshold:
                    G.add_edge(word1, word2, weight=1 / (distance + 1))
    return G

def plot_topology(G, canvas):
    pos = nx.spring_layout(G)
    labels = {node: node for node in G.nodes()}

    # Draw nodes as black circles with black outlines and dark blue edges
    nx.draw(G, pos, labels=labels, node_size=2000, node_color="white", font_size=10, font_color="black",
            edge_color="darkblue", width=2, edgecolors="black")  # Adjust width for line thickness

    # Customize edge labels
    edge_labels = {(u, v): f"{1 / d:.2f}" for u, v, d in G.edges(data='weight')}
    pos_edge_labels = {key: ((pos[key[0]][0] + pos[key[1]][0]) / 2,
                             (pos[key[0]][1] + pos[key[1]][1]) / 2) for key in edge_labels}
    nx.draw_networkx_edge_labels(G, pos_edge_labels, edge_labels=edge_labels, font_color="black", label_pos=0.3)

    canvas.draw()
