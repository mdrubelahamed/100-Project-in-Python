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

path1 = input('''You're at a cross road, where do you want to ge? Type "left" or "right": ''').lower()


if path1 == "left":
    path2 = input('''You come to a lake. There is an island in the middle of the lake,Type "wait" to wait for a boat or type "swim" to swim across: ''').lower()
    if path2 == "wait":
        path3 = input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, which colour do you choose? ''').lower()
        if path3 == "green":
            print("Congratulation!!! You find the treasue.")
        elif path3 == "red":
            print("you enter a ghost room, Game Over")
        elif path3 == "blue":
            print("you enter a beast room, Game Over")
        else : 
            print("Sorry, you have to choose between the red,green and blue room, Game Over")
    elif path2 == "swim":
        print("You've eaten by a blue wheal, Game Over")
    else: print("Next time choose between the 'wait' or 'swim'. ")
elif path1 == "right":
    print("You fell into a hole, Game Over")
else:print("Next time choose between left or right.")


