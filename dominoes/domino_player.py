"""Module with logic of player moves"""
import random


class Player:
    """Class which work with user and his moves"""
    def __init__(self, hand, domino):
        self.hand = hand
        self.domino = domino

    def make_move(self):
        """Function to check correct of player turn"""
        while True:
            turn = self.get_player_input()
            if self.is_valid_pick(turn):
                if turn == 0:
                    self.draw_from_stock()
                elif turn > 0:
                    self.place_tile(turn - 1)
                elif turn < 0:
                    self.place_reversed_tile(-turn - 1)
                break

    @staticmethod
    def get_player_input() -> int:
        """Check user input and change it to int"""
        turn = int(input())
        return turn

    def is_valid_pick(self, turn) -> bool:
        """Check correct of user input mainly based on user hand"""
        if turn > len(self.hand) or turn < -len(self.hand):
            return False
        return True

    def draw_from_stock(self):
        """Function to give player opportunity to pick tile from stock"""
        if len(self.domino.stack) > 0:
            tile = random.choice(self.domino.stack)
            self.hand.append(tile)
            self.domino.stack.remove(tile)

    def place_tile(self, index):
        """Function to check raw position of tile in board"""
        tile = self.hand[index]
        if self.domino.snake[-1][1] == tile[0]:
            self.domino.snake.append(tile)
        elif self.domino.snake[-1][1] == tile[1]:
            self.domino.snake.append(tile[::-1])
        elif self.domino.snake[0][0] == tile[1]:
            self.domino.snake = [tile] + self.domino.snake
        elif self.domino.snake[0][0] == tile[0]:
            self.domino.snake = [tile[::-1]] + self.domino.snake
        self.hand.remove(tile)

    def place_reversed_tile(self, index):
        """Function to check reversed position of tile in board"""
        tile = self.hand[index]
        if self.domino.snake[0][0] == tile[1]:
            self.domino.snake = [tile] + self.domino.snake
        elif self.domino.snake[0][0] == tile[0]:
            self.domino.snake = [tile[::-1]] + self.domino.snake
        elif self.domino.snake[-1][1] == tile[1]:
            self.domino.snake.append(tile)
        elif self.domino.snake[-1][1] == tile[0]:
            self.domino.snake.append(tile[::-1])
        self.hand.remove(tile)
