import json
from FileOperations import FileOperations 

fo = FileOperations("../input.json")
fo.normalize()
fo.get_json()
fo.tokenize()[0]
print fo.get_freq_dist().most_common(20)

