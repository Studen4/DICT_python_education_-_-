"""Main part of program with starter and checker who win"""
from variants_of_game import Modes
from writer_system import Results


class Analyzer:
    """Class to calculate winner of game"""
    def __init__(self):
        self.game_options = ['rock', 'gun', 'lightning', 'devil', 'dragon',
                             'water', 'air', 'paper', 'sponge', 'wolf', 'tree',
                             'human', 'snake', 'scissors']

    def calculate_winner(self, from_user: str, level: str):
        """Function to check answers of user and bot and gives win to someone"""
        from_bot = Modes(game_options, level).get_bot_choice()
        print(f"Bot choice: {from_bot}")
        if from_user == from_bot:
            return 'Tie'
        user_pick = self.game_options.index(from_user)
        bot_pick = self.game_options.index(from_bot)
        coefficient = len(self.game_options)
        win_condition = (coefficient // 2 + 1) % coefficient
        if (user_pick - bot_pick) % coefficient < win_condition:
            return 'User wins'
        else:
            return 'Bot wins'


if __name__ == '__main__':
    game = Analyzer()
    mode = input("Enter the mode of the game (Impossible/Full/Standard): ")
    while mode not in ('Impossible', 'Full', 'Standard'):
        mode = input("Invalid mode. Enter the mode of the game (Impossible/Full/Standard): ")
    bot_wins_always = False
    game_options = game.game_options
    match mode:
        case 'Impossible':
            bot_wins_always = True
        case 'Standard':
            game_options = Modes.get_game_options(game_options, "Standard")
        case 'Full':
            pass
    game_mode = Modes(game_options, bot_wins_always)
    print("Okay, let's start.")
    user_score = 0
    bot_score = 0
    while True:
        user_choice = input(f"Enter your choice ({', '.join(game_options)}) or type !exit to exit:")
        if user_choice == '!exit':
            results = Results()
            results.get_user_name()
            results.update_score(user_score)
            results.get_user_score()
            print(f"""
            Bot score: {bot_score}
            User score: {user_score}
            Bye!
            """)
            break
        if user_choice not in game_options:
            print("Invalid input.")
            continue
        bot_choice = game_mode.get_bot_choice()
        winner = game.calculate_winner(user_choice, mode)
        print(winner)
        match winner:
            case 'User wins':
                user_score += 1
            case 'Bot wins':
                bot_score += 1
