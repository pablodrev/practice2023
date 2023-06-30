import random

colors = ["Синий", "Зеленый", "Красный", "Оранжевый", "Фиолетовый"]
print("Номера цветов: ")
for i in range(len(colors)):
    print(str(i+1) + ". " + colors[i])

correct = random.randint(1, len(colors))
while True:
    guess = int(input("Угадайте цвет (введите номер): "))
    if guess == correct:
        print("Вы угадали!")
        break
    else:
        print("Вы не угадали. Подсказка: ")
        if correct == 1:
            print("Этот цвет есть на логотипе Python")
        elif correct == 2:
            print("Яблоки бывают такого цвета")
        elif correct == 3:
            print("Цвет главной площади России")
        elif correct == 4:
            print("Апельсин")
        else:
            print("Цвет логотипа Visual Studio")
