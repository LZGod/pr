import re
def file(a):
    with open(a, encoding = "utf-8") as e:
        f = e.read()
        ans = re.search(r'id=bel">...', f)
        if ans:
            an = ans.group()
            ons = re.sub('id=bel">', '', an)
            return ons
        else:
            print('no')
        
def main():
    f = file('bel.htm')
    with open("otv.txt", "w", encoding="utf-8") as t:
       t.write(f)
if __name__ == '__main__':
    main() 
