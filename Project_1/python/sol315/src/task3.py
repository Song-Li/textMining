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

origin = FileOperations("../input.json")
origin.get_json()

stop = set(stopwords.words('english'))

pairs = dict()
attributes = dict()
regex = re.compile('[^a-zA-Z]')

#this for loop is only used for get the attributes of task 2
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

#sort the attributes and keep the first 50
attributes = sorted(attributes.items(), key = operator.itemgetter(1), reverse = True)[:50]
#remove the number
attributes = [attr[0] for attr in attributes]

sentence = dict()

for i in range(len(tages)):
    line = tages[i]
    for j in range(len(line)):
        tag = line[j]
        if tag[0] not in attributes:
            continue
        if tag[1] == 'NN' or tag[1] == 'NNS':
            tag[0] = regex.sub('', tag[0]).lower()
            if tag[0] in stop or len(tag[0]) <= 1:
                tag[1] = 'STOP'
            else:
                dis = 1e5
                res = -1
                for k in range(len(line)):
                    tagJJ = line[k]
                    #only keep the nearest JJ. The distance will be abs(k - j)
                    if tagJJ[1] == 'JJ' and tagJJ[0] != 'other':# or tagJJ[1] == 'JJR' or tagJJ[1] == 'JJS':
                        if abs(k - j) < dis:
                            res = k
                            dis = abs(k - j)

                if res != -1:
                    tagJJ = line[res]
                    pair = tag[0] + ',' + tagJJ[0]
                    if pair in pairs:
                        pairs[pair] += 1
                    else:
                        pairs[pair] = 1
                    if pair not in sentence:
                        sentence[pair] = origin.reviews[i]

pairs = sorted(pairs.items(), key = operator.itemgetter(1), reverse = True)

for pair in pairs[:50]:
    print '(' + pair[0] +'),1,"' + sentence[pair[0]]  + '"'
