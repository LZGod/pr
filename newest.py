import re
def get_data(file_name):
    ''' прочесть содержимое файла '''
    with open(file_name, encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text

def n1(text):
    i = 0
    j = 0
    f = 0
    for line in text:
        for "<w>" and "</w>" in line:
            j = j + 1
        ifor "<ana>" in line:
            i = i + 1
    f = i/j
    print(f)
def pos_freq(text):
    '''  '''
    pos = re.findall(r'gr="([A-Z-]+)\W', text)
    pos_freq_d = {p: pos.count(p) for p in pos}
    return pos_freq_d

def dict_to_file(freq_dict):
    with open('pos_freq.tsv', 'w') as f:
        f.write("POS\tFrequency\n")
        for p in freq_dict:
            f.write(p + '\t' + str(freq_dict[p]) + '\n')
    print('Done.')

if __name__ == '__main__':
    raw = get_data("karenina.xml")
    freq = pos_freq(raw)
    dict_to_file(freq)
    n1(raw)
#    print(raw[:1000])
