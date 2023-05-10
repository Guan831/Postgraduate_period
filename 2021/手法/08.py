
import numpy as np
import csv


A = [['たぶん', 'THE BOOK', 'YOASOBI', '2021-01-06', 256773, 69, 5, 1, 0.748,
      0.157, 0.661, 0.00102, 0.101, -6.702, 0.0334, 90.003, 4, 0.743],
     ['ベテルギウス', 'ベテルギウス', 'Yuuri', '2021-11-04', 230393, 77, 5, 1,
         0.432, 0.199, 0.68, 0, 0.481, -4.839, 0.0431, 180.002, 4, 0.685],
     ['レオ', '壱', 'Yuuri', '2022-01-12', 238973, 63, 5, 1, 0.629,
         0.383, 0.543, 0, 0.127, -6.281, 0.0252, 93.043, 4, 0.403],
     ['YELLOW', 'SHIAWASE NA OTONA', 'Yoh kamiyama', '2019-04-03', 178712, 65, 7,
      0, 0.786, 0.0144, 0.719, 0.000638, 0.0887, -4.77, 0.0353, 117.981, 4, 0.686],
     ['Beautiful World - Da Capo Version', 'BADモード', 'Hikaru Utada', '2022-01-19',
      357886, 55, 8, 0, 0.436, 0.701, 0.415, 0, 0.1, -11.354, 0.0628, 113.828, 4, 0.294],

     ['白日', 'CEREMONY', 'King Gnu', '2020-01-15', 276373, 2, 1, 1, 0.599,
         0.562, 0.891, 0.0, 0.322, -3.242, 0.116, 93.029, 4, 0.694],
     ['小さな惑星', 'Ceremony', 'King Gnu', '2020-01-15', 151773, 24, 11, 1, 0.615,
     0.0797, 0.953, 0.0186, 0.198, -2.996, 0.0544, 119.947, 4, 0.766],
     ['Remember Me', 'Remember Me', 'MAN WITH A MISSION', '2019-05-06', 288900, 0, 0, 1, 0.542,
      0.00393, 0.848, 0.0, 0.0848, -4.302, 0.0496, 125.991, 4, 0.381],
     ['恋音と雨空', 'AAA Special Live 2016 in Dome -FANTASTIC OVER- SET LIST', 'AAA', '2017-01-18', 316186, 50, 1, 1, 0.625,
      0.0512, 0.86, 0.0, 0.408, -4.456, 0.0314, 129.064, 4, 0.533],
     ['新宝島', '魚図鑑', 'Sakanaction', '2018-03-28', 302493, 54, 7, 0, 0.557,
         0.00118, 0.917, 0.00914, 0.419, -3.426, 0.0757, 158.0, 4, 0.653],

     ['感電', 'STRAY SHEEP', 'Kenshi Yonezu', '2020-08-05', 264533, 4, 8, 0, 0.633, 0.107,
      0.723, 0.0, 0.0818, -5.733, 0.143, 103.101, 4, 0.688],
     ['ドライフラワー', 'ドライフラワー', '優里', '2020-10-25', 285586, 77, 7, 1, 0.463, 0.426,
     0.624, 0.0, 0.221, -5.118, 0.0274, 147.929, 4, 0.521],
     ['Lemon', 'STRAY SHEEP', 'Kenshi Yonezu', '2020-08-05', 255826, 54, 11, 1, 0.525,
      0.304, 0.646, 0.0, 0.297, -4.963, 0.0268, 86.957, 4, 0.373],
     ['LOSER', 'BOOTLEG', 'Kenshi Yonezu', '2017-11-01', 243813, 0, 1, 0, 0.679,
     0.00466, 0.931, 0.0, 0.0652, -3.74, 0.0474, 121.001, 4, 0.962],
     ['カタオモイ', 'daydream', 'Aimer', '2016-09-21', 207360, 1, 1, 1, 0.621,
     0.78, 0.533, 0.0, 0.333, -5.974, 0.0342, 96.981, 4, 0.791]
     ]
