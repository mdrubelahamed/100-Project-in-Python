from module import alphabet, numbers, symbols

def encode(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            final_index = (index + shift) % len(alphabet)
            cipher_text += alphabet[final_index]
        elif char in symbols:
            index = symbols.index(char)
            final_index = (index + shift) % len(symbols)
            cipher_text += symbols[final_index]
        elif char in numbers:
            index = numbers.index(char)
            final_index = (index + shift) % len(numbers)
            cipher_text += numbers[final_index]
        else:
            cipher_text += char

    print(f"Your Cipher Text: {cipher_text}")


def decode(secret_text, shift):
    original_text = ""
    for char in secret_text:
        if char in alphabet:
            original_index = (alphabet.index(char) - shift) % len(alphabet)
            original_text += alphabet[original_index]
        elif char in symbols:
            original_index = (symbols.index(char) - shift) % len(symbols)
            original_text += symbols[original_index]
        elif char in numbers:
            original_index = (numbers.index(char) - shift) % len(numbers)
            original_text += numbers[original_index]
        else:
            original_text += char

    print(f"Your Original Message: {original_text}")


end_cipher_game = False
while not end_cipher_game:
    action = input("e for encode, d for decode\n").lower()
    if action == "e":
        text = input("Which message do you want to encode?\n")
    else:
        text = input("Which message do you want to decode?\n")
    shift = int(input("Input your secret number?\n"))

    if action == "e":
        encode(text=text, shift=shift)
    elif action == "d":
        decode(secret_text=text, shift=shift)

    quit_option = input("If you want to quit, type 'q'. If you want to play again, type 'p'\n").lower()

    if quit_option == "q":
        end_cipher_game = True
