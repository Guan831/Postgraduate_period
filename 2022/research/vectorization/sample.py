import random
import csv
import gensim
from gensim.models.word2vec import Word2Vec
import numpy as np
from collections import defaultdict
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import time

start = time.time()


# じゃらんモデル
# model = gensim.models.KeyedVectors.load_word2vec_format("/Users/ota/2022_ota/research/taiken/jalan_wakati.model")
# model = gensim.models.KeyedVectors.load_word2vec_format("/Users/ota/2022_ota/research/taiken/jalan_wakati_neologd.model")
model = gensim.models.KeyedVectors.load_word2vec_format(
    "/Users/ota/2022_ota/research/taiken/jalan_wakati_neologd.model.bin", binary=True)


# 体験の取得
with open("/Users/ota/2022_ota/research/taiken/data/taiken_jalan.csv", "r", encoding="utf-8_sig") as f:
    words = csv.reader(f)
    words_list = list(words)
# random.seed(1000)
words_list = random.sample(words_list, 75000)


# 体験ベクトルの生成
vecvec_list = []
wordword_list = []
for i in range(len(words_list)):
    if words_list[i][0] in model.index_to_key and words_list[i][1] in model.index_to_key:
        # 名詞の単語ベクトル
        vec1 = model[words_list[i][0]]
        # print(f'「{words_list[i][0]}」のベクトル：{vec1} 次元数：{vec1.shape}')
    # 動詞の単語ベクトル
        vec2 = model[words_list[i][1]]
        # print(f'「{words_list[i][1]}」のベクトル：{vec2} 次元数：{vec2.shape}')
    # 名詞+動詞の単語ベクトル
        wordword_list.append(words_list[i][0] + words_list[i][1])
        # 結合
        # v1 = vec1.tolist()
        # v2 = vec2.tolist()
        # vec3 = v1 + v2
        # vecvec_list.append(vec3)
        # 平均値
        # vec3 = np.mean([vec1, vec2], axis=0)
        # vecvec_list.append(vec3)
        # 最大値
        vec3 = np.maximum(vec1, vec2)
        vecvec_list.append(vec3)
        # 絶対値の最大値
        # vec1_abs = np.abs(vec1)
        # vec2_abs = np.abs(vec2)
        # vec3 =[]
        # for i in range(200):
        #     if vec1_abs[i] > vec2_abs[i]:
        #         vec3.append(vec1[i])
        #     else:
        #         vec3.append(vec2[i])
        # vecvec_list.append(vec3)
    # ベクトルの表示
        # print(f'「{wordword_list[-1]}」のベクトル：{vecvec_list[-1]} 次元数：{len(vec3)}')

print(f"taiken_vec: {len(vecvec_list)}")


# 階層的クラスタリング（群平均法,コサイン類似度）
linkage_result = linkage(vecvec_list, method='average', metric='cosine')
# コサイン類似度  範囲：-1~1
threshold = 0.2

clustered = fcluster(linkage_result, t=threshold, criterion='distance')
dic = defaultdict(list)
k = []
for i in range(len(wordword_list)):
    dic[clustered[i]].append(wordword_list[i])
for i in range(1, len(dic)+1):
    k.append(dic[i])
    # print(i, dic[i])
print("cluster:", len(k))


# クラスタリング結果をcsvに保存
with open("/Users/ota/2022_ota/research/taiken/data/cluster75000_max0.2.csv", "w", encoding='utf_8_sig', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(k)


end = time.time()
print("time:", end - start)