B = [
    ['砂の惑星 ( + 初音ミク )', 'BOOTLEG', 'Kenshi Yonezu', '2017-11-01', 240026, 54,
     10, 0, 0.507, 0.0252, 0.94, 0, 0.152, -3.264, 0.0927, 94.874, 4, 0.917],
    ['Pretender', 'Traveler', 'Official HIGE DANdism', '2019-08-31', 326842,
     60, 8, 1, 0.538, 0.047, 0.869, 0, 0.14, -3.464, 0.0275, 91.972, 4, 0.369],
    ['優しい彗星(TVアニメ 「BEASTARS」エンディング)(オリジナル:YOASOBI)(ピアノ)', '癒しのピアノ「J-POPセレクション」 vol.6', 'スイートピアノ・メロディーズ',
     '2021-02-08', 219966, 7, 5, 1, 0.538, 0.225, 0.651, 0.945, 0.105, -9.32, 0.0358, 89.989, 4, 0.421],
    ['One Last Kiss(原曲: 宇多田ヒカル)「シン・エヴァンゲリオン劇場版」より[ORIGINAL COVER]', 'One Last Kiss(原曲: 宇多田ヒカル)「シン・エヴァンゲリオン劇場版」より[ORIGINAL COVER]',
     'サウンドワークス', '2021-03-12',
     40982, 1, 8, 0, 0.474, 0.579, 0.431, 0.803, 0.0762, -14.801, 0.0409, 111.933, 4, 0.148],
    ['残響散歌', '残響散歌', 'Aimer', '2021-12-06',
     184893, 83, 11, 1, 0.367, 0.000627, 0.896, 0, 0.207, -4.002, 0.091, 170.863, 4, 0.38]]

C = [['LOSER', 'BOOTLEG', 'Kenshi Yonezu', '2017-11-01', 243813, 0, 1, 0, 0.679,
     0.00466, 0.931, 0.0, 0.0652, -3.74, 0.0474, 121.001, 4, 0.962],
     ['白日', 'CEREMONY', 'King Gnu', '2020-01-15', 276373, 2, 1, 1, 0.599,
     0.562, 0.891, 0.0, 0.322, -3.242, 0.116, 93.029, 4, 0.694],
     ['炎', '炎', 'LiSA', '2020-10-12', 275000, 73, 2, 1, 0.477,
         0.105, 0.685, 0, 0.277, -4.554, 0.0325, 152.04, 4, 0.308],
     ['Pretender', 'Traveler', 'Official HIGE DANdism', '2019-08-31', 326842,
     60, 8, 1, 0.538, 0.047, 0.869, 0, 0.14, -3.464, 0.0275, 91.972, 4, 0.369],
     ['Lemon', 'STRAY SHEEP', 'Kenshi Yonezu', '2020-08-05', 255826, 54, 11, 1, 0.525,
     0.304, 0.646, 0.0, 0.297, -4.963, 0.0268, 86.957, 4, 0.373],

     ]


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def cossim_list(music_list, Y):
    y = bekutoru(Y)
    Movie_cossin_D = {}
    for music in music_list:
        x = []
        for i in range(7, 19):
            x.append(float(music[i]))
        x = bekutoru(x)
        cnt = cos_sim(x, y)
        Movie_cossin_D[music[0]] = cnt
    d_order = sorted_D(Movie_cossin_D)
    return d_order


def sorted_D(d={}):
    d_order = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return d_order


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

    music_list = list(C)
    Umusic_list = list(C)

    SMusic_list = []
    for uMusic in Umusic_list:
        y = []
        sMusic_list = []
        for i in range(6, 18):
            y.append(float(uMusic[i]))
        y = bekutoru(y)
        for music in music_list:
            x = []
            for i in range(6, 18):
                x.append(float(music[i]))
            x = bekutoru(x)
            cnt1 = cos_sim(x, y)
            UM = [music[0], uMusic[0], cnt1]
            sMusic_list.append(UM)
        sMusic_list.sort(key=lambda x: x[2], reverse=True)
        SMusic_list.append(sMusic_list)
        # print(cnt)
    with open("music_to_music_test2.csv", "w", encoding='utf-8', newline="") as file:
        writer = csv.writer(file)
        for Music in SMusic_list:
            writer.writerow(Music)
        file.close()
    """

    A = ['前前前世', '前前前世', 'Aruvn', '2017-01-31', 280460, 37, 1, 0, 0.502,
         0.00179, 0.952, 0, 0.0908, -4.567, 0.0805, 94.939, 4, 0.501]

    B = ['AS ONE', '30', 'UVERworld', '2021-12-22', 229253, 45, 1, 1, 0.333,
         0.000225, 0.859, 2.63e-05, 0.618, -4.596, 0.073, 107.146, 3, 0.519]
    x = []
    for i in range(6, 18):
        x.append(float(A[i]))
    x = bekutoru(x)
    y = []
    for i in range(6, 18):
        y.append(float(B[i]))
    y = bekutoru(y)
    cnt = cos_sim(x, y)
    print(cnt)
    """
