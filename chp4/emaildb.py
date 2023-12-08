import pygame

# initialize the module
pygame.init()

# setting up screen
screen = pygame.display.set_mode((900, 900))
running = True

pygame.display.set_caption("Chess Game")

icon = pygame.image.load("iconboard.png")

pygame.display.set_icon(icon)

bishop = pygame.image.load("bishop.png")


def bishop_pieces(x, y):
    screen.blit(bishop, (x, y))


x_pos = 0
y_pos = 800

screen.fill((255, 255, 255))
pygame.display.update()

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x_pos += 0
    y_pos -= 80
    bishop_pieces(x_pos,y_pos)
    pygame.display.update()
    pygame.time.wait(500)
