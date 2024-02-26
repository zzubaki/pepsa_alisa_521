import pygame
import sys
import math

pygame.init()

# Установка размеров окна
screen_width, screen_height = 800, 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("едрен батон")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Свойства шарика
ball_radius = 15
ball_color = WHITE
ball_pos = [screen_width // 10, screen_height // 15]  # Начальное положение шарика
ball_velocity = [4, 0]  # Начальная скорость шарика
gravity = 0.9  # Гравитация
elasticity = 0.9  # Коэффициент упругости
min_speed = 5  # Минимальная скорость по Y, при которой шарик останавливается
friction = 0.99  # Коэффициент трения для замедления шарика

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Перемещение шарика
    ball_velocity[1] += gravity  # Добавляем гравитацию
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Проверка на столкновение со стенами
    if ball_pos[0] + ball_radius > screen_width or ball_pos[0] - ball_radius < 0:
        ball_velocity[0] = -ball_velocity[0] * elasticity  # Изменение направления и скорости при упругом отскоке

    if ball_pos[1] + ball_radius > screen_height:
        ball_pos[1] = screen_height - ball_radius  # Предотвращаем проваливание шарика под нижнюю границу окна
        ball_velocity[1] = -ball_velocity[1] * elasticity  # Изменение направления и скорости при упругом отскоке
        ball_velocity[0] *= friction  # Применяем трение

    # Остановка шарика по вертикали, если скорость становится слишком маленькой
    if math.fabs(ball_velocity[1]) < min_speed and ball_pos[1] + ball_radius >= screen_height:
        ball_velocity[1] = 0

    # Заливка окна белым цветом
    window.fill(RED)

    # Рисуем шарик
    pygame.draw.circle(window, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Обновляем экран
    pygame.display.flip()

    # Задержка для плавного движения
    pygame.time.Clock().tick(60)