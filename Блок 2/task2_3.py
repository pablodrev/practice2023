digits = input("Введите число: ")

result = 0
for d in digits:
    result += int(d)**len(digits)

if result == int(digits):
    print(f"Число {digits} - число Армстронга.")
else:
    print(f"Число {digits} - не число Армстронга")
