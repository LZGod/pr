import re

with open("C:/Users/student/Desktop/yy.html", encoding = "utf-8") as f:
    te = f.read()
#links = re.findall('<a.*?href="(http.*?)">', te)
#for link in links:
#    print(link)
main = re.findall('mw-content-text.*?>(.*)', te)[0]
print(main[:100])
pars = re.findall('<p>(.*?)</p>', main)
for p in pars:
    print(p)
