dict = {i: i**2 for i in [1,2,3,4]}
new_dict = {dict[k]: k for k in dict}
print(new_dict)
f = 'Длина слова {0} равна {1}'.format('мемы', len('мемы'))
print(f)
user = input("Имя мне быстро!")
greet = 'Что тебе надо у меня дома, {}?'.format(user)
print(greet)
r = '{:)<15}'.format('кондиционер')
print(r)
o = '{:0.3f}'.format(1.23456789)
print(o)
