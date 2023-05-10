
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import csv


def getTrack(music_name, music_artist):
    # spotify developerから取得したclient_idとclient_secretを入力
    client_id = 'bdbfd3ec572846619335e13dd3d60057'
    client_secret = '47614857c04f465baefd0fb4b37dfc8a'

    client_credentials_manager = SpotifyClientCredentials(
        client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    t_sp1 = sp.search(f"{music_name}+{music_artist[:4]}", limit=30)
    tracks = t_sp1['tracks']['items']
    # print(t_sp1['tracks']['items'][0]['name'])
    l = len(tracks)
    if len(tracks) == 0:

        return ""
    id = tracks[0]['id']
    for x in range(0, l):

        # break
        name = tracks[x]['name']
        artist = tracks[x]['artists'][0]['name']
        name = name.strip(" ")
        artist = artist.strip(" ")
        if ((name == music_name) or (music_name.find(name) != -1) or (name.find(music_name) != -1)):
            print(name, "|", artist, "|", music_artist)
            if((music_artist is artist) or (music_artist.find(artist) != -1) or (artist.find(music_artist) != -1)):
                id = tracks[x]['id']
                break

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
    print(track)
    return(track)


if __name__ == '__main__':

    file = open("movie_music3.csv")
    music_list = list(csv.reader(file))
    new_music_list = []
    file.close()
    for music in music_list:
        if music[2] != "":
            track = getTrack(music[2], music[3])
            music.append(track)
            new_music_list.append(music)
    with open("movie_music3.csv", "w", encoding='utf-8', newline="") as file:
        writer = csv.writer(file)
        for Music in new_music_list:
            writer.writerow(Music)
        file.close()
