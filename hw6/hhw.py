print("Тернистый путь к файлу")
x = input()
print("8 слов")
y = input()
l = y.split()
if len(l)<8:
    print("Game over")
else:
    with open(x, "w") as f: 
        f.write(l[0]+l[1]+'\n')
        f.write(l[2]+l[3]+'\n')
        f.write(l[4]+l[5]+'\n')
        f.write(l[6]+l[7])
    
