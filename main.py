import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Puzzle Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Puzzle piece dimensions
PIECE_SIZE = 80
GRID_WIDTH = 4
GRID_HEIGHT = 5

# Puzzle grid
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Load puzzle piece images
piece_images = []
for i in range(1, 21):
    image = pygame.image.load(f"piece{i}.png")  # Replace with your own puzzle piece images
    image = pygame.transform.scale(image, (PIECE_SIZE, PIECE_SIZE))
    piece_images.append(image)

# Randomly assign puzzle pieces to the grid
pieces = list(range(1, 21))
random.shuffle(pieces)
for i in range(GRID_HEIGHT):
    for j in range(GRID_WIDTH):
        grid[i][j] = pieces.pop()

# Store the clicked piece's position
selected_piece = None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                col = pos[0] // PIECE_SIZE
                row = pos[1] // PIECE_SIZE
                if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
                    selected_piece = (row, col)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if selected_piece:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // PIECE_SIZE
                    row = pos[1] // PIECE_SIZE
                    if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
                        # Swap the puzzle pieces
                        grid[row][col], grid[selected_piece[0]][selected_piece[1]] = \
                            grid[selected_piece[0]][selected_piece[1]], grid[row][col]
                    selected_piece = None

    # Clear the screen
    screen.fill(WHITE)

    # Draw the puzzle grid
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] != 0:
                piece = grid[i][j]
                screen.blit(piece_images[piece - 1], (j * PIECE_SIZE, i * PIECE_SIZE))

    # Draw the grid lines
    for i in range(GRID_HEIGHT + 1):
        pygame.draw.line(screen, GRAY, (0, i * PIECE_SIZE), (GRID_WIDTH * PIECE_SIZE, i * PIECE_SIZE))
    for j in range(GRID_WIDTH + 1):
        pygame.draw.line(screen, GRAY, (j * PIECE_SIZE, 0), (j * PIECE_SIZE, GRID_HEIGHT * PIECE_SIZE))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
