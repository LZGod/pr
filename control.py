o = 0
m = []
for i in range(0, 1000):
    r = input()
    if r != '':
        m.append(r)
    else:
        break
w = []
with open("C:/Users/student/Documents/quotes.txt", encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split('—')
        w = words[0].split()
        if len(w) <= 10  and len(w[0]) < 5:
            print(w)
    print('')
    print("Слово есть в цитатах вот этих людей:")
    for line in lines:
        words = line.split('—')
        w = words[0].split()
        if "разум" in w:
            print(words[1]+'.')
    print('')
    for line in lines:
        words = line.split('—')
        w = words[0].split()
        for i in range(0, len(m)):
            if m[i] in w:
                print("Слово "+m[i]+" встречается:"+words[1]+"    "+words[0])
                print('')
                o = 1
        if o == 0:
            print("Увы, цитат со словом нет. Совсем. Но вы не расстраивайтесь.")
                
            
        
            
        
