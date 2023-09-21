class Difficulty:
    def __init__(self, difficulty):
        self.difficulty = None

    def get_sleep_time(self):
        if self.difficulty == "easy":
            return 0.3
        elif self.difficulty == "medium":
            return 0.2
        elif self.difficulty == "hard":
            return 0.1
        else:
            # Default to medium difficulty if an invalid option is chosen
            return 0.2
