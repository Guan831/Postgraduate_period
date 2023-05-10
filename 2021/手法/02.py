import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
#from google.colab import files


def getTrackIDs(playlist_ids):
    track_ids = []

    for playlist_id in playlist_ids:
        playlist = sp.playlist(playlist_id)
        while playlist['tracks']['next']:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])
            playlist['tracks'] = sp.next(playlist['tracks'])
        else:
            for item in playlist['tracks']['items']:
                track = item['track']
                if not track['id'] in track_ids:
                    track_ids.append(track['id'])

    return track_ids


def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    key = features[0]['key']
    mode = features[0]['mode']
    danceability = features[0]['danceability']
    acousticness = features[0]['acousticness']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    valence = features[0]['valence']

    track = [name, album, artist, release_date, length, popularity, key, mode, danceability, acousticness,
             energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature, valence]
    return track


if __name__ == '__main__':
    # spotify developerから取得したclient_idとclient_secretを入力
    client_id = 'bdbfd3ec572846619335e13dd3d60057'
    client_secret = '47614857c04f465baefd0fb4b37dfc8a'

    client_credentials_manager = SpotifyClientCredentials(
        client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    t_sp1 = sp.search("桜ひとひら",type="")
    playlist_ids = ['4vFZ21t84EEfWkl7HGa926',
                    '1qOIDkEQX5ee2zxsGVxejg']  # SpotifyのプレイリストのIDを入力
    track_ids = getTrackIDs(playlist_ids)
    print(len(track_ids))
    print(track_ids)

    tracks = []

    for track_id in track_ids:
        time.sleep(0.5)
        track = getTrackFeatures(track_id)
        tracks.append(track)

    df = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'key', 'mode', 'danceability',
                      'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature', 'valence'])
    df.head()

    df.to_csv('spotify_music_data.csv', sep=',')

    #  files.download('spotify_music_data.csv')
