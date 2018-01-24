import random
def rea(f):
    lines = []
    with open(f) as d:
        lines = d.readlines()
        for line in lines:
            words = line.split(' ')
    return words


def adj_abl(a):
    words = rea(a)
    return random.choice(words)
#возвращает прилагательное в творительном падеже(2 слога)

def noun_abl(a):
    words = rea(a)
    return random.choice(words)
#возвращает существительное в творительном падеже(3 слога)

def short_adv(a):
    words = rea(a)
    return random.choice(words)
#возвращает краткое причастие женского рода(3 слога)

def noun_1(a):
    words = rea(a)
    return random.choice(words)
#возвращает существительное женского рода(2 слога)

def noun_plus_v(a):
    words = rea(a)
    word = random.choice(words)
    return 'в' + ' ' + word
#возвращает предлог "в" и существительное множественного числа в предложном падеже(2 слога)

def verb_1sg(a):
    words = rea(a)
    return random.choice(words)
#возвращает глагол 1 лица единственного числа(2 слога)

def noun_plus_pod(a):
    words = rea(a)
    word = random.choice(words)
    return 'под' + ' ' + word
#возвращает предлог "под"(1 слог) и существительное в творительном падеже(2 слога)

def noun_2(a):
    words = rea(a)
    return random.choice(words)
#возвращает существительное мужского рода(1 слог)

def noun_pl_plus_po(a):
    words = rea(a)
    word = random.choice(words)
    return 'по' + ' ' + word
#возвращает предлог "по"(1 слог) и существительное множественного числа в дательном падеже(3 слога)

def verb_perf(a):
    words = rea(a)
    return random.choice(words)
#возвращает совершенный глагол мужского рода(2 слога)

def noun_3(a):
    words = rea(a)
    return random.choice(words)
#возвращает существительное множественного числа(2 слога)

def verb_done_pl(a):
    words = rea(a)
    return random.choice(words)
#возвращает совершенный глагол множественного числа будущего времени(3 слога)

def str_1():
    return adj_abl("adj_abl.txt") + ' ' + noun_abl("noun_abl.txt")


def str_2():
    return short_adv("short_adv.txt") + ' ' + noun_1("noun_1.txt") + ' ' + noun_plus_v("noun_plus_v.txt") + '.'


def str_3():
    return verb_1sg("verb_1sg.txt") + ', ' + noun_plus_pod("noun_plus_pod.txt")


def str_4():
    return noun_2("noun_2.txt") + ' ' + noun_pl_plus_po("noun_pl_plus_po.txt") + ' ' + verb_perf("verb_perf.txt") + '...'


def str_5():
    return 'Значит, ' + noun_3("noun_3.txt") + ' ' + verb_done_pl("verb_done_pl.txt")


def main():
    print(str_1() + '\n' + str_2() + '\n' + str_3() + '\n' + str_4() + '\n' + str_5() + '.')


if __name__ == '__main__':
    main()

