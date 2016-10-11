import json
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

class FileOperations:
    def __init__(self, file_name):
        self.file_name = file_name
        f = open(file_name, 'r')
        self.text = f.read()

    def get_json(self):
        print "Loading json..."
        self.jsons = []
        lines = self.text.split('\n');
        for line in lines:
            try:
                self.jsons.append(json.loads(line))
            except:
                pass
        return self.jsons

    def normalize(self):
        print "Normalizing..."
        self.text = self.text.lower()

    def tokenize(self):
        print "Tokenizing..."
        self.tokens = []
        self.all = []
        stop = stopwords.words('english')
        
        tokenizer = RegexpTokenizer(r'\w+')
        for line in self.jsons:
            self.tokens.append([words for words in tokenizer.tokenize(line['reviewtext']) if words not in stop])
        self.all_tokens = list(set(word for words in self.tokens for word in words))
        return self.tokens

    def get_freq_dist(self):
        print "Getting frequency..."
        self.freq_dist = nltk.FreqDist(word for words in self.tokens for word in words)
        return self.freq_dist

    def get_line_rate(self, n):
        fdist = nltk.FreqDist(word for word in self.tokens[n])
        print self.jsons[n]
        for word in self.tokens[n]:
            print self.all_tokens.index(word), float(fdist[word]) / float(self.freq_dist[word])
