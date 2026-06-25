import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day 35 - Space Dodge Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 60, 60)
BLUE = (60, 160, 255)
YELLOW = (255, 220, 60)

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 80, 50, 50)
player_speed = 7

meteors = []
meteor_speed = 5
score = 0
level = 1

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def create_meteor():
    size = random.randint(30, 60)
    x = random.randint(0, WIDTH - size)
    return pygame.Rect(x, -size, size, size)

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    if random.randint(1, 25) == 1:
        meteors.append(create_meteor())

    for meteor in meteors[:]:
        meteor.y += meteor_speed

        if meteor.top > HEIGHT:
            meteors.remove(meteor)
            score += 1

        if player.colliderect(meteor):
            screen.fill(BLACK)
            draw_text("GAME OVER", 220, 300, RED)
            draw_text(f"Final Score: {score}", 200, 350, YELLOW)
            pygame.display.update()
            pygame.time.delay(2500)
            pygame.quit()
            sys.exit()

    level = score // 10 + 1
    meteor_speed = 5 + level

    pygame.draw.rect(screen, BLUE, player)

    for meteor in meteors:
        pygame.draw.rect(screen, RED, meteor)

    draw_text(f"Score: {score}", 20, 20)
    draw_text(f"Level: {level}", 480, 20)

    pygame.display.update()
