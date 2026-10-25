import pygame
import sys
import random

# 1. Инициализация и настройки окна
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # Размер одного игрового блока (в пикселях)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра 'Змейка' для Политеха")
clock = pygame.time.Clock()

# Цвета (RGB)
GREEN = (34, 139, 34)    # Змейка
RED = (220, 20, 60)      # Еда (яблоко)
BLACK = (20, 20, 20)     # Фон
WHITE = (255, 255, 255)   # Текст очков

# 2. Инициализация игровых элементов
# Стартовая позиция головы змейки (центр экрана)
snake_pos = [300, 200]
# Тело змейки (список из блоков-координат)
snake_body = [[300, 200], [280, 200], [260, 200]]

# Направление движения (изначально вправо)
direction = "RIGHT"
change_to = direction

# Появление первой еды (случайные координаты, кратные CELL_SIZE)
food_pos = [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]
food_spawn = True

score = 0

# Функция для вывода очков на экран
def show_score(score):
    font = pygame.font.SysFont("Arial", 20)
    score_surface = font.render(f"Очки: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

# 3. Главный игровой цикл
while True:
    # --- Блок обработки событий (клавиатура) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Считываем нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = "RIGHT"

    # Защита от самопересечения на 180 градусов (чтобы змейка не могла пойти назад в себя)
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # --- Движение змейки ---
    if direction == "UP":
        snake_pos[1] -= CELL_SIZE
    if direction == "DOWN":
        snake_pos[1] += CELL_SIZE
    if direction == "LEFT" and direction != "RIGHT":
        snake_pos[0] -= CELL_SIZE
    if direction == "RIGHT":
        snake_pos[0] += CELL_SIZE

    # Выращивание тела: добавляем новую голову в начало списка
    snake_body.insert(0, list(snake_pos))

    # Механика поедания еды
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False  # Флаг, что еду съели, нужно сгенерировать новую
    else:
        # Если еду не съели, удаляем хвост (змейка просто ползет вперед)
        snake_body.pop()

    # Генерация новой еды в случайном месте
    if not food_spawn:
        food_pos = [random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                    random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE]
        food_spawn = True

    # --- Отрисовка графики ---
    screen.fill(BLACK)  # Очищаем экран черным цветом

    # Рисуем тело змейки
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

    # Рисуем еду (яблоко)
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # --- Условия проигрыша (Game Over) ---
    # Пересечение границ экрана
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - CELL_SIZE:
        break
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - CELL_SIZE:
        break

    # Врезание в собственный хвост
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            sys.exit()

    show_score(score)
    pygame.display.update()  # Обновляем кадр на мониторе

    # Скорость игры (10 кадров в секунду — оптимально для змейки)
    clock.tick(10)

# Экран завершения игры при выходе из цикла
print(f"Игра окончена! Вы набрали очков: {score}")
pygame.quit()