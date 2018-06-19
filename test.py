#matrixdata测试
"""
import matrixdata
from gensim.models import Word2Vec

model=Word2Vec.load('save.model')

data=[]

matrixdata.singleData(1,'_normal',data,model)

"""

#svmdata测试
import svmdata

data=[]

x_train,x_test,y_train,y_test,num_normal,num_spam = svmdata.data(25,25,0.2)

print(len(x_train),len(x_test))
print(x_train[0])
