def rea(q):
    with open(q) as d:
        lines = d.readlines()
    return lines

def cha(a):
    ch = {}
    lines = rea(a)
    for line in lines[1:]:
        p = line.split(',')
        if len(p) > 3:
            name = p[2]
            val = ','.join(p[3:])
            val = val[1:]
            if name in ch:
                ch[name] = ch[name] + '\n' + val
            else:
                ch[name] = val
    return ch
def fr(per, ct):
    fr = {}

def main():
    w = cha("all.txt")
    tl = {}
    for charac in w:
        if charac not in tl:
            tl[charac] = len(w[charac])
    mp = tl.items()
    m = []
    for name, length in mp:
        m.append([length, name])
    m = sorted(m, reverse = True)[:20]
    mn = []
    for length, name in m:
        mn.append(name)
    print(mn)
for charac in mn:
    fr()
    
if __name__ == '__main__':
    main() 
