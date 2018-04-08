i = 0
import collections
import re
freq = {}
with open("new 1.txt", encoding="utf-8") as f:
    text = f.read()
    t = re.search("\w+\s\w+\s\w+\s\w+[аго]\s\w+[а]\s\w+\s\w+\s\w+", text)
    if t:
        print(t.group())
    else:
        print("none found")
    splited_text = text.split()
    for word in splited_text:
        i = i+1
    words = splited_text
    counter = collections.Counter(words)
print(counter)
print(i)

    
