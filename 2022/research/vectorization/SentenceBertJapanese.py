import csv
import math
import pickle
from bs4 import BeautifulSoup
import joblib
import pandas
import requests
from transformers import BertJapaneseTokenizer, BertModel
import torch
from janome.tokenfilter import POSKeepFilter, POSStopFilter
from janome.analyzer import Analyzer
import numpy as np
from collections import Counter, defaultdict
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
#from vectorization import requestForUrl
import re
from tqdm import tqdm


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


class SentenceBertJapanese:
    def __init__(self, model_name_or_path, device=None):
        self.tokenizer = BertJapaneseTokenizer.from_pretrained(
            model_name_or_path)
        self.model = BertModel.from_pretrained(model_name_or_path)
        self.model.eval()

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device)
        self.model.to(device)

    def _mean_pooling(self, model_output, attention_mask):
        # First element of model_output contains all token embeddings
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(
            -1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    @torch.no_grad()
    def encode(self, sentences, batch_size=8):
        all_embeddings = []
        iterator = range(0, len(sentences), batch_size)
        for batch_idx in iterator:
            batch = sentences[batch_idx:batch_idx + batch_size]
            encoded_input = self.tokenizer.batch_encode_plus(batch, padding="longest",
                                                             truncation=True, return_tensors="pt").to(self.device)
            model_output = self.model(**encoded_input)
            sentence_embeddings = self._mean_pooling(
                model_output, encoded_input["attention_mask"]).to('cpu')

            all_embeddings.extend(sentence_embeddings)

        # return torch.stack(all_embeddings).numpy()
        if len(all_embeddings) == 0:
            return torch.zeros(1, 100)

        return torch.stack(all_embeddings)


def readFile(File_name):
    with open(str(File_name), "r") as f:
        data = f.read()
    f.close()
    return data


def getSentenceBert(data, model):
    sentence_embeddings = model.encode(data, batch_size=8)
    return sentence_embeddings


def splitLongText(text, length=800):
    n = math.ceil(len(text) / length)  # 分割数を決める
    if n == 0:
        return text
    m = math.ceil(len(text) / n)  # 文字数を決める
    return [text[idx: idx + m] for idx in range(0, len(text), m)]


def encodeSplittedText(text, model):
    text_list = splitLongText(text)
    return np.mean(model.encode(text_list).numpy(), axis=0)


def saveSentenceBert(SentenceBert_File, f_name):
    #file = open(r"2022/research/SentenceBert_Data/SentenceBert01.bin", "wb")
    file = open(r""+f_name, "wb")
    pickle.dump(SentenceBert_File, file=file)
    file.close()


def doClustering(vec_df):
    # 階層的クラスタリング（群平均法,コサイン類似度）
    linkage_result = linkage(vec_df, method='average', metric='cosine')
    # コサイン類似度  範囲：-1~1
    threshold = 0.6

    clustered = fcluster(linkage_result, t=threshold, criterion='distance')
    vec_df["cls"] = clustered
    return vec_df


def getClustering(vec_SentenceBert):
    all_SentenceBert = pandas.DataFrame(vec_SentenceBert)
    SentenceBert_with_cluster = doClustering(
        all_SentenceBert.T)
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    return (SentenceBert_with_cluster)


def getAll_SentenceBert(URLlist, Allword):
    MODEL_NAME = "sonoisa/sentence-bert-base-ja-mean-tokens-v2"  # &lt;- v2です。
    model = SentenceBertJapanese(MODEL_NAME)
    all_SentenceBert = {}
    cnt = 0
    for URL in tqdm(URLlist):
        texts = Allword[cnt]
        SentenceBert = encodeSplittedText(texts, model)
        all_SentenceBert[URL] = SentenceBert
        cnt = cnt+1
    all_SentenceBert = pandas.DataFrame(all_SentenceBert)
    return all_SentenceBert


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


def getHTMLText(url):
    # Webページのテキストを取り出す
    user_agent = {'User-agent': 'Mozilla/5.0'}
    req = requests.get(url=url, headers=user_agent, timeout=10)
    if req.status_code != 200:
        return None
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    # bf.prettify()
    text = bf.get_text()
    # words = get_words(text, keep_pos=['名詞'])
    # no_words = no_stopword(words)
    # tf = Counter(no_words)
    # text = no_stopword(text)
    text = re.sub('\n+', '\n', text)  # 無意味な改行が多いので改行を1つにまとめる
    return text


def doClustering(vec_df):
    # 階層的クラスタリング（群平均法,コサイン類似度）
    linkage_result = linkage(vec_df, method='average', metric='cosine')
    # コサイン類似度  範囲：-1~1
    threshold = 0.5

    clustered = fcluster(linkage_result, t=threshold, criterion='distance')
    vec_df["cls"] = clustered
    return vec_df


if __name__ == '__main__':
    #File_name = "2022//research//saveData//1.txt"
    MODEL_NAME = "sonoisa/sentence-bert-base-ja-mean-tokens-v2"  # &lt;- v2です。
    model = SentenceBertJapanese(MODEL_NAME)

    URLlist = csv.reader(open("2022//research//experiment_Data//30.csv"))

    #data = readFile(File_name)
    #sentence_embeddings = getSentenceBert(data, MODEL_NAME)
    all_SentenceBert = {}
    #all_word = set()
    # cnt = 1
    for URL in URLlist:
        if URL == None:
            continue
        print(URL[0])

        #file_name = '2022//research//saveData//01_1'+str(cnt)+'.txt'
        #texts = readFile(file_name)
        texts = getHTMLText(URL[0])
        # print(texts)
        if texts is None:
            continue
        SentenceBert = encodeSplittedText(texts, model)
        all_SentenceBert[URL[0]] = SentenceBert
        # all_word = all_word | set(SentenceBert.keys())
        # cnt = cnt+1

    #all_word = list(all_word)
    saveSentenceBert(all_SentenceBert,
                     "2022/research/SentenceBert_Data/SentenceBert01.bin")

    # all_SentenceBert = requestForUrl.readTFIDF(
    #    "2022/research/SentenceBert_Data/SentenceBert.bin")
    all_SentenceBert = pandas.DataFrame(all_SentenceBert)
    SentenceBert_with_cluster = doClustering(all_SentenceBert.T)

    print('====クラスタリング結果====')
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    print(SentenceBert_with_cluster['cls'])

    # 平均ベクトルの算出
    clustered_SentenceBert = SentenceBert_with_cluster.groupby("cls").mean()

    #print("Sentence embeddings:", sentence_embeddings)
