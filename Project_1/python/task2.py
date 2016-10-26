import json
from FileOperations import FileOperations
import nltk
from nltk.tag.stanford import StanfordPOSTagger
from nltk.corpus import stopwords
import operator
import os
import re

# set the java environment variables:
# CLASSPATH is the path to the stanford-postagger.jar in your local disk
# STANFORD_MODELS is the path to the tagger file in your local disk
os.environ['CLASSPATH']='/home/sol315/Downloads/stanford-postagger-2015-12-09/stanford-postagger.jar'
os.environ['STANFORD_MODELS']='./models/english-left3words-distsim.tagger'

fo = FileOperations("taged.data")
tages = fo.get_taged_data()

stop = set(stopwords.words('english'))

attributes = dict()
regex = re.compile('[^a-zA-Z]')

for line in tages:
    for tag in line:
        if tag[1] == 'NN' or tag[1] == 'NNS':
            tag[0] = regex.sub('', tag[0]).lower()
            if tag[0] in stop or len(tag[0]) <= 1:
                tag[1] = 'STOP'
            elif tag[0] in attributes:
                    attributes[tag[0]] += 1;
            else:
                attributes[tag[0]] = 1;

attributes = sorted(attributes.items(), key = operator.itemgetter(1), reverse = True)

for attribute in attributes[:50]:
    print attribute[0] + ',' + str(attribute[1])
