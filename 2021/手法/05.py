import numpy as np
import csv


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


def sorted_D(d={}):
    d_order = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return d_order


def cossim_list(music_list, Y):
    y = bekutoru(Y)
    Movie_cossin_D = {}
    for music in music_list:
        x = []
        for i in range(8, 20):
            x.append(float(music[i]))
        x = bekutoru(x)
        cnt = cos_sim(x, y)
        Movie_cossin_D[music[0]] = cnt
    d_order = sorted_D(Movie_cossin_D)

    return d_order


def merge_dict(x, y=[]):
    for k, v in x:
        cnt = 0
        i = 0
        for a, b in y:

            if k == a:
                y[i][1] = b+v
                b = b+v
                cnt = 1
                break
            i = i+1
        if cnt == 0:
            y.append([k, v])
    return y


if __name__ == '__main__':
    U_music_list = [[2, 1, 0.477, 0.105, 0.685, 0.0, 0.277, -4.554, 0.0325, 152.04, 4, 0.308],
                    [8, 1, 0.67, 0.00231, 0.874, 1.72e-05,
                     0.3, -5.221, 0.0305, 130.041, 4, 0.789],
                    [0, 1, 0.844, 0.184, 0.851, 8.53e-05,
                     0.0754, -3.762, 0.0494, 116.038, 4, 0.541],
                    [7, 1, 0.78, 0.0436, 0.885, 2.8e-05,
                     0.105, -3.745, 0.122, 160.087, 4, 0.808],
                    [7, 1, 0.463, 0.426, 0.624, 0.0,
                     0.221, -5.118, 0.0274, 147.929, 4, 0.521],
                    [3, 1, 0.848, 0.824, 0.352, 0.0,
                     0.0906, -6.838, 0.041, 121.833, 4, 0.776], ]
    file = open("movie_spotify_music_data1.csv")
    music_list = list(csv.reader(file))
    file.close()
    U_music_cossim = []
    for umusic in U_music_list:
        music_cos_list = cossim_list(music_list, umusic)
        U_music_cossim = merge_dict(music_cos_list, U_music_cossim)
    U_music_cossim.sort(key=lambda x: x[1], reverse=True)
    print(U_music_cossim)
