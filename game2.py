import pygame
import random

# Initialize the game
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Bird settings
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
BIRD_X = 50
BIRD_Y = 300

# Pipe settings
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(150, 450)
PIPE_GAP = 200
PIPE_VELOCITY = 5

# Gravity and jump
GRAVITY = 0.2
JUMP_STRENGTH = -8

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Bird class
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = BIRD_Y
        self.velocity = 0

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 450)
        self.passed = False

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, BLACK, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP))

    def update(self):
        self.x -= PIPE_VELOCITY

    def collide(self, bird):
        if bird.y < self.height or bird.y > self.height + PIPE_GAP:
            if bird.x + BIRD_WIDTH > self.x and bird.x < self.x + PIPE_WIDTH:
                return True
        return False

# Main game loop
def main():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + 200)]
    clock = pygame.time.Clock()
    score = 0

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()
        bird.draw()

        for pipe in pipes:
            pipe.update()
            pipe.draw()
            if pipe.collide(bird):
                running = False
            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                score += 1
                pipes.append(Pipe(SCREEN_WIDTH))

        pygame.display.update()
        clock.tick(30)

    print(f"Game Over! Your score: {score}")

if __name__ == "__main__":
    main()
    pygame.quit()
