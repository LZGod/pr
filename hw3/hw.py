print("О, великий и могучий Пользователь, мы пали ниц пред Твоим величием. Пощади нас убогих и введи натуральное число.")
a = input()
def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
if isint(a):
    pass
else:
    print("Миссия провалена. Попробуй ещё раз.")
a = int(a)
b=2
if a < 0:
    print("Миссия провалена. Попробуй ещё раз.")
elif b > a:
    print("Увы, a меньше b. Попробуй ещё раз.")
while b <= a:
  print(b)
  b = b*2

