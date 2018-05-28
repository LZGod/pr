#1 (5 баллов). Посчитайте среднее количество разборов (тэг ana) на слово (тэг w).
#2 (8 баллов). Составьте частотный словарь всех частей речи в тексте. Например: {'APRO': 5, 'S': 277, ...}. Распечайте содержимое словаря в отдельный файл (на каждой строке "часть речи"<табуляция>"частотность").
#3 (10 баллов). Найдите в тексте все существительные в творительном падеже (обратите внимание, что некоторые разборы омонимичные. Если хотя бы один разбор с указанием творительного падежа присутствует, слово берём). Запишите в отдельный файл найденные существительные и контекст их употребления в таком формате:
#3 слова слева<табуляция>найденное существительное<табуляция>3 слова справа.
#За сохранение знаков препинания отдельный плюс
import re
import collections
def get_data(filename):
    with open(filename) as f:
        data = f.readlines()
    return data
#def n1(data):
#    for line in data:
#        if "<w>" and "</w>" in line:
#            vh = re.search(r"<ana>", line)
def n2():
    freq = {}
    for line in data:
        word = re.search(r'gr="([A-Z-]+)\W', line)  
        if word in freq:
            freq[word] += 1 
        else:
            freq[word] = 1 
    return freq
def dict_to_file(freq):
    with open("rr.txt", 'w') as f:
        for p in freq:
            f.write(p+'\t'+str(freq[p])+'\n')
def fr(data):
    pos = re.findall(r'gr="([A-Z-]+)\W', data)
    freq = {p:pos.count(p) for p in pos}
    return freq
if _name_=='_main_':
    raw = get_data("")
    freq = n2(raw)
    dict_to_file(freq)
