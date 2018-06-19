import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import numpy as np
import svmdata
import pickle

"""
train test
"""
x_train,x_test,y_train,y_test,num_normal,num_spam = svmdata.data(3,3,0.2)

"""
停用词,词频
"""
stop_words_file = open("stopwords.txt", 'r')
stop_words_content = stop_words_file.read()
stop_words_list = stop_words_content.splitlines()
stop_words_file.close()

count_vect = CountVectorizer(stop_words=stop_words_list, token_pattern=r"(?u)\b\w+\b")
train_count = count_vect.fit_transform(x_train)
print(train_count.shape)
test_count = count_vect.transform(x_test)
print(test_count.shape)

"""
tf-idf chi特征选择
"""
tfidf_trainformer = TfidfTransformer()
train_tfidf = tfidf_trainformer.fit_transform(train_count)
test_tfidf = tfidf_trainformer.transform(test_count)
select = SelectKBest(chi2, k=10000)
# print(X_train_tf.shape)
train_tfidf_chi = select.fit_transform(train_tfidf, y_train)
test_tfidf_chi =select.transform(test_tfidf)
# print(X_train_tf_chi.shape)
# print(X_train_tf_chi)

"""
SVM
"""
print('*************************\nSVM\n*************************')

svclf = SVC(kernel = 'linear')
svclf.fit(train_tfidf, y_train)
print("train accurancy:",svclf.score(train_tfidf, y_train))
train_pre = svclf.predict(train_tfidf)
print(classification_report(train_pre, y_train))
pred_svm = svclf.predict(test_tfidf)
accuracy_svm = np.mean(pred_svm == y_test)
print("test accuracy:", accuracy_svm)
print(classification_report(pred_svm, y_test))

"""
保存模型
"""
with open('svm.pickle', 'wb') as fw:
    pickle.dump(svclf, fw)

with open('count_vect.pickle', 'wb') as fw:
    pickle.dump(count_vect, fw)

with open('tfidf_trainformer.pickle', 'wb') as fw:
    pickle.dump(tfidf_trainformer, fw)

