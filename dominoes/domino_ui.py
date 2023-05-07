"""Module to show user interface and other visual methods"""
from domino_bot import Bot
from domino_player import Player
from domino_tiles_part import Domino


class Interface:
    """Class to work with messages and status of program stages"""
    message = ('It\'s your turn to make a move. Enter your command:\n',
               'Computer is about to make a move. Press Enter to continue...\n')

    def __init__(self, domino: Domino, player: Player, bot: Bot):
        self.domino = domino
        self.bot = bot
        self.player = player
        self.status = self.message[self.domino.turn]

    def set_status(self, status: str):
        """Deploy status in console"""
        self.status = status

    def visual_display(self):
        """Visual part of program to inform user"""
        print(f'''
            Stock size: {len(self.domino.stack)}
            Computer pieces: {len(self.bot.hand)}
            Snake: {self.domino.snake if len(self.domino.snake) < 7 else f'{self.domino.snake[:3]}'
                                                                         f'...{self.domino.snake[-3:]}'}
            Your pieces: 
            ''')
        for index, piece in enumerate(self.player.hand):
            print(f'{index + 1}:', piece)
        print(f"\nStatus: {self.status}")
