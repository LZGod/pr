import re
w = input()
t = re.search("[аеиоуёэяюы]", w)
if t:
    print("ye", t.group())
else:
    print("no")
