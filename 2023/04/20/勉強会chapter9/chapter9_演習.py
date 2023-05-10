from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()
x_org, y_org = iris.data, iris.target

x_select = x_org[:, [0, 2]]
print('元データ', x_select.shape, y_org.shape)


x_t0 = x_select[y_org == 0]
x_t1 = x_select[y_org == 1]
x_t2 = x_select[y_org == 2]
"""
plt.figure(figsize=(6,6))
plt.scatter(x_t0[:,0], x_t0[:,1], marker='x', c='k', s=50, label='0 (setosa)')
plt.scatter(x_t1[:,0], x_t1[:,1], marker='o', c='b', s=50, label='1 (versicolour)')
plt.scatter(x_t2[:,0], x_t2[:,1], marker='+', c='k', s=50, label='2 (virginica)')
plt.xlabel('sepal_length', fontsize=14)
plt.ylabel('petal_length', fontsize=14)
plt.xticks(size=14)
plt.yticks(size=14)
plt.legend(fontsize=14)
plt.show()
"""

# ダミー変数を追加
x_all = np.insert(x_select, 0, 1.0, axis=1)
# yをOne-hot-Vectorに
ohe = OneHotEncoder(sparse=False, categories='auto')
y_work = np.c_[y_org]
y_all_one = ohe.fit_transform(y_work)
print('オリジナル', y_org.shape)
print('２次元化', y_work.shape)
print('One Hot Vector化後', y_all_one.shape)
# 学習データ、検証データに分割

x_train, x_test, y_train, y_test, y_train_one, y_test_one = train_test_split(
    x_all, y_org, y_all_one, train_size=75, test_size=75, random_state=123)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape,
      y_train_one.shape, y_test_one.shape)

print('入力データ(x)')
print(x_train[:5, :])
print('正解データ(y)')
print(y_train[:5])
print('正解データ (One Hot Vector化後)')
print(y_train_one[:5, :])

# 学習対象の選択
x, yt = x_train, y_train_one

# softmax関数 (9.7.3)


def softmax(x):
    x = x.T
    x_max = x.max(axis=0)
    x = x - x_max
    w = np.exp(x)
    return (w / w.sum(axis=0)).T

# 予測値の計算 (9.7.1, 9.7.2)


def pred(x, W):
    return softmax(x @ W)

# 交差エントロピー関数)(9.5.1)


def cross_entropy(yt, yp):
    return -np.mean(np.sum(yt * np.log(yp), axis=1))


def evaluate(x_test, y_test, y_test_one, W):

    # 予測値の計算(確率値)
    yp_test_one = pred(x_test, W)

    # 確率値から予測クラス(0, 1, 2)を導出
    yp_test = np.argmax(yp_test_one, axis=1)

    # 損失関数値の計算
    loss = cross_entropy(y_test_one, yp_test_one)

    # 精度の算出
    score = accuracy_score(y_test, yp_test)
    return loss, score


# 標本数
M = x.shape[0]
# 入力次元数(ダミー変数を含む
D = x.shape[1]
# 分類先クラス数
N = yt.shape[1]

# 繰り返し回数
iters = 10000

# 学習率
alpha = 0.01

# 重み行列の初期設定(すべて1)
W = np.ones((D, N))

# 評価結果記録用
history = np.zeros((0, 3))
# ここからお願いします。
#  メイン処理
for k in range(iters):

    # 予測値の計算 (9.7.1)　(9.7.2)
    yp = pred(x, W)

    # 誤差の計算 (9.7.4)
    yd = yp - yt

    # 重みの更新 (9.7.5)
    W = W - alpha * (x.T @ yd) / M

    if (k % 10 == 0):
        loss, score = evaluate(x_test, y_test, y_test_one, W)
        history = np.vstack((history,
                             np.array([k, loss, score])))
        print("epoch = %d loss = %f score = %f"
              % (k, loss, score))

# 損失関数値と精度の確認
print('初期状態: 損失関数:%f 精度:%f'
      % (history[0, 1], history[0, 2]))
print('最終状態: 損失関数:%f 精度:%f'
      % (history[-1, 1], history[-1, 2]))
# 学習曲線の表示 (損失関数)
plt.plot(history[:, 0], history[:, 1])
plt.ylim(0, 1.2)
plt.grid()
plt.xlabel('iter', fontsize=14)
plt.ylabel('loss', fontsize=14)
plt.title('iter vs loss', fontsize=14)
plt.show()

# 学習曲線の表示 (精度)
plt.plot(history[:, 0], history[:, 2])
plt.ylim(0, 1)
plt.grid()
plt.xlabel('iter', fontsize=14)
plt.ylabel('accuracy', fontsize=14)
plt.title('iter vs accuracy', fontsize=14)
plt.show()
