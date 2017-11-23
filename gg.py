y = input()
s ="all work and no play makes Jack a dull boy"
words = s.split()
l = []
for i in range(len(words)):
    if i%2!=0:
        l.append(words[i].upper())
    else:
        l.append(words[i].lower())
with open(y, "w") as d:
    for j,w in enumerate(l):
        j = str(j)
        d.write(j+" "+w+'\n')
