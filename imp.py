def rea(f):
    lines = []
    with open(f) as d:
        lines = d.readlines()[8:]
    return lines


def wor(lines):
    orde = {}
    for line in lines:
        words = line.split('\t')
        wo = words[3]
        if wo in orde:
            orde[wo] += 1
        else:
            orde[wo] = 1
    return orde
def main():
    lines = rea('C:/Users/student/Desktop/81A_tab.txt')
    w = wor(lines)
    for wo in w:
        print(wo, w[wo])
main()
    
