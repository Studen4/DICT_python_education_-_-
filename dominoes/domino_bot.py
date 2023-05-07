"""Module with logic of bot moves"""
import random


class Bot:
    """Class which work with bot and his moves"""

    def __init__(self, hand, domino):
        self.domino = domino
        self.hand = hand

    def make_move(self):
        """Function to check correct of bot turn"""
        scores = self.calculate_scores()
        sorted_tiles = sorted(self.hand, key=lambda raw_tile: scores[tuple(raw_tile)], reverse=True)

        for tile in sorted_tiles:
            if self.can_place_tile(tile):
                self.place_tile(tile)
                return

        if len(self.domino.stack) > 0:
            self.draw_from_stock()

    def draw_from_stock(self):
        """Bot draws a tile from the stock"""
        if len(self.domino.stack) > 0:
            tile = random.choice(self.domino.stack)
            self.hand.append(tile)
            self.domino.stack.remove(tile)

    def calculate_scores(self):
        """Calculate scores for each tile based on the numbers in the tile"""
        scores = {}
        snake_numbers = [number for tile in self.domino.snake for number in tile]
        for tile in self.hand:
            scores[tuple(tile)] = snake_numbers.count(tile[0]) + snake_numbers.count(tile[1])
        return scores

    def can_place_tile(self, tile):
        """Check if the tile can be placed on either side of the snake"""
        left_number = self.domino.snake[0][0]
        right_number = self.domino.snake[-1][1]
        return tile[0] == left_number or tile[1] == left_number \
            or tile[0] == right_number or tile[1] == right_number

    def place_tile(self, tile):
        """Place the tile on the snake"""
        left_number = self.domino.snake[0][0]
        right_number = self.domino.snake[-1][1]
        if tile[0] == left_number:
            self.domino.snake.insert(0, tile[::-1])
        elif tile[1] == left_number:
            self.domino.snake.insert(0, tile)
        elif tile[0] == right_number:
            self.domino.snake.append(tile)
        elif tile[1] == right_number:
            self.domino.snake.append(tile[::-1])
        self.hand.remove(tile)
