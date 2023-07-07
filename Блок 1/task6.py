text = input("Введите строку: ")
new_text = " ".join([word.capitalize() for word in text.split()])
print(new_text)
