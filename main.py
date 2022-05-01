#from graph import Graph
import time
import WLalg
import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


'''A = np.matrix([[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])
B = np.matrix([[0, 0, 1],
              [0, 0, 1],
              [1, 1, 0]])
times = []
G = nx.from_numpy_array(A, create_using=nx.DiGraph())
H = nx.from_numpy_array(B, create_using=nx.DiGraph())
'''
data = dict()
for size in range(30, 300):
    G = nx.path_graph(size)
    H = G.copy()
    data.update({size:[]})
    for i in range(20):
        start = time.time()
        WLalg.wlalg(G, H)
        end = time.time()
        data[size].append(end-start)
print(data)
'''
with open('data.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=';')
    for key in data.keys():
        w.writerow([key]+data[key])
'''
''' for drawing graph
layout = nx.spring_layout(G)
nx.draw(G, layout, with_labels=True)
#labels = nx.get_edge_attributes(G, "weight")
#nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
plt.savefig("graphH.png")
plt.clf()
nx.draw(G, with_labels=True)
plt.savefig("graphG.png")
'''
