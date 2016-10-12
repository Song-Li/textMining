import json
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer

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
        tokens = nltk.word_tokenize(raw)
        stems = [stemmer.stem(word) for word in tokens]
        return stems

    def get_tfidf(self):
        print "Getting TF-IDF..."
        tfidf = TfidfVectorizer(tokenizer=self.tokenize, stop_words='english')
        tfs = tfidf.fit_transform(self.reviews)
        print len(tfs)

