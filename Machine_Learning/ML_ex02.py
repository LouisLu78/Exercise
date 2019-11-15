'''The following codes are copied from textbook.

import os, sys
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)

# content = ["How to format my hard disk", " Hard disk format problems "]
# X = vectorizer.fit_transform(content)
# print(vectorizer.get_feature_names())
# print(X.toarray().transpose())
posts = [open(os.path.join('.\\DIR', f)).read() for f in os.listdir('.\\DIR')]
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
print(vectorizer.get_feature_names())
print(X_train.toarray())

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print(new_post_vec)
print(new_post_vec.toarray())

import scipy as sp
def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

def dist_norm(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = 100
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_norm(post_vec, new_post_vec)
    print("=== Post %i with dist=%.2f: %s" % (i, d, post))
    if d<best_dist:
        best_dist=d
        best_i=i
print("Best post is %i with dist=%.2f" %(best_i, best_dist))'''

from sklearn.feature_extraction.text import CountVectorizer
import nltk.stem

english_stemmer= nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedCountVectorizer(min_df=1, stop_words = 'english')

import os
posts = [open(os.path.join('.\\DIR', f)).read() for f in os.listdir('.\\DIR')]
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
print(vectorizer.get_feature_names())
print(X_train.toarray())

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print(new_post_vec)
print(new_post_vec.toarray())

import scipy as sp


def dist_norm(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = []
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_norm(post_vec, new_post_vec)
    print("=== Post %i with dist=%.2f: %s" % (i, d, post))
    best_dist.append((i,d))

min_dist=min(item[1] for item in best_dist)
for item in best_dist:
    if item[1]==min_dist:
        (best_i, best_d) = item
print("Best post is %i with dist=%.2f" %(best_i, best_d))

# import math
# def tfidf(term, doc, docset):
#     tf = float(doc.count(term))/sum(doc.count(w) for w in docset)
#     idf = math.log(float(len(docset))/(len([doc for doc in docset if term in doc])))
#     return tf * idf
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# class StemmedTfidfVectorizer(TfidfVectorizer):
#     def build_analyzer(self):
#         analyzer = super(TfidfVectorizer, self).build_analyzer()
#         return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
#
# vectorizer = StemmedTfidfVectorizer(min_df=1, stop_words='english', charset_error='ignore')