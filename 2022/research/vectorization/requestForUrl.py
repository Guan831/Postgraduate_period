# -*-coding : UTF-8 -*-
# import random
import csv
import json
# import gensim
# from gensim.models.word2vec import Word2Vec
from collections import Counter, defaultdict

import joblib
import numpy as np
import pickle
# import time
import pandas
import requests
from bs4 import BeautifulSoup
from janome.analyzer import Analyzer
# from janome.tokenfilter import ExtractAttributeFilter
from janome.tokenfilter import POSKeepFilter, POSStopFilter
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer,
                                             TfidfVectorizer)
from tqdm import tqdm


def get_words(string, keep_pos=None):
    filters = []
    if keep_pos is None:
        filters.addend(POSStopFilter(('記号')))  # 記号除外
    else:
        filters.append(POSKeepFilter(keep_pos))
    # filters.append(ExtractAttributeFilter('surface'))
    a = Analyzer(token_filters=filters)
    analyzed = list(a.analyze(string))
    words = []
    for token in analyzed:
        token = str(token)
        if token.split(',')[1] == "サ変接続" or token.split(',')[1] == "一般" or token.split(',')[1] == "固有名詞":
            words.append(token.split('\t')[0])

    return words


def stopword():
    url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
    r = requests.get(url)
    tmp = r.text.split('\r\n')
    stopwords = []
    for i in range(len(tmp)):
        if len(tmp[i]) < 1:
            continue
        stopwords.append(tmp[i])
    joblib.dump(stopwords, 'stopwords.jb', compress=3)
    return joblib.load('stopwords.jb')


def Stopwordslist():
    stopwords = [line.strip() for line in open(
        '2022/research/stopWord.txt', encoding='UTF-8').readlines()]
    print(stopwords)
    return stopwords


def no_stopword(words):
    Stopwords = stopword()
    no_stopword = []
    for word in words:
        td = 0
        for sw in Stopwords:
            if word == sw:
                td = -1
                continue
        if td == 0:
            no_stopword.append(word)

    return no_stopword


def calculateTF(serval):
    words = get_words(serval, keep_pos=['名詞'])
    no_words = no_stopword(words)
    tf = Counter(no_words)
    return tf


def takeSecond(elem):
    return elem[1]


def doClustering(vec_df):
    # 階層的クラスタリング（群平均法,コサイン類似度）
    linkage_result = linkage(vec_df, method='average', metric='cosine')
    # コサイン類似度  範囲：-1~1
    threshold = 0.5

    clustered = fcluster(linkage_result, t=threshold, criterion='distance')
    vec_df["cls"] = clustered
    return vec_df

    # dic = defaultdict(list)
    # k = []
    # for i in range(len(wordword_list)):
    #     dic[clustered[i]].append(wordword_list[i])
    # for i in range(1, len(dic)+1):
    #     k.append(dic[i])
    #     # print(i, dic[i])
    # print("cluster:", len(k))


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def get_combine_vic1list(viclist):
    vecvec1_list = []
    Allword_list = []
# 単語リスト
    for page in viclist:
        for v in page:
            if v in Allword_list:
                continue
            else:
                Allword_list.append(v[0])
# ベクトルリスト
    for v in viclist:
        n = len(Allword_list)
        vic = np.zeros(n)
        for i in range(n):
            for vw in v:
                if Allword_list[i] == vw[0]:
                    x = vw.index(Allword_list[i])
                    vic[x] = vw[x][1]
        vecvec1_list.append(vic)
    return vecvec1_list, Allword_list


def getHTMLText(url):
    # Webページのテキストを取り出す
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        req = requests.get(url=url, headers=user_agent, timeout=10)
    except:
        return None
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    bf.prettify()
    return bf.get_text()


def makeTFIDFVector(all_tf, all_word, idf):
    # TFIDFベクトルを生成する
    all_tfidf = {}
    for url in all_tf:
        vector = []
        for word in all_word:
            vector.append(all_tf[url].get(word, 0)*idf.get(word, 0))
        all_tfidf[url] = vector
    return pandas.DataFrame(all_tfidf)


