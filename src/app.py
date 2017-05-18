# Modules
import numpy as np
import networkx as nx
import math
import matplotlib.pyplot as plt

# Local
import graph
import songs


FAKE_SONGS = []
FILTER_BY_TEMPO = True
TEMPO_RANGE = 5


# Build out test data
def create_songs():
    for i in range(0, 50):
        song = {}
        song['id'] = i + 1
        song['key'] = int(math.ceil(np.random.random() * 12))
        song['mode'] = int(round(np.random.random(), 0))
        song['modified_key'] = (song['key'] * (song['mode'] + 1 ))
        song['tempo'] = np.random.normal(loc=120.0, scale=8.0, size=None)
        FAKE_SONGS.append(song)
    return
create_songs()

# Songs
REAL_SONGS = songs.get_songs()

# Build harmony and tempo graph
# ------------
harmony_graph = graph.build_harmony_graph(FAKE_SONGS, FILTER_BY_TEMPO, TEMPO_RANGE)
# print harmony_graph

# Graph
d = harmony_graph
G = nx.Graph(d)
nx.draw_spring(G, node_size=300, with_labels=True)
# ----------
# plt.show()



