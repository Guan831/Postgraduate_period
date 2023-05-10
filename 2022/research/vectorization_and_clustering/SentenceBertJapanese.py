import csv
import math
import pickle
from transformers import BertJapaneseTokenizer, BertModel
import torch
import numpy as np


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
    m = math.ceil(len(text) / n)  # 文字数を決める
    return [text[idx: idx + m] for idx in range(0, len(text), m)]


def encodeSplittedText(text, model):
    text_list = splitLongText(text)
    return np.mean(model.encode(text_list).numpy(), axis=0)


def saveSentenceBert(SentenceBert_File):
    file = open(r"2022/research/SentenceBert_Data/SentenceBert.bin", "wb")
    pickle.dump(SentenceBert_File, file=file)
    file.close()


if __name__ == '__main__':
    #File_name = "2022//research//saveData//1.txt"
    MODEL_NAME = "sonoisa/sentence-bert-base-ja-mean-tokens-v2"  # &lt;- v2です。
    model = SentenceBertJapanese(MODEL_NAME)
    URLlist = csv.reader(open("2022//research//urlList.csv"))
    #data = readFile(File_name)
    #sentence_embeddings = getSentenceBert(data, MODEL_NAME)
    all_tf = {}
    #all_word = set()
    cnt = 1
    for URL in URLlist:
        print(URL[0])
        file_name = '2022//research//saveData//'+str(cnt)+'.txt'
        texts = readFile(file_name)
        SentenceBert = getSentenceBert(texts, model)
        all_tf[URL[0]] = SentenceBert
        #all_word = all_word | set(SentenceBert.keys())
        cnt = cnt+1

    #all_word = list(all_word)
    saveSentenceBert(all_tf)
    #print("Sentence embeddings:", sentence_embeddings)
