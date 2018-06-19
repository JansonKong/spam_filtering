from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import jieba
import os
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

os.chdir('_normal')
lines=[]
for file in os.listdir():
    lines+=LineSentence(file)

model = Word2Vec(lines, size=100)  # 训练skip-gram模型; 默认window=5


os.chdir('..')

model.save('save.model')



