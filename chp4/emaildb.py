import pygame

# initialize the module
pygame.init()

# setting up screen
screen = pygame.display.set_mode((1000, 900))
running = True

pygame.display.set_caption("Chess Game")

icon = pygame.image.load("iconboard.png")

pygame.display.set_icon(icon)

king_white = pygame.image.load("king.png")
bishop_white_left = pygame.image.load("bishop.png")
knight_white_left = pygame.image.load("knight.png")
rook_white_left = pygame.image.load("rook.png")
queen_white = pygame.image.load("queen.png")


def bishop_pieces(x, y):
    screen.blit(bishop_white_left, (x, y))


x_pos = 0
y_pos = 800

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x_pos += 0
    y_pos -= 80
    screen.fill((255, 255, 255))
    pygame.display.update()
    bishop_pieces(x_pos,y_pos)
    pygame.display.update()
    pygame.time.wait(500)
