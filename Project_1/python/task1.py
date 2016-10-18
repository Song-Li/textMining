import json
from FileOperations import FileOperations 
from sklearn.naive_bayes import MultinomialNB
import scipy

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

clf_bayes = fo.train_bayes_model(train_data,train_lable)
fo.score(clf_bayes, test_data, test_lable)

clf_rocchio = fo.train_rocchio_model(train_data,train_lable)
fo.score(clf_rocchio, test_data, test_lable)

