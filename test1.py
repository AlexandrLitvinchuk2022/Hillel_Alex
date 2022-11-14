alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypt = input("Enter login: ")
key = int(input("Enter a key from 1-25: "))
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    new_position = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[new_position]
    else:
        encrypted = encrypted + letter
print(encrypted)