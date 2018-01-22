d = {'kot':{'name': 'kotae', 'age': 20}}
e = type(d)
d['gog'] = 'geg'
for p in d:
    if 'age' in d[p]:
        print(p, '->', d[p]['age'])
    else:
        print('no age for', d[p])
print(list(d.keys()))

