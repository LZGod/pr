import os
def getta(path):
    alls = os.listdir(path)
    print(alls)
def che(path):
    for root, dirs, files in os.walk(path):
        print(root)
        print(dirs)
        print(files[:10])
        print(len(files))
        for name in files:
            file_path = os.path.join(root, name)
            with open(file_path) as f:
                raw = f.read()
                print(raw[:100])
che('./Downloads')
