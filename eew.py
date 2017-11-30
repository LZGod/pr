def t(a):
    u = 0
    with open(a) as b:
        t = b.readlines()
        ll = []
    for line in t:
        c = line.strip()
        if c:
            print(len(c), c)
            ll.append(len(c))
    return min(ll)
k = input()
lin = t(k)
print(lin)
