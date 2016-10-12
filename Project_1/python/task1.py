import json
from FileOperations import FileOperations 
from sklearn.naive_bayes import MultinomialNB
import scipy

fo = FileOperations("../input.json")
fo.normalize()
fo.get_json()
#tokens = fo.tokenize()
fo.get_tfidf()

#print fo.get_freq_dist()
#fo.get_all_rate()
#line = fo.rate_table[0]
#for word in line:
#    if word != 0:
#        print word
#clf = MultinomialNB()
#clf.fit(X,y)
