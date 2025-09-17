import pygame
import random

pygame.init()
pygame.font.init()

# Размер экрана
WIDTH = 640
HEIGHT = 480
# Количество обновлений в сек
FPS = 60
# Базовые цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2

player_rect = pygame.Rect(x, y, 10, 10)
food_rect = pygame.Rect(x, y, 10, 10)
speed = 100

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


while True:
    # Обозначаем дельту времени 
    dt = clock.tick(FPS) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        
        # Обрабатываем НАЖАТИЕ клавиш
        if event.type == pygame.KEYDOWN:
            if event.key in movement_keys:
                # Устанавливаем направление при нажатой клавише
                direction = movement_keys[event.key]
        
    # Движение всегда в текущем направление
    dx, dy = direction
    player_rect.x += dx * speed * dt
    player_rect.y += dy * speed * dt
                
    # Ограничение по границам экрана
    player_rect.clamp_ip(screen.get_rect())
    
                   
    screen.fill(WHITE)
    
    # Отрисовка прямоугольника
    pygame.draw.rect(screen, RED, player_rect)
    #pygame.draw.rect(screen, GREEN, food_rect)
    
    # Отладочный текст
    dir_text = { (0, -1): "Вверх", (0, 1): "Вниз", (-1, 0): "Влево", (1, 0): "Вправо" }
    text = font.render(f"Направление: {dir_text.get(direction, '???')}", True, RED)
    screen.blit(text, (10, 10))
    
    # Обновление экрана
    pygame.display.update()

    
   