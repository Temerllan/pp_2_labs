
import pygame
import time

pygame.init()

screen_length = 1000
screen_width = 800

screen = pygame.display.set_mode((screen_length, screen_width))
pygame.display.set_caption("Mickey Clock")

icon = pygame.image.load('images/mickeyclock1.png')
pygame.display.set_icon(icon)

clock_img = pygame.image.load('images/mickeyclock1.png').convert_alpha()
second_arrow = pygame.image.load('images/hand1.png').convert_alpha()
minute_arrow = pygame.image.load('images/hand2.png').convert_alpha()

x = (screen_length - clock_img.get_width()) // 2
y = (screen_width - clock_img.get_height()) // 2

clock_center = (x + clock_img.get_width() // 2, y + clock_img.get_height() // 2)

running = True
while running:
    screen.fill(('white'))
    screen.blit(clock_img, (x, y))

    seconds = time.localtime().tm_sec
    minutes = time.localtime().tm_min

    angle1 = -seconds * 6
    angle2 = -minutes * 6

    rotated_second_arrow = pygame.transform.rotate(second_arrow, angle1)
    rotated_minute_arrow = pygame.transform.rotate(minute_arrow, angle2)

    second_rect = rotated_second_arrow.get_rect(center=clock_center)
    minute_rect = rotated_minute_arrow.get_rect(center=clock_center)

    screen.blit(rotated_minute_arrow, minute_rect.topleft)
    screen.blit(rotated_second_arrow, second_rect.topleft)

    pygame.display.flip()
    pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

