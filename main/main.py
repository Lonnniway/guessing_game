import random

def is_valid(a, key):
    if a == key:
        return True
    if a < key:
        print("Ваше число мало, возьмите больше.")
    if a > key:
        print("Ваше число слишком большое, возьмите меньше.")

print("Добро пожаловать в мою игру: 'Числовая угодайка' ")
while True:
    print("case 1: Start game\ncase 2: Restart game\ncase 0: Exit")
    case = input("case: ")
    print("\n")

    if case == "2":
        case = "1"

    if case == '1':
        key = random.randint(1, 100)
        print("Компьютер загадал число, игра началась.")

        x = int(input("Введите число: "))
        while is_valid(x, key) != True:
            x = int(input("Введите число: "))
        print("Поздравляем, вы нашли загаданное число!")

    if case == '0':
        break