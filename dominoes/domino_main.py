"""Module to start the game"""
from domino_bot import Bot
from domino_player import Player
from domino_tiles_part import Domino
from domino_ui import Interface


class Game:
    """Main class of program with start part of it"""
    def __init__(self):
        self.domino = Domino()
        self.player = Player(self.domino.player_hand, self.domino)
        self.bot = Bot(self.domino.comp_hand, self.domino)
        self.interface = Interface(self.domino, self.player, self.bot)

    def user_checker(self) -> bool:
        """Function to check who turns"""
        match self.domino.player[self.domino.turn]:
            case 'Player':
                self.player.make_move()
                if len(self.player.hand) == 0:
                    self.interface.set_status('The game is over. You won!')
                    return True
            case 'Bot':
                input()
                self.bot.make_move()
                if len(self.bot.hand) == 0:
                    self.interface.set_status('The game is over. The computer won!')
                    return True
        if self.domino.check_draw():
            self.interface.set_status('The game is over. It\'s a draw!')
            return True
        self.domino.turn = abs(self.domino.turn - 1)
        self.interface.set_status(self.interface.message[self.domino.turn])
        return False

    def play(self):
        """Function to show game interface"""
        while True:
            self.interface.visual_display()
            if self.user_checker():
                break
        self.interface.visual_display()


if __name__ == "__main__":
    game = Game()
    game.play()
