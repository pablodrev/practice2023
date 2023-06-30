import random

round_count = 1
wins = 0
loses = 0
while True:
    print("\nРаунд ", round_count)
    correct = random.randint(0, 1)
    guess = int(input("Орел или решка? (0 - Орел, 1 - Решка): "))
    if guess != 0 and guess != 1:
        print("Введено неверное число. Игра окончена.")
        break
    if guess == correct:
        print("Вы угадали.")
        wins += 1
    else:
        print("Вы не угадали.")
        loses += 1
    if loses == 3:
        print("Вы проиграли 3 раза подряд. Игра окончена.")
        break
    print(f"Счет: Победы: {wins}, Проиграши: {loses}")
    round_count += 1
