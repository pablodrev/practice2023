text = input()
vowels = "аеёиоуыэюя"
letters = {letter: (letter in vowels) for letter in text}
print(letters)
