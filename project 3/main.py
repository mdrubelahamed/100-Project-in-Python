#treasure island game
print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')

print("Welcome to Trease Island.")
print("Your mission is to find the treasure")

choice1 = input('''You're at a cross road, where do you want to ge? Type "left" or "right": ''').lower()


if choice1 == "left":
    choice2 = input('''You come to a lake. There is an island in the middle of the lake,Type "wait" to wait for a boat or type "swim" to swim across: ''').lower()
    if choice2 == "wait":
        choice3 = input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, which colour do you choose? ''').lower()
        if choice3 == "green":
            print("Congratulation!!! You find the treasue.")
        elif choice3 == "red":
            print("you enter a ghost room, Game Over!")
        elif choice3 == "blue":
            print("you enter a beast room, Game Over!")
        else : 
            print("Sorry, you have to choose between the red,green and blue room, Game Over!")
    else:
        print("Blue wheal was eaten you, Game Over!")
else:
    print("You fell into a hole, Game Over!")
