__author__ = 'tspycher'

from gameboard import Gameboard
from snake import Snake, SnakeMoveDirection
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN


class Game(object):

    _gamespeed = 0.6
    _snake = None
    _gameboard = None
    _screen = None

    def __init__(self):
        # Create the screen object
        curses.initscr()
        self._screen = curses.newwin(20, 20, 0, 0) #curses.initscr()
        self._screen.keypad(1)
        self._screen.nodelay(1)
        self._screen.timeout(150)
        self._screen.border(1)


        curses.noecho()
        curses.cbreak()

        self._gameboard = Gameboard((20, 20), self._screen)
        self._snake = Snake(self._gameboard)

    def run(self):
        key = KEY_RIGHT
        try:
            while 1:
                event = self._screen.getch()
                key = key if event == -1 else event
                s = None

                if key == KEY_UP:
                    s = SnakeMoveDirection.up
                elif key == KEY_DOWN:
                    s = SnakeMoveDirection.down
                elif  key == KEY_LEFT:
                    s = SnakeMoveDirection.left
                elif key == KEY_RIGHT:
                    s = SnakeMoveDirection.right

                self._snake.move(s)
                self._gameboard.draw()
        finally:
            curses.echo()
            curses.nocbreak()
            curses.endwin()

if __name__ == "__main__":
    g = Game()
    g.run()