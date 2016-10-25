import json
from FileOperations import FileOperations
import nltk
from nltk.tag.stanford import StanfordPOSTagger
import os

# set the java environment variables:
# CLASSPATH is the path to the stanford-postagger.jar in your local disk
# STANFORD_MODELS is the path to the tagger file in your local disk
os.environ['CLASSPATH']='/home/sol315/Downloads/stanford-postagger-2015-12-09/stanford-postagger.jar'
os.environ['STANFORD_MODELS']='./models/english-left3words-distsim.tagger'

fo = FileOperations("taged.data")
tages = fo.get_taged_data()


