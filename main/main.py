import random
import time
"""
Rating = []
"""
f = open('res.txt', 'r')
Rating = [i for i in f]
Temp = []
for i in range(len(Rating)):
    s = Rating[i]
    Temp.append(int(s[7:8]))

n = len(Temp)
for i in range(0, n-1):
    for j in range(n - 1):
        if Temp[j] > Temp[j + 1]:
            Temp[j], Temp[j + 1] = Temp[j + 1], Temp[j]
            Rating[j], Rating[j + 1] = Rating[j + 1], Rating[j]

def is_valid(a, key, Dip):
    if a == key:
        return True
    if a < key:
        Dip[0] = a
        print("Ваше число мало, возьмите больше", Dip)
    if a > key:
        Dip[1] = a
        print("Ваше число слишком большое, возьмите меньше", Dip)



print("Добро пожаловать в мою игру: 'Числовая угодайка' ")
while True:
    print("\n\ncase 1: Start game\ncase 2: Restart game\ncase 3: Results table\ncase 0: Exit")
    case = input("case: ")
    print("\n")

    if case == "2":
        case = "1"

    if case == '3':
        for i in range(len(Rating)):
            print(str(i+1)+')', Rating[i])

    if case == '1':
        score = 0
        key = random.randint(1, 100)
        print("Компьютер загадал число, игра началась.")

        Diapason = [1, 100]
        x = int(input("Введите число: "))
        score += 1
        while is_valid(x, key, Diapason) != True:
            x = int(input("Введите число: "))
            score += 1
        print("Поздравляем, вы нашли загаданное число!", 'ваши очки: ', score)
        res = 'score: ' + str(score) + '  date: ' + time.ctime()
        Rating.append(res)

    if case == '0':
        f = open('res.txt', 'w')
        for i in Rating:
            f.write(i + '\n')
        break