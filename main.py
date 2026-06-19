import pygame
import sys

pygame.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Finding The Items")

clock = pygame.time.Clock()

WALL = (95, 70, 50)
FLOOR = (70, 45, 30)

WINDOW_FRAME = (60, 40, 20)
WINDOW_GLASS = (80, 120, 170)

BOOKSHELF = (90, 60, 30)
DESK = (100, 65, 40)

SOFA = (60, 80, 50)

DOOR = (80, 50, 25)

PAINTING_FRAME = (50, 30, 15)
PAINTING = (140, 140, 120)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WALL)

    pygame.draw.rect(screen, FLOOR, (0, 500, WIDTH, 300))

    pygame.draw.rect(screen, WINDOW_FRAME, (450, 70, 300, 180))
    pygame.draw.rect(screen, WINDOW_GLASS, (465, 85, 270, 150))

    pygame.draw.line(screen, WINDOW_FRAME, (600, 85), (600, 235), 6)
    pygame.draw.line(screen, WINDOW_FRAME, (465, 160), (735, 160), 6)

    pygame.draw.rect(screen, BOOKSHELF, (80, 180, 180, 320))

    for y in [250, 320, 390, 460]:
        pygame.draw.line(screen, (50, 30, 15), (80, y), (260, y), 4)

    pygame.draw.rect(screen, PAINTING_FRAME, (900, 180, 180, 130))
    pygame.draw.rect(screen, PAINTING, (915, 195, 150, 100))

    pygame.draw.rect(screen, DESK, (450, 400, 300, 120))
    pygame.draw.rect(screen, DESK, (470, 520, 20, 80))
    pygame.draw.rect(screen, DESK, (710, 520, 20, 80))

    pygame.draw.rect(screen, SOFA, (120, 550, 260, 120))
    pygame.draw.rect(screen, SOFA, (100, 520, 40, 120))
    pygame.draw.rect(screen, SOFA, (360, 520, 40, 120))

    pygame.draw.rect(screen, DOOR, (950, 350, 140, 250))

    pygame.draw.circle(screen, (220, 180, 40), (1060, 480), 8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
