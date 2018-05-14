import re
def get_data(filename):
    raw = ''
    with open(filename) as f:
        raw = f.read()
    print(raw[:50])
    return raw
def preprocess(text):
    tokens = text.split()
    tokens = [word for word in tokens if len(word) > 2]
    bigrams = [tokens[i:i+2] for i in range(len(tokens))]
    return bigrams
def count_freq(tokens):
    print('В файле {} слов'.format(len(tokens)))
    
