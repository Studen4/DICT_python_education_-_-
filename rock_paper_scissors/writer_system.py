"""Module for work with final part of program"""


class Results:
    """Class to work with results and write it to results.txt"""
    def __init__(self):
        self.force_creator()
        self.user_score = 0
        self.user_name = None
        self.scores = {}
        self.load_scores()

    def load_scores(self):
        """Function to read previous scores of named user"""
        with open('rating.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, score = line.strip().split()
                self.scores[name] = int(score)

    def get_user_name(self):
        """Function to ask user about his/her name"""
        self.user_name = input("Enter your name: ")
        print(f"Hello, {self.user_name}!")

    def get_user_score(self):
        """Function to get current user score"""
        if self.user_name in self.scores:
            self.user_score = self.scores[self.user_name]
        else:
            self.user_score = 0

    def update_score(self, new_score):
        """Function to overwrite previous score to new version"""
        self.user_score += new_score
        self.scores[self.user_name] = self.user_score
        with open('rating.txt', 'w', encoding='utf-8') as file:
            for name, score in self.scores.items():
                file.write(f"{name} {score}\n")

    def display_scores(self):
        """Function to show scoreboard to user"""
        print("\nScoreboard:")
        for name, score in self.scores.items():
            print(f"{name}: {score}")

    @staticmethod
    def force_creator():
        """Function to create score file if it not exists"""
        try:
            with open('rating.txt', 'x', encoding='utf-8'):
                pass
        except FileExistsError:
            pass
