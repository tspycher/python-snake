__author__ = 'tspycher'

import time
from gameboard import Gameboard
from snake import Snake, SnakeMoveDirection
import sys
from select import select


class Game(object):

    _gamespeed = 0.6
    _snake = None
    _gameboard = None

    def __init__(self):
        self._gameboard = Gameboard((20,20))
        self._snake = Snake(self._gameboard)

    def run(self):
        while 1:
            rlist, _, _ = select([sys.stdin], [], [], self._gamespeed)
            s = None

            if rlist:
                s = sys.stdin.readline()
                if "w" in s:
                    s = SnakeMoveDirection.up
                elif "s" in s:
                    s = SnakeMoveDirection.down
                elif "a" in s:
                    s = SnakeMoveDirection.left
                elif "d" in s:
                    s = SnakeMoveDirection.right
            self._snake.move(s)
            self._gameboard.draw()

if __name__ == "__main__":
    g = Game()
    g.run()