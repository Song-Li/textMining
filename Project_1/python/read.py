import json

f = open('taged.data', 'r')
lines = f.read().split('\n')
for line in lines:
    if line == '':
        break
    r = json.loads(line)
    print r
