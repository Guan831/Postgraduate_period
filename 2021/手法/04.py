
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


if __name__ == '__main__':
    X = np.array([7, 1, 0.501, 0.000273, 0.785, 0.0123,
                 0.36, -6.205, 0.0329, 94.109, 4, 0.211])
    Y = np.array([5, 1, 0.518, 0.0778, 0.585, 2.43E-06,
                 0.31, -8.485, 0.0279, 144.998, 4, 0.312])

    # cos(X,Y) = (0.789×0.832)+(0.515×0.555)+(0.335×0)+(0×0)≒0.942
    '''    
    X = bekutoru(X)
    print(X)
    print(cos_sim(bekutoru(X), bekutoru(Y)))
    '''

    file = open("movie_spotify_music_data1.csv")
    music_list = list(csv.reader(file))
    file.close()
    file = open("spotify_music_data.csv")
    Umusic_list = list(csv.reader(file))
    file.close()
    sMusic_list = []
    for uMusic in Umusic_list:
        y = []
        cnt = 0
        sMusic = []
        for i in range(7, 19):
            y.append(float(uMusic[i]))
        y = bekutoru(y)
        for music in music_list:
            x = []
            for i in range(8, 20):
                x.append(float(music[i]))
            x = bekutoru(x)
            cnt1 = cos_sim(x, y)
            if cnt1 > cnt:
                cnt = cnt1
                sMusic = music
        # print(sMusic)
        UM = [sMusic[0], uMusic[1], cnt]
        """ 
        sMusic.append(uMusic[1])
        sMusic.append(cnt)
        sMusic_list.append(sMusic)"""
        sMusic_list.append(UM)
        # print(cnt)
    with open("music_to_movie2.csv", "w", encoding='utf-8', newline="") as file:
        writer = csv.writer(file)
        for sMusic in sMusic_list:
            writer.writerow(sMusic)
        file.close()
