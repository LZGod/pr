import os
import re
i = 0
start = 'bbc'
names = os.listdir(start)
for name in names:
    path_to_file = os.path.join(start, name)
    if os.path.isdir(path_to_file):
        match = re.search('[a-z]+', name)
        match2 = re.search('[а-я]+', name)
        if match and match2:
            print(name)
            i += 1
print(i)
