EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

class Level:


    def guessing_chance(self,user_input):
        if user_input == "easy":
            return EASY_LEVEL_ATTEMPTS
        elif user_input == "hard":
            return HARD_LEVEL_ATTEMPTS
        else:
            return EASY_LEVEL_ATTEMPTS



    def level_choice(self):
        user_level = input("Choose your playing level? 'easy' or 'hard'-")
        self.guessing_chance(user_input=user_level)
    
