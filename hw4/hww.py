print("Слово мне, слово! Полцарства за слово!")
a=list(input())
def isstr(a):
    try:
        str(a)
        return True
    except ValueError:
        return False
if isstr(a):
    pass
else:
    print("Миссия провалена. Попробуй ещё раз.")
print("".join(a))
while len(a) > 1:
    y = len(a)
    a.pop(0)
    a.pop(y - 2)
    print("".join(a))
    
    
