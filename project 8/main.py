# TEXT ENCRYPTION AND DECRYPTION
from day8module import alphabet, logo

print(logo)
alphabet_length = len(alphabet)


def encrypt(plain_text, shift_amount):
    global cipher_text
    cipher_text = ""
    for letter in plain_text:
        # if user give any input outside a-z for ex: @#$% etc
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            final_index = letter_index + shift_amount
            # when final_index is out of range we go back to the first letter
            if final_index >= alphabet_length:
                final_index -= 26
                new_letter = alphabet[final_index]
                cipher_text += new_letter
            else:
                new_letter = alphabet[final_index]
                cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"Encoded text is {cipher_text}")


# decryption
def decrypt(encoded_text, shift_amount):
    original_text = ""
    for letter in encoded_text:
        if letter in alphabet:
            final_index = alphabet.index(letter) - shift_amount
            letter = alphabet[final_index]
            original_text += letter
        else:
            original_text += letter
        # in list there are negative indexing so we don't need to use if else statement
    print(f"Your original text is {original_text}")


# use for loop to continue the game until user say 'no'
end_of_loop = False
while not end_of_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(encoded_text=text, shift_amount=shift)
    else:
        print("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    quit = input("Type 'yes' if you want to do it again or type 'no'.\n")

    if quit == "no":
        end_of_loop = True
