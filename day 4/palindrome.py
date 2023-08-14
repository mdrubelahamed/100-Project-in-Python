# Take a word as input from the user.
# Check if the input word is a palindrome.
# Print "Palindrome" if it's a palindrome, otherwise print "Not Palindrome".

str1 = input("Which word do you think in your 🧠 ")
str2 = str1.lower()
reverse_str = str2[::-1]
if str2 == reverse_str:
    print(f"{str1} is a Palindrome.")
else:
    print(f"{str1} is not a Palindrome.")

# print("Palindrome") if str == reverse_str else print("Not Palidrome")