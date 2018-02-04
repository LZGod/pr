def rea(f):
    with open(f) as d:
        w = d.read()
        words = w.split()
    return words
#выдаёт список слов из текста в файле
def d(a):
    words = rea(a)
    unw = []
    for word in words:
        if len(word) > 1 and word[0] == 'u' and word[1] == 'n':
            unw.append(word)
    return unw
#составляет список слов на "un"
def am(a, e):
    un = d(a)
    fin = 0
    f = 0
    t = len(un)
    for u in un:
        if len(u) > e:
            fin = fin + 1
    if t != 0:
        f = (fin / t)* 100
    print('vsego:', t)
    print('dolya:', f,'%')
#считает количество элементов списка и ищет % слов на "un" короче e букв(е вводит пользователь)   
def main():
    e = int(input())
    am("ment.txt", e)
    
if __name__ == '__main__':
    main()
