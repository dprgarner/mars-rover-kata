DIRECTION_DELTAS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}
DIRECTIONS = ['N', 'E', 'S', 'W']


class Rover():
    width = 5
    height = 5

    def __init__(self, position, direction, obstacles=[]):
        self.x, self.y = position
        self.direction = direction
        self.obstacles = obstacles

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def _delta(self):
        return DIRECTION_DELTAS[self.direction]

    def wrap(self):
        if self.x > self.width:
            self.x = 1
        if self.x == 0:
            self.x = self.width
        if self.y == 0:
            self.x = self.width + 1 - self.x
            self.y = 1
            self.direction = 'N' if self.direction == 'S' else 'S'
        if self.y == self.height + 1:
            self.x = self.width + 1 - self.x
            self.y = self.height
            self.direction = 'N' if self.direction == 'S' else 'S'

    def move_forward(self):
        self.x += self._delta[0]
        self.y += self._delta[1]
        self.wrap()

    def move_backward(self):
        self.x -= self._delta[0]
        self.y -= self._delta[1]
        self.wrap()

    def turn_left(self):
        idx = DIRECTIONS.index(self.direction)
        idx = (idx - 1) % 4
        self.direction = DIRECTIONS[idx]

    def turn_right(self):
        idx = DIRECTIONS.index(self.direction)
        idx = (idx + 1) % 4
        self.direction = DIRECTIONS[idx]

    def move(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'b':
                self.move_backward()

            if self.position in self.obstacles:
                obstacle = self.position
                self.move_backward() if command == 'f' else self.move_forward()
                return obstacle
