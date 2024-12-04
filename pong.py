# pong game in pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_vel = random.choice([-4, 4])
        self.y_vel = random.choice([-4, 4])

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        # Bounce off top and bottom
        if self.y - BALL_RADIUS <= 0 or self.y + BALL_RADIUS >= HEIGHT:
            self.y_vel *= -1

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (self.x, self.y), BALL_RADIUS)

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5

    def move(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

    def draw(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def ai_move(self, ball):
        # Simple AI to follow the ball
        if self.y + PADDLE_HEIGHT // 2 < ball.y:
            self.move(up=False)
        elif self.y + PADDLE_HEIGHT // 2 > ball.y:
            self.move(up=True)

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()

    player_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    computer_paddle = Paddle(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    while run:
        clock.tick(60)
        win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_paddle.y - player_paddle.vel >= 0:
            player_paddle.move(up=True)
        if keys[pygame.K_s] and player_paddle.y + player_paddle.vel + PADDLE_HEIGHT <= HEIGHT:
            player_paddle.move(up=False)

        ball.move()
        computer_paddle.ai_move(ball)

        # Check for collision with paddles
        if ball.x - BALL_RADIUS <= player_paddle.x + PADDLE_WIDTH and player_paddle.y < ball.y < player_paddle.y + PADDLE_HEIGHT:
            ball.x_vel *= -1
        if ball.x + BALL_RADIUS >= computer_paddle.x and computer_paddle.y < ball.y < computer_paddle.y + PADDLE_HEIGHT:
            ball.x_vel *= -1

        player_paddle.draw(win)
        computer_paddle.draw(win)
        ball.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    
    
