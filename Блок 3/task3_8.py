alphabet = {letter:number+1 for number, letter in enumerate([chr(i) for i in range(ord("а"), ord("я")+1)])}
print(alphabet)
