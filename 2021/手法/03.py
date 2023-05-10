import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import csv


def getmain_music_string(string):
    s = "「"
    begin = 0
    if(string.find(s) != -1):
        begin = string.index(s)+1
    end = len(string)
    if(string.find("」") != -1):
        end = string.index("」")
    elif(string.find("(") != -1):
        end = string.index("(")

    if begin == end:
        end = len(string)
    return string[begin:end]


def get_music_id(movie_list):
    id_list = []
    for movie in movie_list:
        movie_name = movie[0]
        # music_name = getmain_music_string(movie[1])
        music_name = movie[1]
        music_artist = movie[2]
        if music_name == "":
            continue
        music_artist = music_artist.strip(" ")
        music_name = music_name.strip(" ")
        t_sp1 = sp.search(f"{music_name}+{music_artist[:4]}", limit=30)
        tracks = t_sp1['tracks']['items']
        # print(t_sp1['tracks']['items'][0]['name'])
        l = len(tracks)
        movie_music_id = []
        id = ""
        for x in range(0, l):
            id = ""
            name = tracks[x]['name']
            artist = tracks[x]['artists'][0]['name']
            name = getmain_music_string(name)
            name = name.strip(" ")
            artist = artist.strip(" ")
            if ((name == music_name) or (music_name.find(name) != -1) or (name.find(music_name) != -1)):
                print(name, "|", artist, "|", music_artist)
                if((music_artist is artist) or (music_artist.find(artist) != -1) or (artist.find(music_artist) != -1)):
                    id = tracks[x]['id']
                    break
        movie_music_id.append(movie_name)
        movie_music_id.append(music_name)
        movie_music_id.append(music_artist)
        movie_music_id.append(id)
        id_list.append(movie_music_id)
        time.sleep(1)
    return id_list


def getTrackFeatures(movie, id):
    meta = sp.track(id)
    features = sp.audio_features(id)
    movie_name = movie[0]
    movie_music_name = movie[1]
    movie_music_artist = movie[2]
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

    track = [movie_name, movie_music_name, movie_music_artist, name, album, artist, release_date, length, popularity, key, mode, danceability, acousticness,
             energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature, valence]
    return track


if __name__ == '__main__':
    # spotify developerから取得したclient_idとclient_secretを入力
    client_id = 'bdbfd3ec572846619335e13dd3d60057'
    client_secret = '47614857c04f465baefd0fb4b37dfc8a'

    client_credentials_manager = SpotifyClientCredentials(
        client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    '''
    movie1 = ["イレイザー Eraser (1996)", "「Where Do We Go From Here(愛のゆくえ)"]
    movie2 = [
        "鬼滅の刃 (2019) ", "「from the edge」FictionJunction feat. LiSA、梶浦由記(作詞・作曲・編曲)"]

    movie_list = []
    movie_list.append(movie1)
    movie_list.append(movie2)
    '''
    file = open("movie_music_list.csv")
    movie_list = list(csv.reader(file))
    file.close()
    for n in range(98, 527):
        mini_list = []
        for i in range(0, 10):
            cnt = n*10+i
            mini_list.append(movie_list[cnt])

        file = open("movie_spotify_music_data.csv")
        tracks = list(csv.reader(file))
        file.close()
        movie_music_id_list = get_music_id(mini_list)

        for movie in movie_music_id_list:
            if movie[3] != "":
                track = getTrackFeatures(movie, movie[3])
                tracks.append(track)
            time.sleep(0.5)
        with open("movie_spotify_music_data.csv", "w", encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            for tracks in tracks:
                writer.writerow(tracks)
            file.close()

        time.sleep(5)
        print(n)
