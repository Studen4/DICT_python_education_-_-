"""Module to work with modes of game"""
import random


class Modes:
    """Class which receive list of game and his level and pick the game mod"""
    def __init__(self, game_options, level="Standard"):
        self.game_options = self.get_game_options(game_options, level)
        self.bot_options = ['rock', 'paper', 'scissors', 'devil', 'dragon',
                            'water', 'air', 'gun', 'sponge', 'wolf', 'tree',
                            'human', 'snake', 'lightning']
        self.level = level

    @staticmethod
    def get_game_options(game_options, level):
        """Function to change 'bot pool of variations' to standard if user input is similar"""
        simple_game = ["rock", "paper", "scissors"]
        match level:
            case "Full":
                return game_options
            case "Standard":
                return simple_game

    def get_bot_choice(self):
        """Function to realise always win of bot situation, or simple pick variant with random"""
        match self.level:
            case 'impossible':
                bot_choice = self.bot_options[random.randint(0, len(self.game_options) - 1)]
                return self.get_winning_choice(bot_choice)
            case 'Full':
                return random.choice(self.bot_options)
            case 'Standard':
                return random.choice(self.bot_options[:3])

    def get_winning_choice(self, choice):
        """Function which helps bot always winning if program need it"""
        winning_choice_index = (self.game_options.index(choice) + 1) % len(self.game_options)
        return self.bot_options[winning_choice_index]
