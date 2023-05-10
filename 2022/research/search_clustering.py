import pickle
from search import searchGoogleAPI
from search import make_search_results
from vectorization import SentenceBertJapanese
from vectorization import requestForUrl
import numpy as np

import csv
import pandas


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


if __name__ == '__main__':
    # User search result vectorization

    target_keyword = "LaMDA"
    useWebCache = False  # 新たに検索する時はこれをFalseにする．検索結果を再利用する場合はTrueにする
    useBERTCache = False  # BERTベクトル生成まで終わっているならTrueにする
    if useWebCache:
        U_list = pandas.read_csv(
            'data/results/results_20230228.tsv', sep='\t', header=0, index_col='no')
        URLlist = U_list['link']
        name_List = U_list['title']
    else:
        results = searchGoogleAPI.getSearchResponse(target_keyword)
        make_search_results.makeSearchResults()

        URLlist = []
        name_List = []
        for res in results["response"]:
            for r in res["items"]:
                URLlist += [r["link"]]
                name_List += [r['title']]

    if useBERTCache:
        all_SentenceBert = requestForUrl.readTFIDF(
            "2022/research/SentenceBert_Data/SentenceBert12_1.bin")
    else:
        print("検索結果ページのテキスト取得開始")
        All_Word, URLlist = requestForUrl.getAll_word(URLlist=URLlist)
        # 取得できなかったURLを除外して上書きしている

        All_Word = [a[:10000] for a in All_Word]
        # 巨大すぎるテキストは10000字までにする

        print("SentenceBERTベクトルの作成開始")
        all_SentenceBert = SentenceBertJapanese.getAll_SentenceBert(
            URLlist=URLlist, Allword=All_Word)

    file = open(r"2022/research/SentenceBert_Data/SentenceBert12_1.bin", "wb")
    pickle.dump(all_SentenceBert, file=file)
    file.close()
    '''
    '''

    all_SentenceBert = requestForUrl.readTFIDF(
        "2022/research/SentenceBert_Data/SentenceBert12_1.bin")

    all_SentenceBert = pandas.DataFrame(all_SentenceBert)
    average_SentenceBert = np.mean(all_SentenceBert.T, axis=0)

    # get browsing record clustering
    record_SentenceBert = requestForUrl.readTFIDF(
        "2022/research/SentenceBert_Data/SentenceBert01.bin")
    record_SentenceBert = pandas.DataFrame(record_SentenceBert)
    SentenceBert_with_cluster = requestForUrl.doClustering(
        record_SentenceBert)

    Clustering = SentenceBertJapanese.getClustering(SentenceBert_with_cluster)
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    # 平均ベクトルの算出
    clustered_SentenceBert = Clustering.groupby("cls").mean()
    grouped = Clustering.groupby("cls")

    for index, row in grouped:
        # 输出行的索引（它就是行的id）
        print("Row id:", index, row[0])
    # 输出行的内容

    all_SentenceBert = all_SentenceBert.T
    for clsClustering in clustered_SentenceBert.T:
        v_all = clustered_SentenceBert.loc[clsClustering]
        cosAll = cos_sim(average_SentenceBert, v_all)
        # print(cosAll)
        if cosAll < 0.6:
            for i in range(0, len(all_SentenceBert)):
                v1 = all_SentenceBert.iloc[i]
                cos_c = cos_sim(v1, v_all)
                if cos_c > 0.3:
                    print(v1.name, ' ', clsClustering, ' ', cos_c)
