from module import alphabet,numbers,symbols


def encode(text,shift):
    global cipher_text
    cipher_text = ""
    for char in text:
        if char in alphabet:
                l_index = alphabet.index(char)
                final_index = l_index + shift

                if final_index >= len(alphabet):
                    final_index = final_index - len(alphabet)
                    cipher_text += alphabet[final_index]
                else:
                    cipher_text += alphabet[final_index]
        elif char in symbols:
                    s_index = symbols.index(char)
                    final_s_index = s_index + shift

                    if final_s_index >= len(symbols):
                        final_s_index = final_s_index - len(symbols)
                        cipher_text += symbols[final_s_index]
                    else:
                        cipher_text += symbols[final_s_index]

        elif char in numbers:
            n_index = numbers.index(char)
            final_n_index = n_index + shift
            
            if final_n_index >= len(numbers):
                 final_n_index = final_n_index - len(numbers)
                 cipher_text += numbers[final_n_index]
            else:
                 cipher_text += numbers[final_n_index]
        
        else:
             cipher_text += char

    print(f"cipher text {cipher_text}")


def decode(cipher_text,shift):
    original_text = ""
    for char in cipher_text:
        if char in alphabet:
            pass
               
               


action = input("e for encode, d for decode\n").lower()
text = input("What massage do you want to be secret?\n")
shift = int(input("Input your secret number?\n"))

if action == "e":
    encode(text=text, shift=shift)
elif action == "d":
    pass