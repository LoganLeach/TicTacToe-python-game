import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 255)
FPS = 60

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

# Initialize the board
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'

# Draw the grid
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)

# Draw X or O on the board
def draw_move(row, col, player):
    font = pygame.font.SysFont(None, 150)
    if player == 'X':
        text = font.render('X', True, CROSS_COLOR)
    else:
        text = font.render('O', True, CIRCLE_COLOR)
    text_rect = text.get_rect(center=(col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6))
    screen.blit(text, text_rect)

# Check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Check for a tie
def check_tie():
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

# Display game over screen
def game_over_screen(message):
    screen.fill(WHITE)

    font = pygame.font.SysFont(None, 80)
    text = font.render(message, True, LINE_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text, text_rect)

    font_small = pygame.font.SysFont(None, 40)
    restart_text = font_small.render("Press 'R' to restart or 'Q' to quit", True, LINE_COLOR)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // (HEIGHT // 3)
                clicked_col = mouseX // (WIDTH // 3)

                if board[clicked_row][clicked_col] == '':
                    board[clicked_row][clicked_col] = current_player
                    draw_move(clicked_row, clicked_col, current_player)

                    if check_winner():
                        if game_over_screen(f"Player {current_player} wins!"):
                            # Restart the game
                            board = [['', '', ''], ['', '', ''], ['', '', '']]
                            current_player = 'X'
                        else:
                            running = False
                    elif check_tie():
                        if game_over_screen("It's a tie!"):
                            # Restart the game
                            board = [['', '', ''], ['', '', ''], ['', '', '']]
                            current_player = 'X'
                        else:
                            running = False
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'

    # Draw the grid and current state of the board
    screen.fill(WHITE)
    draw_grid()
    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                draw_move(row, col, board[row][col])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
