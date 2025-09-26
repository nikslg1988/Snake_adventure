import pygame
import random

pygame.init()
pygame.font.init()

# Размер экрана
WIDTH = 640
HEIGHT = 480
# Количество обновлений в сек
FPS = 60
#Привязка к клеткам
CELL_SIZE = 10
# Базовые цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

start_x = WIDTH // 2
start_y = HEIGHT // 2

#Змейка Голова Тело и Хвост
snake = [
    (start_x + CELL_SIZE, start_y),
    (start_x, start_y),
    (start_x - CELL_SIZE, start_y)
]


# Начальное направление
direction = (0,-1)  # dx dy движение вверх

# Словарь для соответсвия нажатия клавиш и направлений (x,y) координаты в кортеже
movement_keys = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

font = pygame.font.SysFont(None, 24)

#Таймер для ступенчатого движения
last_move_time = pygame.time.get_ticks()
move_delay = 150 #Задержка движения в 150мс

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        
        # Обрабатываем НАЖАТИЕ клавиш
        if event.type == pygame.KEYDOWN:
            if event.key in movement_keys:
                # Устанавливаем направление при нажатой клавише
                direction = movement_keys[event.key]
    #Проверка пора ли двигаться
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time > move_delay:
        last_move_time = current_time
        
        # Движение змейки — ступенчато
        head_x, head_y = snake[0]  # текущая голова
        dx, dy = direction
        new_head = (head_x + dx * CELL_SIZE, head_y + dy * CELL_SIZE)  # следующая клетка
        snake.insert(0, new_head)  # добавляем новую голову
        snake.pop()  # удаляем хвост — если не съели еду, иначе не удаляем (см. дальше)
    
        #Проверка столкновения со стенами 
        head_x, head_y = snake[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            exit() #пока что выход
        
        #Проверка столкновения с телом змеи
        if (head_x, head_y) in snake[1:]:
            exit()  # пока что выход
            
        
    
    
                   
    screen.fill(WHITE)
    
    # Отрисовка прямоугольника
    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, RED, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
    
    # Отладочный текст
    dir_text = { (0, -1): "Вверх", (0, 1): "Вниз", (-1, 0): "Влево", (1, 0): "Вправо" }
    text = font.render(f"Направление: {dir_text.get(direction, 'Нет')}", True, RED)
    screen.blit(text, (10, 10))
    
    # Обновление экрана
    pygame.display.update()

    
   