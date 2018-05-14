import re
a = [i**2 for i in [1,2,3,4]]
b = ''.join([sym+' ' for sym in 'abcdf'])   
c = [word.title() for word in 'на улице смерть'.split()]
dict = {i: i**2 for i in [1,2,3,4]}
e = [(item[1], item[0])for item in dict.items()]
# e = [item[::1] for item in dict.items()]
f = [i for i in range(3, 19, 2)]
f2 = [i for i in range(3, 19) if i%2==0]
g = [word if word.istitle() else '_'+word+'_' for word in 'Алиса в Стране Чудес'.split()]
g2 = [word for word in 'Алиса в Стране Чудес'.split() if len(word)>3]
g3 = [word for word in 'Алиса в Стране Чудес'.split() if len(re.findall('[аыеуяиоэАЕИЯЫУЭЮ]', word))>3]
print(g3)
