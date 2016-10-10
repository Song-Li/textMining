import json

class FileOperations:
    def __init__(self, file_name):
        self.file_name = file_name
        f = open(file_name, 'r')
        self.text = f.read()

    def get_json(self):
        jsons = []
        lines = self.text.split('\n');
        for line in lines:
            try:
                jsons.append(json.loads(line))
            except:
                pass
        return jsons

    def normalize(self):
        self.text = self.text.lower()

    def tokenize(self):
        pass



fo = FileOperations("input.json")
fo.normalize()
print fo.get_json()[0]
