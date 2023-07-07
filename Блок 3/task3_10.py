s = input("Введите строку: ")
d = {letter: s.count(letter) for letter in s if letter != " "}
print(d)
