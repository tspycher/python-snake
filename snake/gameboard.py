__author__ = 'tspycher'

import sys
import random

class Gameboard(object):

    board = []
    boardSize = None
    food = None
    _screen = None

    def __init__(self, size, screen):
        self._screen = screen
        self.boardSize = size
        self.placeFood()

    def clearBoard(self):
        for x in xrange(self.boardSize[0]):
            self.board.append([])
            for y in xrange(self.boardSize[1]):
                self.board[x].append([])
                #if self.food[0] == x and self.food[1] == y:
                #    self.board[x][y] = "*"
                #else:
                self.board[x][y] = None

    def placeFood(self):
        self.food = (random.randint(0, self.boardSize[0]), random.randint(0, self.boardSize[1]))

    def draw(self):
        # Draw Food
        self._screen.addch(self.food[0], self.food[1], "*")

        # Draw Snake and Rest
        for x in xrange(self.boardSize[0]):
            for y in xrange(self.boardSize[1]):
                if self.board[x][y] is not None:
                    self._screen.addch(x, y, str(self.board[x][y]))

        self._screen.refresh()
