import re
m = input()
rig = re.search(r'(\+7|8)\d{10}$',m)
if rig:
    print('ya')
else:
    print('no')
