from day8module import alphabet, logo, numbers, symbols

alphabet_length = len(alphabet)
numbers_length = len(numbers)
symbols_length = len(symbols)


print(logo)


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            final_index = letter_index + (shift_amount % alphabet_length)
            if final_index >= alphabet_length:
                final_index -= alphabet_length  # 26
                end_text += alphabet[final_index]
            else:
                end_text += alphabet[final_index]

        elif letter in numbers:
            letter_index = numbers.index(letter)
            final_index = letter_index + (shift_amount % numbers_length)
            if final_index >= numbers_length:
                final_index -= numbers_length  # 10
                end_text += numbers[final_index]
            else:
                end_text += numbers[final_index]

        elif letter in symbols:
            letter_index = symbols.index(letter)
            final_index = letter_index + (shift_amount % symbols_length)
            if final_index >= symbols_length:
                final_index -= symbols_length  # 30
                end_text += symbols[final_index]
            else:
                end_text += symbols[final_index]
        else:
            end_text += letter

    print(f"your {cipher_direction}d text is {end_text}")


end_of_loop = False
while not end_of_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    quit = input("Type 'yes' if you want to do it again or type 'no'.\n")
    if quit == "no":
        end_of_loop = True
