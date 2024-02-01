'''
bina language
vowel -> g
'''
def translate(pharse):
    result = ""
    for letter in pharse:
        if letter in 'aeiouAEIOU':    # if letter.lower() in 'aeiou'
            if letter.isupper():
                result = result + 'G'
            else :
                result = result + 'g'
        else: 
            result = result+letter
    return result

print(translate(input("enter a pharse: ")))