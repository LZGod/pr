def get():
    with open("C:/Users/student/Documents/sample_tagged_text.txt", encoding = 'utf-8') as f:
        w = f.read()
        return w
def tok(w):
    words = w.split()
    return words
def ext(words):
    ll = []
    for i, token in enumerate(words):
        mem = token.split('_')
        word = mem[0]
        pos = mem[-1]
        if pos == 'A':
            n = words[i + 1]
            if n.endswith('_S'):
                ll.apped(word + '' + n[:-2])
def writ(e, nam):
    with open(nam, 'w') as f:
        for d in e:
            f.write(d + '/n')
def main():
    r = get()
    takk = tok(r)
    e = ext(takk)
    for entry in e:
        print(entry)
    writ(e,'fule.txt')
main()
    
