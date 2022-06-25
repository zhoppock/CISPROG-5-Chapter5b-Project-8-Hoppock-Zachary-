f = open("text.txt", "r")
text = []
for line in f:
    words = line.split()
    for word in words:
      text.append(word)

f.close()

group = {}

for word in text:
  if word not in group:
    group[word] = 1
  else:
    group[word] += 1

for index in sorted(group):
  print("%s %s" % (index, group[index]))