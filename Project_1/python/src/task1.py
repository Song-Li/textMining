import json
from FileOperations import FileOperations 
from sklearn.naive_bayes import MultinomialNB
import scipy
import time

fo = FileOperations("../input.json")
fo.get_json()
#fo.normalize()
#tokens = fo.tokenize()
#clf.fit(X,y)
split = fo.num_lines / 100 * 80
data = fo.get_tfidf()
lable = fo.get_value()

train_data = data[:split]
train_lable = lable[:split]
test_data = data[split:]
test_lable = lable[split:]

start = time.time()
clf_bayes = fo.train_bayes_model(train_data,train_lable)
end = time.time()
print "Train Time:" + str(end - start) + 's'
start = time.time()
TP, FP, FN, TN = fo.score(clf_bayes, test_data, test_lable)
end = time.time()
print "Test Time:" + str(end - start) + 's'
print "Accuracy: " , float(TP + TN) / float(TP + FP + FN + TN)
print "precision: " , float(TP) / float(TP + FP) 
print "Call back: " , float(TP) / float(TP + TN) 

start = time.time()
clf_rocchio = fo.train_rocchio_model(train_data,train_lable)
end = time.time()
print "Train Time:" + str(end - start) + 's'
start = time.time()
TP, FP, FN, TN = fo.score(clf_rocchio, test_data, test_lable)
end = time.time()
print "Test Time:" + str(end - start) + 's'
print "Accuracy: " , float(TP + TN) / float(TP + FP + FN + TN)
print "precision: " , float(TP) / float(TP + FP) 
print "Call back: " , float(TP) / float(TP + TN) 


