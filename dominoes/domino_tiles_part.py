"""Module to work with domino tiles and check their valid in such cases"""
import random


class Domino:
    """Class to work with domino tiles"""
    def __init__(self):
        self.stack = []
        self.snake = []
        self.player = ('Player', 'Bot')
        self.turn = -1
        while self.turn == -1:
            self.domino_create()
            self.player_hand = self.new_hand()
            self.comp_hand = self.new_hand()
            self.status_check()

    def domino_create(self):
        """Function to create new stack of dominoes"""
        for i in range(0, 7):
            for j in range(i, 7):
                self.stack.append([i, j])

    def new_hand(self):
        """Function to give in hand some dominoes"""
        hand = []
        for _ in range(0, 7):
            hand.append(random.choice(self.stack))
            self.stack.remove(hand[-1])
        return hand

    def status_check(self):
        """Function to check doubles in start hand"""
        first_doubles = sorted([i for i in self.player_hand
                                if i[0] == i[1]], key=lambda x: x[0], reverse=True)
        second_doubles = sorted([i for i in self.comp_hand
                                 if i[0] == i[1]], key=lambda x: x[0] + x[1], reverse=True)

        match (len(first_doubles), len(second_doubles)):
            case (0, 0):
                pass
            case (_, 0):
                self.turn = 1
                self.snake.append(first_doubles[0])
                self.player_hand.remove(first_doubles[0])
            case (0, _):
                self.turn = 0
                self.snake.append(second_doubles[0])
                self.comp_hand.remove(second_doubles[0])
            case (_, _):
                match (sum(first_doubles[0]), sum(second_doubles[0])):
                    case _ if sum(first_doubles[0]) > sum(second_doubles[0]):
                        self.turn = 1
                        self.snake.append(first_doubles[0])
                        self.player_hand.remove(first_doubles[0])
                    case _ if sum(second_doubles[0]) > sum(first_doubles[0]):
                        self.turn = 0
                        self.snake.append(second_doubles[0])
                        self.comp_hand.remove(second_doubles[0])

    def check_draw(self):
        """Function to check if snake is full or not"""
        snake = ''
        for i in self.snake:
            snake += ''.join(list(map(str, i)))
        if snake.count(snake[0]) == 8 and snake.count(snake[-1]) == 8:
            return True
        return False
