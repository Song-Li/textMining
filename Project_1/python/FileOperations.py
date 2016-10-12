import json
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors.nearest_centroid import NearestCentroid
import scipy
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class FileOperations:
    def __init__(self, file_name):
        self.file_name = file_name
        f = open(file_name, 'r')
        self.text = f.read()

    def get_json(self):
        print "Loading json..."
        self.jsons = []
        self.reviews = []
        lines = self.text.split('\n');
        for line in lines:
            try:
                self.jsons.append(json.loads(line))
                self.reviews.append(json.loads(line)['reviewtext'])
            except:
                pass
        self.num_lines = len(self.jsons)
        return self.jsons

    def normalize(self):
        print "Normalizing..."
        self.text = self.text.lower()

    def tokenize(self, raw):
        stemmer = PorterStemmer()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(raw)
        stems = [stemmer.stem(word) for word in tokens]
        return stems

    def get_tfidf(self):
        print "Getting TF-IDF..."
        tfidf = TfidfVectorizer(tokenizer=self.tokenize, stop_words='english')
        tfs = tfidf.fit_transform(self.reviews)
        print tfs.shape
        return tfs

    def get_value(self):
        y = []
        for line in self.jsons:
            if int(line['overall']) > 3:
                y.append(1)
            else:
                y.append(0)
        return y

    def train_bayes_model(self, X, y):
        print "Training Bayes model..."
        clf = MultinomialNB()
        clf.fit(X,y)
        return clf

    def score(self, clf, X, y):
        print "Predicting..."
        print clf.score(X,y)

    def train_rocchio_model(self, X, y):
        print "Training Rocchio model..."
        clf = NearestCentroid()
        clf.fit(X,y)
        return clf

