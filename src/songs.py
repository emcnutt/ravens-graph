# SONGS
# -------------
# Used to pull songs from spotify

import json
import math

import numpy as np
import spotipy
import spotipy.util as util

# Authorization
scope = 'user-library-read playlist-modify-private playlist-read-private playlist-read-collaborative playlist-modify-public'
username = '1233289929'  # Change to ID
client_id = '7a7ff44c4ab14b7a929af189770abf4c'
client_secret = 'e613d7b6e6b744d9a489a9ae126cd2aa'
redirect_uri = 'http://localhost/'
playlist_id = '6wF3lPFUIZeIij8WkkA48O'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
if token:
    spotify = spotipy.Spotify(auth=token)
else:
    print("Can't get token for: ", username)

# Key Notation Lookup
CAMELOT = {
    0: {
        0: '5A',
        1: '8B'
    },
    1: {
        0: '12A',
        1: '3B'
    },
    2: {
        0: '10B',
        1: '7A'
    },
    3: {
        0: '2A',
        1: '5B'
    },
    4: {
        0: '12B',
        1: '9A'
    },
    5: {
        0: '4A',
        1: '7B'
    },
    6: {
        0: '11A',
        1: '2B'
    },
    7: {
        0: '6A',
        1: '9B'
    },
    8: {
        0: '1A',
        1: '4B'
    },
    9: {
        0: '11B',
        1: '8A'
    },
    10: {
        0: '3A',
        1: '6B'
    },
    11: {
        0: '10A',
        1: '1B'
    }
}

# Seed
SEED = ['1mvDFqbbmgmMmU6U4dIq5m']
TARGET_DANCEABILITY = 0.80
TARGET_POPULARITY = None
TARGET_ENERGY = 0.70
TARGET_INSTRUMENTALNESS = 0.50
TARGET_ACOUSTICNESS = None
TARGET_VALENCE = None
TARGET_TEMPO = None


# Build out and return new songs
def get_new_songs(network_size=100):
    recommendations = get_recommendations(SEED, network_size)
    print(recommendations)
    ids = get_recommendation_track_ids()
    songs = get_song_data(ids);
    converted_songs = convert_key_notation(songs)
    print('YO: New songs all been got')
    return converted_songs


# Return old songs
def get_old_songs():
    with open('./songs.json') as data_file:
        songs = json.load(data_file)
    print('YO: Old songs all been got')
    return songs


# Get song recommendations. Takes an array of song/artist ids
def get_recommendations(seed_tracks, limit, seed_artists=None, seed_genres=None):
    country = 'US'
    recommendations = spotify.recommendations(
        seed_artists,
        seed_genres,
        seed_tracks,
        limit,
        country,
        target_danceability=TARGET_DANCEABILITY,
        target_popularity=TARGET_POPULARITY,
        target_energy=TARGET_ENERGY,
        target_instrumentalness=TARGET_INSTRUMENTALNESS,
        target_acousticness=TARGET_ACOUSTICNESS,
        target_valence=TARGET_VALENCE,
        target_tempo=TARGET_TEMPO,
    )

    with open('./recommendations.json', 'w') as outfile:
        json.dump(recommendations, outfile, sort_keys=True, indent=4, ensure_ascii=True)

    # print(json.dumps(recommendations))
    return


# Takes a blob of reccomendations and returns an array of song URIs
def get_recommendation_track_ids():
    track_ids = []
    with open('./recommendations.json') as data_file:
        data = json.load(data_file)
    for track in data["tracks"]:
        track_ids.append(track["id"])
    return track_ids


# Takes an array of songs and build a json file of the relevant song info needed
def get_song_data(song_id_array):
    analysis = spotify.audio_features(tracks=song_id_array)
    with open('./songs.json', 'w') as outfile:
        json.dump(analysis, outfile, sort_keys=True, indent=4,
                  ensure_ascii=True)
    return analysis


# Takes an array of songs objects and converts key+mode to camelot wheel notation
def convert_key_notation(songs):
    converted_songs = []
    for song in songs:
        key = song['key']
        mode = song['mode']
        matched_key = CAMELOT[key]
        converted_key = matched_key[mode]
        song["camelot"] = converted_key
        converted_songs.append(song)

    with open('./songs.json', 'w') as outfile:
        json.dump(converted_songs, outfile, sort_keys=True, indent=4,
                  ensure_ascii=True)
    return converted_songs


# Build out test data
def create_fake_songs():
    fake_songs = []
    for i in range(0, 50):
        song = {}
        song['id'] = i + 1
        song['key'] = int(math.ceil(np.random.random() * 12))
        song['mode'] = int(round(np.random.random(), 0))
        song['modified_key'] = (song['key'] * (song['mode'] + 1))
        song['tempo'] = np.random.normal(loc=120.0, scale=8.0, size=None)
        fake_songs.append(song)
    return fake_songs


# Create playlist on spotify
def replace_playlist(tracks):
    uris = []
    for track in tracks:
        uri = 'spotify:track:{0}'.format(track)
        uris.append(uri)
    spotify.user_playlist_replace_tracks(username, playlist_id, uris)
