f = open("./p1_t1.csv", 'r')
text = f.read()
lines = text.split('\n')
for line in lines:
  parts = line.split(',')
  parts[3] = '"' + parts[3] + '"'
  line = parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + parts[3]
  print line
