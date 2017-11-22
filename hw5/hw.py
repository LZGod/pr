print("Hey you, out there in the cold, getting lonely, getting old, would you show file?")
y = input()
j = 0
with open(y, encoding="utf-8") as f:
    text = f.read()
lines = text.splitlines()
print("Всего строк:", len(lines))
for line in lines:
    if len(line.split())>5:
        j = j+1
print("Строк длиннее 5 слов:", j)
p = (j/len(lines))*100
print(p,"%")
