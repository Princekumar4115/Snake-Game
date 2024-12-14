import pygame
import sys
from enum import Enum
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
#Next, let's define the Snake class that will represent the snake in the

#python
#Edit
#3ull Screen
#Copy code
class Snake:
    def __init__(self, block_size, bounds):
        self.length = 3
        self.body = [(20, 20), (20, 40), (20, 60)]
        self.direction = Direction.DOWN
        self.block_size = block_size
        self.bounds = bounds

    def respawn(self):
        self.length = 3
        self.body = [(20, 20), (20, 40), (20, 60)]
        self.direction = Direction.DOWN

    def move(self):
        head = self.body[0]
        dx, dy = 0, 0

        if self.direction == Direction.UP:
            dy -= self.block_size
        elif self.direction == Direction.DOWN:
            dy += self.block_size
        elif self.direction == Direction.LEFT:
            dx -= self.block_size
        elif self.direction == Direction.RIGHT:
            dx += self.block_size

        new_head = (head[0] + dx, head[1] + dy)

        if not self.check_collision(new_head):
            self.body.insert(0, new_head)
            self.body.pop()

    def check_collision(self, pos):
        x, y = pos
        return (x < 0 or x >= self.bounds[1] or y < 0 or y >= self.bounds[1])

    def steer(self, direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction
#Now, let's create the Food class that will represent the food in the game:

#python
#Edit
#Full Screen
#Copy code
class Food:
    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()

    def respawn(self):
        self.x = random.randint(0, self.bounds[0] // self.block_size) * self.block_size
        self.y = random.randint(0, self.bounds[1] // self.block_size) * self.block_size

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.block_size, self.block_size))
#Now, let's create the main game loop:

#python
#Edit
#Full Screen
#Copy code
def main():
    pygame.init()

    # Initialize the window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Initialize the clock
    clock = pygame.time.Clock()

    # Initialize the snake and food
    snake = Snake(BLOCK_SIZE, (WINDOW_WIDTH, WINDOW_HEIGHT))
    food = Food(BLOCK_SIZE, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.steer(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    snake.steer(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.steer(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.steer(Direction.RIGHT)

        # Move the snake
        snake.move()

        # Draw the food
        food.draw(window)

        # Draw the snake
        for pos in snake.body:
            pygame.draw.rect(window, (0, 0, 255), pygame.Rect(pos[0], pos[1], snake.block_size, snake.block_size))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(SPEED)

if __name__ == "__main__":
    main()
