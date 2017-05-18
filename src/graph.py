# GRAPH
# -------------
# Used to build song graphs


# Harmony lookup (modified camelot wheel)
HARMONY = {
    1: [1, 12, 13, 2],
    2: [2, 1, 14, 3],
    3: [3, 2, 15, 4],
    4: [4, 3, 16, 5],
    5: [5, 4, 17, 6],
    6: [6, 5, 18, 7],
    7: [7, 6, 19, 8],
    8: [8, 7, 20, 9],
    9: [9, 8, 21, 10],
    10: [10, 9, 22, 11],
    11: [11, 10, 23, 12],
    12: [12, 11, 24, 13],
    13: [13, 12, 1, 14],
    14: [14, 13, 2, 15],
    15: [15, 14, 3, 16],
    16: [16, 15, 4, 17],
    17: [17, 16, 5, 18],
    18: [18, 17, 6, 19],
    19: [19, 18, 7, 20],
    20: [20, 19, 8, 21],
    21: [21, 20, 9, 22],
    22: [22, 21, 10, 23],
    23: [23, 22, 11, 24],
    24: [24, 23, 12, 1]
}


# Takes a song in a list of songs and returns an array of songs that are in harmony
def find_songs_in_harmony(song, songs, filter_by_tempo, tempo_range):
    song_id = song['id']
    song_key = song['modified_key']
    harmony_matches = HARMONY[song_key]
    song_matches = []
    for s in songs:
        match_key = s['modified_key']
        match_id = s['id']
        match_tempo = song['tempo']
        max_tempo = match_tempo + tempo_range
        min_tempo = match_tempo - tempo_range
        for value in harmony_matches:
            if value == match_key and match_id != song_id:
                if filter_by_tempo:
                    if min_tempo < match_tempo <  max_tempo:
                        song_matches.append(match_id)
                else:
                    song_matches.append(match_id)
    return song_matches


# Builds out a graph of songs in harmony
def build_harmony_graph(songs, filter_by_tempo=True, tempo_range=5):
    harmony_graph = {}
    for song in songs:
        song_id = song['id']
        songs_in_harmony = find_songs_in_harmony(song, songs, filter_by_tempo, tempo_range)
        harmony_graph[song_id] = songs_in_harmony
    return harmony_graph


# Builds out a graph of songs in harmony and tempo range
def build_harmony_and_tempo_graph(songs, tempo_range):
    harmony_and_tempo_graph = {}
    for song in songs:
        # print song
        song_id = song['id']
        song_tempo = song['tempo']
        songs_in_harmony = find_songs_in_harmony(song, songs)
        songs_in_harmony_and_tempo = filter_songs_by_tempo_range(songs_in_harmony, songs, song_tempo, tempo_range)
        harmony_and_tempo_graph[song_id] = songs_in_harmony_and_tempo
    return harmony_and_tempo_graph
