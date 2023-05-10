from filecmp import cmp
import numpy as np
import csv

A = [[1, 0, 0.679, 0.00466, 0.931, 0.0, 0.0652, -3.74, 0.0474, 121.001, 4, 0.962],  # 夜に駆ける
     [1, 1, 0.599, 0.562, 0.891, 0.0, 0.322, - \
         3.242, 0.116, 93.029, 4, 0.694],  # 白日
     [2, 1, 0.477, 0.105, 0.685, 0, 0.277, -4.554, 0.0325, 152.04, 4, 0.308],  # 炎
     [8, 1, 0.538, 0.047, 0.869, 0, 0.14, -3.464,
         0.0275, 91.972, 4, 0.369],  # Pretender
     [11, 1, 0.525, 0.304, 0.646, 0.0, 0.297, - \
         4.963, 0.0268, 86.957, 4, 0.373]  # Lemon,

     ]


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def bekutoru(X):
    X[0] = (X[0]+1)/12
    X[7] = (X[7]+60)/60
    X[9] = (X[9]-60)/70
    if(X[9] < 0):
        X[9] = 0
    elif(X[9] > 1):
        X[9] = 1
    X[10] = (X[10]-3)/4
    return X


def sorted_D(d=[]):
    d.sort(key=lambda x: x[1], reverse=True)
    return d


def cossim_list(music_list, Y):
    y = bekutoru(Y)
    Movie_cossin_D = []
    for music in music_list:
        d = []
        x = []
        for i in range(8, 20):
            x.append(float(music[i]))
        x = bekutoru(x)
        cnt = cos_sim(x, y)
        d.append(music[0])
        d.append(cnt)
        if cnt >= 0.85:
            Movie_cossin_D.append(d)
    d_order = sorted_D(Movie_cossin_D)
    d_order2 = []
    for i, music in enumerate(d_order):
        x = 1/(i+1)
        music.append(x)
        d_order2.append(music)

    return d_order2


def merge_dict(x, y):
    for i, music in enumerate(x):
        cnt = 0

        for n, music2 in enumerate(y):

            if music[0] == music2[0]:
                music2[2] = music[2]+y[n][2]
                music2.append(music[3])
                music2.append(music[1])
                music2.append(i)
                y[n] = music2
                cnt = 1
                break
        if cnt == 0:
            music.append(i)
            y.append(music)

    return y


if __name__ == '__main__':
    U_music_list = A
    file = open("movie_spotify_music_data1.csv")
    music_list = list(csv.reader(file))
    file.close()
    U_music_cossim = []
    for i, umusic in enumerate(U_music_list):
        music_cos_list = cossim_list(music_list, umusic)

        for n, music in enumerate(music_cos_list):
            music_cos_list[n].append(i)
        U_music_cossim = merge_dict(music_cos_list, U_music_cossim)
    U_music_cossim.sort(key=lambda x: x[2], reverse=True)

    with open("music_to_movie4.csv", "w", encoding='utf-8', newline="") as file:
        writer = csv.writer(file)
        for Music in U_music_cossim:
            writer.writerow(Music)
        file.close()
