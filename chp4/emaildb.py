import pygame

pygame.init()
Width = 1000
height = 900
screen = pygame.display.set_mode([Width,height])
pygame.display.set_caption('Chess')

timer = pygame.time.Clock()
fps = 60

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook'
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook'
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

black_queen = pygame.image.load('queen_black.png')
black_queen = pygame.transform.scale(black_queen,(80,80))
black_queen_small = pygame.transform.scale(black_queen,(45,45))
black_king = pygame.image.load('king_black.png')
black_king = pygame.transform.scale(black_king,(80,80))
black_king_small = pygame.transform.scale(black_king,(45,45))
black_bishop = pygame.image.load('bishop_black.png')
black_bishop = pygame.transform.scale(black_bishop,(80,80))
black_bishop_small = pygame.transform.scale(black_bishop,(45,45))
black_knight = pygame.image.load('knight_black.png')
black_knight = pygame.transform.scale(black_knight,(80,80))
black_knight_small = pygame.transform.scale(black_knight,(45,45))
black_rook = pygame.image.load('rook_black.png')
black_rook = pygame.transform.scale(black_rook,(80,80))
black_rook_small = pygame.transform.scale(black_rook,(45,45))
black_pawn = pygame.image.load('pawn_black.png')
black_pawn = pygame.transform.scale(black_pawn,(65,65))
black_pawn_small = pygame.transform.scale(black_pawn,(45,45))

white_queen = pygame.image.load('queen.png')
white_queen = pygame.transform.scale(white_queen,(80,80))
white_queen_small = pygame.transform.scale(white_queen,(45,45))
white_king = pygame.image.load('king.png')
white_king = pygame.transform.scale(white_king,(80,80))
white_king_small = pygame.transform.scale(white_king,(45,45))
white_bishop = pygame.image.load('bishop.png')
white_bishop = pygame.transform.scale(white_bishop,(80,80))
white_bishop_small = pygame.transform.scale(white_bishop,(45,45))
white_knight = pygame.image.load('knight.png')
white_knight = pygame.transform.scale(white_knight,(80,80))
white_knight_small = pygame.transform.scale(white_knight,(45,45))
white_rook = pygame.image.load('rook.png')
white_rook = pygame.transform.scale(white_rook,(80,80))
white_rook_small = pygame.transform.scale(white_rook,(45,45))
white_pawn = pygame.image.load('pawn.png')
white_pawn = pygame.transform.scale(white_pawn,(65,65))
white_pawn_small = pygame.transform.scale(white_pawn,(45,45))

white_images = [white_pawn,white_rook,white_knight,white_bishop,white_king,white_queen]
white_small_images = [white_pawn_small,white_rook_small,white_knight_small,white_bishop_small,white_king_small,white_queen_small]

black_images = [black_pawn,black_rook,black_knight,black_bishop,black_king,black_queen]
black_small_images = [black_pawn_small,black_rook_small,black_knight_small,black_bishop_small,black_king_small,black_queen_small]

piece_list = ['pawn','rook','knight','bishop','king','queen']

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200),row * 100, 100,100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()