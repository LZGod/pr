import random
def words(a):
    d = {}
    with open(a) as q:
        helper = ''
        for line in q:
            if helper == '':
                word, helper = line.split(',')
            else:
                helper = helper + line
            if line == '\n':
                word_dict = d.setdefault(word, {})
                helper_dict = word_dict.setdefault(helper, {})
                helper_dict.append(helper)
    return d
def main():
    win = {'you win', 'victory', 'congrats'}
    lose = {'you lose', 'oh no', 'no result'}
    w = words("alll.txt")
    o = random.choice(w.key())
    print(o)
    print("Попытайтесь угадать слово(у вас 1 попытка).")
    a = input()
    if a == w[o][0]:
        print(random.choice(win))
    else:
        print(random.choice(lose))    
if __name__ == '__main__':
    main() 

