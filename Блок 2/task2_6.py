distance = int(input("Введите расстояние: "))
fuel_consumption = int(input("Введите расход топлива на 100 км: "))
fuel = int(input("Введите количество топлива в баке: "))

if fuel/fuel_consumption*100 > distance:
    print("Вы доедете!")
elif fuel/fuel_consumption*100 == distance:
    print("Вам едва ли хватит топлива. Лучше дозаправиться.")
else:
    print("К сожалению, вам не хватит топлива.")
