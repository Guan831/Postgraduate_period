
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

docs = np.array([
    '牛乳        を 買う',
    'パン         を 買う',
    'パン         を 食べる',
    'お菓子       を 食べる',
    '本           を 買う',
    'パン と お菓子 を 食べる',
    'お菓子        を 買う',
    'パン と パン   を 食べる'
])

#
# ベクトル化
#
vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
vecs = vectorizer.fit_transform(docs)

clusters = KMeans(n_clusters=2, random_state=0).fit_predict(vecs)
for doc, cls in zip(docs, clusters):
    print(cls, doc)
