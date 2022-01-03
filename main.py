from pygame import *
import pygame
import sys

pygame.init()
pygame.display.set_caption('тут будет название')
size = width, height = 1500, 800
screen = pygame.display.set_mode(size)


class Menu:
    def __init__(self):
        self.options = []  # для отрисовки
        self.callbacks = []  # функции, которые вызываются при активации одного из пункта меню
        self.current_option_index = 0  # номер выбранного пункта

    def append_option(self, option, callback):
        font = pygame.font.Font(None, 50)
        self.options.append(font.render(option, True, (255, 255, 255)))
        self.callbacks.append(callback)

    def switch_option(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.options) - 1))

    def choose_option(self, ):
        self.callbacks[self.current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self.options):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option_index:
                draw.rect(surf, (199, 121, 121), option_rect)
            surf.blit(option, option_rect)


menu = Menu()  # экземпляры классе меню
menu.append_option('Играть', None)  # пока ничего не делает
menu.append_option('Выход', quit)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:  # ыбрать опцию можно с помощью стрелок
            if event.key == K_UP:
                menu.switch_option(-1)
            elif event.key == K_DOWN:
                menu.switch_option(1)
            elif event.key == K_SPACE:
                menu.choose_option()
    screen.fill((0, 0, 0))

    menu.draw(screen, 100, 100, 75)
    pygame.display.flip()
pygame.quit()