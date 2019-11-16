#-*- coding:utf-8 -*-
import os

# path="C:\\Users\\Basanwei\\Downloads\\20news-18828\\talk.politics.mideast"
#
# for file in os.listdir(path):
#     with open(os.path.join(path, file)) as f:
#         res = f.read()
#     with open('fulltext.txt', 'a') as fa:
#         fa.write(res)
# fulltxt=open('fulltext.txt', 'r')
# fullcontent=fulltxt.read()
# print(fullcontent)
# fulltxt.close()

from gensim import corpora, models, similarities

corpus = corpora.BleiCorpus('fulltext.txt')
model = models.ldamodel.LdaModel(corpus, num_topics=100, id2word=corpus.id2word)
topics = [model[c] for c in corpus]
print (topics[0])