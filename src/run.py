# Modules
import math

# Local
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from src import graph, songs

FILTER_BY_TEMPO = True
TEMPO_RANGE = 5
NETWORK_SIZE = 100
PATH_LENGTH = 14

# Real songs
REAL_SONGS = songs.get_new_songs(NETWORK_SIZE)

# Fake songs
FAKE_SONGS = songs.create_fake_songs()

# Build harmony and tempo graph
# ------------
harmony_graph = graph.build_harmony_graph(REAL_SONGS, FILTER_BY_TEMPO, TEMPO_RANGE)
node_edge_count = graph.build_node_edge_count(REAL_SONGS, FILTER_BY_TEMPO, TEMPO_RANGE)

# Build graph
SONG_GRAPH = nx.Graph(harmony_graph)
edges = SONG_GRAPH.edges()
nodes = SONG_GRAPH.nodes()


# Get playlist
def find_possible_playlists():
    # Start off as no path being found
    starting_point = int(math.ceil(np.random.random() * NETWORK_SIZE))
    target_point = int(math.ceil(np.random.random() * NETWORK_SIZE))
    starting_node = nodes[starting_point]
    target_node = nodes[target_point]
    print('Starting Point:{0} -> Target Point:{1}'.format(starting_point, target_point))

    # Check for any path
    has_path = nx.has_path(SONG_GRAPH, source=starting_node, target=target_node)
    if not has_path:
        print('No path between nodes')

    # If path, find a long enough path
    if has_path:
        for path in nx.all_simple_paths(SONG_GRAPH, source=starting_node, target=target_node, cutoff=PATH_LENGTH):
            print(path)
            if len(path) <= PATH_LENGTH - 2:
                print('Path failed')
                find_possible_playlists()
            else:
                print('Path found')

                # Build playlist
                songs.replace_playlist(path)

                # Draw Graph
                nx.draw_spring(SONG_GRAPH, node_size=300, with_labels=True)
                plt.show()

                break
    else:
        find_possible_playlists()


# Build playlist and add to Spotify
find_possible_playlists()
