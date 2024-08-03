import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
import map_data as metro
import graph_utils as gu
from collections import deque

G = nx.Graph()

edges_r, edges_b, edges_g = [], [], []
nodes_r, nodes_b, nodes_g = [], [], []
r_pos, b_pos, g_pos, pos = {}, {}, {}, {}
labels_r, labels_b, labels_g = {}, {}, {}

for i in range(10,27):
    G.add_edge(100 + i, 100 + i+1, weight = round(4*rnd.random(), 1))
    edges_r.append((100 + i, 100 + i+1))
    G.add_edge(200 + i, 200 + i+1, weight = round(3*rnd.random(), 1))
    edges_b.append((200 + i, 200 + i+1))

for i in range(10,25):
    G.add_edge(300 + i, 300 + i+1, weight = round(2*rnd.random(), 1))
    edges_g.append((300 + i, 300 + i+1))

for i in range(10,28):
    nodes_r.append(100+i)
    nodes_b.append(200+i)
    labels_r[100+i] = 100+i
    labels_b[200+i] = 200+i

for i in range(10,26):
    nodes_g.append(300+i)
    labels_g[300+i] = 300+i

plt.figure(figsize=(20,16))

G.add_edge(313, 119, weight = round(5*rnd.random(), 1))
G.add_edge(217, 120, weight = round(5*rnd.random(), 1))
G.add_edge(218, 314, weight = round(5*rnd.random(), 1))

for key in metro.red_line:
    r_pos[key] = metro.red_line[key]["pos"]
pos.update(r_pos)

for key in metro.blue_line:
    b_pos[key] = metro.blue_line[key]["pos"]
pos.update(b_pos)

for key in metro.green_line:
    g_pos[key] = metro.green_line[key]["pos"]
pos.update(g_pos)

node_options = {"edgecolors": "black", "node_size": 350}
label_options = {"font_size": "8", "font_weight": "black", "font_color": "lightgrey", "font_family": "monospace"}

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

nx.draw_networkx_edges(G, pos, edgelist=((313, 119), (217, 120), (218, 314)), width=10, alpha=0.75, edge_color="grey")
nx.draw_networkx_edges(G, r_pos, edges_r, width=10, alpha=0.5, edge_color="tab:red")
nx.draw_networkx_edges(G, b_pos, edges_b, width=10, alpha=0.5, edge_color="tab:blue")
nx.draw_networkx_edges(G, g_pos, edges_g, width=10, alpha=0.5, edge_color="tab:green")

nx.draw_networkx_nodes(G, r_pos, nodes_r, node_color="tab:red", **node_options)
nx.draw_networkx_nodes(G, b_pos, nodes_b, node_color="tab:blue", **node_options)
nx.draw_networkx_nodes(G, g_pos, nodes_g, node_color="tab:green", **node_options)

nx.draw_networkx_labels(G, b_pos, labels_b, **label_options)
nx.draw_networkx_labels(G, g_pos, labels_g, **label_options)
nx.draw_networkx_labels(G, r_pos, labels_r, **label_options)

for key in metro.red_line:
    labels_r[key] = metro.red_line[key]["name"]
for key in metro.blue_line:
    labels_b[key] = metro.blue_line[key]["name"]
for key in metro.green_line:
    labels_g[key] = metro.green_line[key]["name"]

label_options = {"font_size": "9", "font_weight": "light", "font_family": "monospace", "horizontalalignment": "left", "bbox": {"fc": "white", "alpha": 0.9, "boxstyle": "round, pad=0.5"}}
label_shift = (0.15,0.3)
for i in r_pos:
    r_pos[i] = tuple(map(lambda i, j: i + j, r_pos[i], label_shift))
nx.draw_networkx_labels(G, r_pos, labels_r, **label_options)

label_options = {"font_size": "9", "font_weight": "light", "font_family": "sans-serif", "horizontalalignment": "left", "bbox": {"fc": "white", "alpha": 0.9, "boxstyle": "round, pad=0.5"}}
label_shift = (0.15,0.3)
for i in b_pos:
    b_pos[i] = tuple(map(lambda i, j: i + j, b_pos[i], label_shift))
nx.draw_networkx_labels(G, b_pos, labels_b, **label_options)

label_options = {"font_size": "9", "font_weight": "light", "font_family": "sans-serif", "horizontalalignment": "left", "bbox": {"fc": "white", "alpha": 0.9, "boxstyle": "round, pad=0.5"}}
label_shift = (0.15,0.3)
for i in g_pos:
    g_pos[i] = tuple(map(lambda i, j: i + j, g_pos[i], label_shift))
nx.draw_networkx_labels(G, g_pos, labels_g, **label_options)

plt.title("Metro")
plt.axis("off")
plt.tight_layout()


print("Кількість вузлів (станцій)", G.number_of_nodes())
print("Кількість ребер (перегонів)", G.number_of_edges())
print("Щільність графу", nx.density(G))

G_list = nx.to_dict_of_lists(G)

# DFS manual implementation
print("\nDFS:")
gu.dfs(G_list, 218)

# BFS manual implementation
print("\nBFS")
gu.bfs(G_list, deque([218]))
print("\n")

# Dijkstra's manual implementation
print(gu.dijkstra(G, 218))

label_options = {"font_size": "8", "font_weight": "black", "font_color": "lightgrey", "font_family": "monospace"}

# DFS visualization
dfs_edges = list(nx.dfs_edges(G, source=218))
dfs_G = nx.Graph()
i = 1
for item in dfs_edges:
    dfs_G.add_edge(item[0], item[1], weight = i)
    i += 1
plt.figure(2, figsize=(20,16))
plt.title("DFS")
plt.axis("off")
labels = nx.get_edge_attributes(dfs_G, 'weight')
nx.draw_networkx_edges(dfs_G, pos, width=10, alpha=0.75, edge_color="lightgrey")
nx.draw_networkx_labels(dfs_G, pos, **label_options)
nx.draw_networkx_nodes(dfs_G, pos, node_color="tab:blue", **node_options)
nx.draw_networkx_nodes(dfs_G, pos, nodelist=[218], node_color="tab:red", **node_options)
nx.draw_networkx_edge_labels(dfs_G, pos, labels)

# BFS visualization
bfs_edges = list(nx.bfs_edges(G, source=218))
bfs_G = nx.Graph()
i = 1
for item in bfs_edges:
    bfs_G.add_edge(item[0], item[1], weight = i)
    i += 1
plt.figure(3, figsize=(20,16))
plt.title("BFS")
plt.axis("off")
labels = nx.get_edge_attributes(bfs_G, 'weight')
nx.draw_networkx_edges(bfs_G, pos, width=10, alpha=0.75, edge_color="lightgrey")
nx.draw_networkx_labels(bfs_G, pos, **label_options)
nx.draw_networkx_nodes(bfs_G, pos, node_color="tab:blue", **node_options)
nx.draw_networkx_nodes(bfs_G, pos, nodelist=[218], node_color="tab:red", **node_options)
nx.draw_networkx_edge_labels(bfs_G, pos, labels)


plt.show()