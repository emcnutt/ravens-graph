# Modules
import numpy as np
import networkx as nx
import math
import matplotlib.pyplot as plt

# Local
import graph
import songs

FILTER_BY_TEMPO = True
TEMPO_RANGE = 5

# Real songs
REAL_SONGS = songs.create_real_songs();

# Fake songs
FAKE_SONGS = songs.create_fake_songs()

# Build harmony and tempo graph
# ------------
harmony_graph = graph.build_harmony_graph(REAL_SONGS, FILTER_BY_TEMPO, TEMPO_RANGE)
# print harmony_graph

# Graph
d = harmony_graph
G = nx.Graph(d)
nx.draw_spring(G, node_size=300, with_labels=True)
# ----------
plt.show()



