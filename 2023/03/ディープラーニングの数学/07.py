# 必要ライブラリの宣言
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# waring抑止
import warnings
warnings.filterwarnings('ignore')


def pred(x, w):
    return (x @ w)


# 「ボストン・データセット」はscikit-learnのライブラリでも取得できるが、
# その場合、将来版で利用できなくなる予定のため、別Webサイトから取得する
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+",
                     skiprows=22, header=None)
x_org = np.hstack([raw_df.values[::2, :],
                   raw_df.values[1::2, :2]])
yt = raw_df.values[1::2, 2]
feature_names = np.array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
                          'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

print('元データ', x_org.shape, yt.shape)
print('項目名: ', feature_names)

# データ絞り込み (項目 RMのみ)
x_data = x_org[:, feature_names == 'RM']
print('絞り込み後', x_data.shape)

# ダミー変数を追加

x = np.insert(x_data, 0, 1.0, axis=1)
print('ダミー変数追加後', x.shape)


print(x.shape)
print(x[:5, :])

print(yt[:5])

M = x.shape[0]
D = x.shape[1]
iters = 50000
alpha = 0.01
w = np.ones(D)

history = np.zeros((0, 2))
for k in range(iters):
    yp = pred(x, w)

    yd = yp-yt

    w = w-alpha*(x.T@yd)/M

    if(k % 100 == 0):
        loss = np.mean(yd**2)/2

        #history = np.vstack((history, np.array([k, loss])))
        history = np.vstack((history, np.array([k, loss])))
        #print("iter=", k, "loss=", loss)

print('損失関数初期値: %f' % history[0, 1])
print('損失関数最終値: %f' % history[-1, 1])
xall = x[:, 1].ravel()
xl = np.array([[1, xall.min()], [1, xall.max()]])
yl = pred(xl, w)
'''
plt.figure(figsize=(6, 6))
plt.scatter(x[:, 1], yt, s=10, c='b')
plt.xlabel('ROOM', fontsize=14)
plt.ylabel('PRICE', fontsize=14)
plt.plot(xl[:, 1], yl, c='k')
plt.show()

plt.plot(history[1:, 0], history[1:, 1])
plt.show()
'''

# 列(LSTAT: 低所得者率)の追加
x_add = x_org[:, feature_names == 'LSTAT']
x2 = np.hstack((x, x_add))
print(x2.shape)
# 入力データxの表示 (ダミーデータを含む)
print(x2[:5, :])
# データ系列総数
M = x2.shape[0]

# 入力データ次元数(ダミー変数を含む)
D = x2.shape[1]

# 繰り返し回数
iters = 50000

# 学習率
alpha = 0.01

# 重みベクトルの初期値 (すべての値を1にする)
w = np.ones(D)

# 評価結果記録用 (損失関数値のみ記録)
history = np.zeros((0, 2))
for k in range(iters):

    # 予測値の計算 (7.8.1)
    yp = pred(x2, w)

    # 誤差の計算 (7.8.2)
    yd = yp - yt

    # 勾配降下法の実装 (7.8.4)
    w = w - alpha * (x2.T @ yd) / M

    # 学習曲線描画用データの計算、保存
    if (k % 100 == 0):
        # 損失関数値の計算 (7.6.1)
        loss = np.mean(yd ** 2) / 2
        # 計算結果の記録
        history = np.vstack((history, np.array([k, loss])))
        # 画面表示
        #print("iter = %d  loss = %f" % (k, loss))

# 初期化処理 (パラメータを適切な値に変更)

# データ系列総数
M = x2.shape[0]

# 入力データ次元数(ダミー変数を含む)
D = x2.shape[1]

# 繰り返し回数
#iters = 50000
iters = 2000

# 学習率
#alpha = 0.01
alpha = 0.001

# 重みベクトルの初期値 (すべての値を1にする)
w = np.ones(D)

# 評価結果記録用 (損失関数値のみ記録)
history = np.zeros((0, 2))

x_add = x_org[:, feature_names == 'LSTAT']
x2 = np.hstack((x, x_add))
print(x2.shape)

print(x2[:5, :])

M = x2.shape[0]
D = x2.shape[1]

iters = 50000
alpha = 0.01

w = np.ones(D)
history = np.zeros((0, 2))

for k in range(iters):

    yp = pred(x2, w)

    yd = yp - yt

    w = w - alpha * (x2.T @ yd) / M

    if (k % 100 == 0):
        loss = np.mean(yd ** 2) / 2
        history = np.vstack((history, np.array([k, loss])))

        #print("iter = %d  loss = %f" % (k, loss))
M = x2.shape[0]
D = x2.shape[1]

iters = 2000
alpha = 0.001

w = np.ones(D)
history = np.zeros((0, 2))

print('損失関数初期値: %f' % history[0, 1])
print('損失関数最終値: %f' % history[-1, 1])