def saveHTML(file_name, html_text):
    file_w = open(str(file_name), "w")
    print(file_w.name)
    file_w.write(html_text)
    file_w.close()


def saveTFIDF(TF_IDF_file, file_name):
    file = open(r"2022//research//TFIDF_Data//"+str(file_name)+".bin", "wb")
    pickle.dump(TF_IDF_file, file=file)
    file.close()


def readTFIDF(file_name):
    df = open(file_name, "rb")
    TFIDF = pickle.load(df)
    df.close()
    return TFIDF


def getAll_word(URLlist):
    all_word = []
    new_URLlist = []
    for URL in tqdm(URLlist):

        texts = getHTMLText(URL)
        if texts is not None:
            all_word.append(texts)
            new_URLlist.append(URL)

    return all_word, new_URLlist


"""
if __name__ == '__main__':

    '''
    URLlist = csv.reader(open("2022//research//urlList.csv"))
    vic = []
    # idf値は全体で同じなので，1回読み込めばいい
    idf = json.loads(open('./2022/research/words_idf.json').read())
    all_tf = {}
    all_word = set()
    #cnt = 1
    for URL in URLlist:
        print(URL[0])
        texts = getHTMLText(URL[0])
        #file_name = '2022//research//saveData//'+str(cnt)+'.txt'
        #saveHTML(file_name, texts)
        tf = calculateTF(texts)
        all_tf[URL[0]] = tf
        all_word = all_word | set(tf.keys())
        #cnt = cnt+1

    all_word = list(all_word)
    df_tfidf = makeTFIDFVector(all_tf, all_word, idf)
    saveTFIDF(df_tfidf, "2022//research//TFIDF_Data//tfidf.bin")
    df_tfidf_with_cluster = doClustering(df_tfidf.T)
    '''
    # df_tfidf保そうする

    # for cor1 in df_tfidf:
    #     for cor2 in df_tfidf:
    #         print(cos_sim(df_tfidf[cor1], df_tfidf[cor2]))

    df_tfidf = readTFIDF("2022//research//TFIDF_Data//tfidf.bin")
    df_tfidf_with_cluster = doClustering(df_tfidf.T)
    print('====クラスタリング結果====')
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    print(df_tfidf_with_cluster['cls'])

    # 平均ベクトルの算出
    df_clustered_tfidf = df_tfidf_with_cluster.groupby("cls").mean()

    # この後に，閲覧履歴とクラスタベクトルの対応を書く

    # for t, f in tf.items():
    #     tfidf.append([t, f*idf.get(t, 0)])
    #     # tfidf={t: f*idf.get(t, 0) for t, f in tf.items()}
    # tfidf.sort(key=takeSecond, reverse=True)
    # print(tfidf)

    # loc = []
    # for i in range(10):
    #     loc.append(tfidf[i])
    # vic.append(loc)
    # print(loc)
    # print("\n")
    # sample_a(loc, idf)
    # victol, allword = get_combine_vic1list(vic)
    # print(victol)
    # print(allword)

    # sample_a(vicl)
    '''
    URL='https://www3.nhk.or.jp/news/special/coronavirus/data/'
    req=requests.get(url=URL)
    req.encoding='utf-8'
    html=req.text
    bf=BeautifulSoup(html,'html.parser')
    bf.prettify()

    texts=bf.get_text()
    tf,idf=get_sample(texts)
    tfidf =[]
    for t, f in tf.items():
        tfidf.append([t,f*idf.get(t, 0)])
        # tfidf={t: f*idf.get(t, 0) for t, f in tf.items()}
    tfidf.sort(key=takeSecond,reverse=True)
    loc=[]
    for i in range(10):
        loc.append(tfidf[i])
    print (loc)

    print("\n")
    '''
    '''
        sample=np.array(texts)
        vectorizer = TfidfVectorizer(
                           max_df=0.9,
                           min_df=5,
                           max_features=1280,
                           tokenizer=mecaber.parse,
                           stop_words=['ann0'],
                           analyzer='word',
                           ngram_range=(1, 1))

            # フィッティング                           
            vectorizer.fit(sample)

            # ベクトルに変換
            tfidf = vectorizer.transform(sample)
    '''
"""
