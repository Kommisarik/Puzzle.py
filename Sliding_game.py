import pygame
import random
import sys

"Функции для тестов"
#def check_win_for_test(massiv):
#   correct_indices = list(range(15)) + [-1]
#  return massiv == correct_indices


#def test_move_tile(clicked_index, empty_index):
#    if clicked_index > 15 or clicked_index < 0:
#        return
#   dx = (clicked_index % 4) - (empty_index % 4)
#   dy = (clicked_index // 4) - (empty_index // 4)
#    if abs(dx) + abs(dy) == 1:
#        return 1

# Размеры окна
WIDTH = 600
HEIGHT = 600
TILE_SIZE = WIDTH // 4

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Загрузим изображение
IMAGE_PATH = 'jinx.jpg'

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пятнашки")
clock = pygame.time.Clock()

# Загрузка и нарезка изображения
image = pygame.image.load(IMAGE_PATH)
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
tiles = []
for i in range(4):
    for j in range(4):
        rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        sub_image = image.subsurface(rect)
        tiles.append(sub_image)

# Удаление последней плитки
tiles.pop()

# Перемешанные индексы плиток
indices = list(range(15)) + [-1]
random.shuffle(indices)


# Функция для проверки победы
def check_win(indices):
    correct_indices = list(range(15)) + [-1]
    return indices == correct_indices

# Функция для перемещения плитки
def move_tile(clicked_index):
    if clicked_index > 15 or clicked_index < 0:
        return
    empty_index = indices.index(-1)
    dx = (clicked_index % 4) - (empty_index % 4)
    dy = (clicked_index // 4) - (empty_index // 4)
    if abs(dx) + abs(dy) == 1:
        indices[clicked_index], indices[empty_index] = indices[empty_index], indices[clicked_index]

# Основная логика игры
running = True
while running:
    clock.tick(30)

    screen.fill(BLACK)

    # Отображаем плитки
    for i in range(len(indices)):
        if indices[i] >= 0:
            screen.blit(tiles[indices[i]], (i % 4 * TILE_SIZE, i // 4 * TILE_SIZE))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_index = (pos[1] // TILE_SIZE) * 4 + (pos[0] // TILE_SIZE)
            move_tile(clicked_index)

    # Проверка победы
    if check_win(indices):
        font = pygame.font.Font(None, 24)
        text = font.render("Вы выиграли!", True, GREEN)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()