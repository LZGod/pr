import re
def get_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    return data
def challenge(data):
    betterdata = re.sub('[—)(,]', ' ', data)
    sents = betterdata.split('.')
    for sent in sents:
        words = sent.split()
        freq = {word: words.count(word) for word in words if int(words.count(word)>=2)}
        for key, value in freq.items():
            print(key, '           ', value)
def main():
    data = get_data("k.txt")
    challenge(data)
if __name__ == '__main__':
    main()
    
    
