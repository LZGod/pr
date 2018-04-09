import re
linen = []
def main():
    with open("qq.txt", encoding="utf-8") as f:
        text = f.readlines()
        for line in text:
            if "Птиц" or "Птица" or "Птицу" or "Птицы" or "Птице" or "Птицей" or "Птицами" or "Птицам" or "Птицах" in line:
                liner = re.sub('Птиц','Рыб', line)
            else:
                liner = re.sub('птиц','рыб', line)
            linen.append(liner)
    with open("qq.txt", "w", encoding="utf-8") as f:
        for liner in linen:
            f.write(str(liner))
if __name__ == '__main__':
    main()
