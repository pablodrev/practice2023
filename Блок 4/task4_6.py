alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_rot13 = "nopqrstuvwxyzabcdefghijklm"
d = {a: b for a, b in zip(alphabet, alphabet_rot13)}
print(d)

text = input("Enter some text to encode: ")

new_text = ""
for letter in text:
    new_text += d[letter]

print(new_text)
