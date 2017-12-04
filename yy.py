y = input()
lin = [] 
with open(y, encoding = 'utf-8') as d:
    l = d.readlines()
    for i in l:
        if "2016," in i:
            lin.append(i)        
p = 0
x = input()
for j in lin:
    if x in j:
        v = j.split(',')
        h = float(v[3].strip())
        print(h)
        p = 1
        break
if p == 0:
    print("Nope")
