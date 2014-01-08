__author__ = 'tspycher'

class SnakeMoveDirection(object):
    left = 0
    right = 1
    up = 2
    down = 3

class Snake(object):

    _gameboard = None
    _snake = []
    _previousDirection = SnakeMoveDirection.right

    def __init__(self, gameboard, snakeInitSize=10):
        self._gameboard = gameboard
        self._loadSnake(snakeInitSize)

    def _loadSnake(self, size):
        start = self._gameboard.boardSize[0] / 2
        for i in xrange(size):
            self._snake.append((start, 2+i))

    def move(self, direction):
        # Check if we got a new direction
        if direction is not None and direction != self._previousDirection:
            self._previousDirection = direction

        if self._previousDirection == SnakeMoveDirection.left:
            newElement = (self._snake[-1][0], self._snake[-1][1]-1)
        elif self._previousDirection == SnakeMoveDirection.right:
            newElement = (self._snake[-1][0], self._snake[-1][1]+1)
        elif self._previousDirection == SnakeMoveDirection.up:
            newElement = (self._snake[-1][0]-1, self._snake[-1][1])
        else:
            newElement = (self._snake[-1][0]+1, self._snake[-1][1])

        # Check if we reach the border
        if newElement[0] == 0 or newElement[1] == 0 or newElement[0] == self._gameboard.boardSize[0] or newElement[1] == self._gameboard.boardSize[1]:
            raise Exception("End of gameboard reached")

        # Check if snake bits himself
        for e in self._snake:
            if newElement == e:
                raise Exception("Snake bits itself")

        self._snake.append(newElement)
        # Check if snake is eating food
        if newElement == self._gameboard.food:
            self._gameboard.placeFood()
        else:
            self._snake.pop(0)
        self._gameboard.clearBoard()

        for e in self._snake:
            self._gameboard.board[e[0]][e[1]] = "#"