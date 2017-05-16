# SONGS
# -------------
# Used to pull songs from spotify

import spotipy
import spotipy.util as util


# Authorization
scope = 'user-library-read'
username = '1233289929' # Change to ID
token = util.prompt_for_user_token(username, scope)

if token:
    spotify = spotipy.Spotify(auth=token)
else:
    print "Can't get token for: ", username


# Analysis
# analysis = spotify.audio_features('01b8aKaPyULAQlGywrtm8U')
# print analysis

SEED = ['68hrtOiA7J06Bp42M6KZdc']
def get_recommendations(seed_tracks):
    seed_artists = None
    seed_genres = None
    limit = 20
    country = 'US'
    recommendations = spotify.recommendations(seed_artists, seed_genres, seed_tracks, limit, country)
    print recommendations
