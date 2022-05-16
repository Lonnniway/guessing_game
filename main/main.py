import random
import math
s = "100"

def is_valid(s):
    s = str(s)
    if s.isdigit():
        if 0 <= int(s) <= 100:
            return True
        else:
            return False
    else:
        return False



x = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")

if is_valid(x) == False:
    print("Неверно")
else:
    while True:
        res = int(input())
        if res == x:
            break
        elif res > x:
            print("Слишком много, попробуйте еще раз")
        else:
            print("Слишком мало, попробуйте еще раз")
    print("Вы угадали, поздравляем!")