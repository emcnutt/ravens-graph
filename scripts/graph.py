# GRAPH
# -------------
# Used to build song graphs


# Harmony lookup (modified camelot wheel)
HARMONY = {
    '1A': ['1A', '12A', '1B', '2A'],
    '2A': ['2A', '1A', '2B', '3A'],
    '3A': ['3A', '2A', '3B', '4A'],
    '4A': ['4A', '3A', '4B', '5A'],
    '5A': ['5A', '4A', '5B', '6A'],
    '6A': ['6A', '5A', '6B', '7A'],
    '7A': ['7A', '6A', '7B', '8A'],
    '8A': ['8A', '7A', '8B', '9A'],
    '9A': ['9A', '8A', '9B', '10A'],
    '10A': ['10A', '9A', '10B', '11A'],
    '11A': ['11A', '10A', '11B', '12A'],
    '12A': ['12A', '11A', '12B', '1B'],
    '1B': ['1B', '12A', '1A', '2B'],
    '2B': ['2B', '1B', '2A', '3B'],
    '3B': ['3B', '2B', '3A', '4B'],
    '4B': ['4B', '3B', '4A', '5B'],
    '5B': ['5B', '4B', '5A', '6B'],
    '6B': ['6B', '5B', '6A', '7B'],
    '7B': ['7B', '6B', '7A', '8B'],
    '8B': ['8B', '7B', '8A', '9B'],
    '9B': ['9B', '8B', '9A', '10B'],
    '10B': ['10B', '9B', '10A', '11B'],
    '11B': ['11B', '10B', '11A', '12B'],
    '12B': ['12B', '11B', '12A', '1A']
}


# Takes a song in a list of songs and returns an array of songs that are in harmony
def find_songs_in_harmony(song, songs, filter_by_tempo, tempo_range, skip_same_artist=True):
    song_id = song['id']
    song_key = song['camelot']
    song_tempo = song['tempo']
    harmony_matches = HARMONY[song_key]
    song_matches = []
    for s in songs:
        match_key = s['camelot']
        match_id = s['id']
        match_tempo = s['tempo']
        max_tempo = song_tempo + tempo_range
        min_tempo = song_tempo - tempo_range
        for key in harmony_matches:
            if key == match_key and match_id != song_id:
                if filter_by_tempo:
                    if min_tempo <= match_tempo <=  max_tempo:
                        # print 'Min:{0} Match:{1} Max:{2} ID:{3}'.format(min_tempo, match_tempo, max_tempo, match_id)
                        song_matches.append(match_id)
                else:
                    song_matches.append(match_id)
    return song_matches


# Builds out a graph of songs in harmony
def build_harmony_graph(songs, filter_by_tempo=True, tempo_range=3):
    harmony_graph = {}
    for song in songs:
        song_id = song['id']
        songs_in_harmony = find_songs_in_harmony(song, songs, filter_by_tempo, tempo_range)
        harmony_graph[song_id] = songs_in_harmony
    # print harmony_graph
    return harmony_graph


# Builds out list of nodes and edge count
def build_node_edge_count(songs, filter_by_tempo=True, tempo_range=3):
    node_edge_count = []
    for song in songs:
        song_id = song['id']
        songs_in_harmony = find_songs_in_harmony(song, songs, filter_by_tempo, tempo_range)
        edge_count = len(songs_in_harmony)
        node_edge_count.append({song_id: edge_count})
    # print node_edge_count
    return node_edge_count
