import sqlite3

import pygame
import os
from cards import Card
import random

class Deck:
    pass


class Game:
    pass


pygame.init()
pygame.display.set_caption('тут будет название')
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mixer.music.load('music1.mp3')
pygame.mixer.music.play(-1)


class Buttons():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, text, action=None, size=30):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse_pos[0] < x + self.width and y < mouse_pos[1] < y + self.height:
            pygame.draw.rect(screen, (204, 88, 48), (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                if action == quit:
                    pygame.quit()
                else:
                    action()

        else:
            pygame.draw.rect(screen, (234, 135, 92), (x, y, self.width, self.height))

        print_text(text=text, x=x + 10, y=y + 10, size=size)


def print_text(text, x, y, color=(242, 242, 242), font_type='Impact.ttf', size=30):
    font_type = pygame.font.Font(font_type, size)
    text_ = font_type.render(text, True, color)
    screen.blit(text_, (x, y))


def menu():
    back = pygame.image.load('временый фон.xcf')

    start = Buttons(250, 70)
    exit = Buttons(250, 70)

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
        screen.blit(back, (0, 0))
        start.draw(50, 400, 'Играть', name_input, 50)
        exit.draw(50, 500, 'Выход', quit, 50)  # не знаю почему возникает ошибка

        pygame.display.update()
        clock.tick(60)

input_name = ''

def name_input():
    show = True

    need_input = False
    global input_name

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
            if need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    need_input = False
                    start_game()
                elif event.key == pygame.K_BACKSPACE:
                    input_name = input_name[:-1]
                else:
                    if len(input_name) < 18:
                        input_name += event.unicode

        screen.fill((84, 83, 83))
        pygame.draw.rect(screen, (234, 135, 92),
                         (350, 320, 300, 53), 10)
        pygame.draw.rect(screen, (234, 135, 92),
                         (350, 250, 300, 53))
        print_text("Введите имя", 370, 250, color=(242, 242, 242), font_type='Impact.ttf', size=45)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            need_input = True

        print_text(input_name, 360, 325)

        pygame.display.update()
        clock.tick(60)

def zapis_name_base():
    con = sqlite3.connect("mydatabase_durak.db")
    cur = con.cursor()
    result = cur.execute(
        '''SELECT * FROM results WHERE name LIKE ?''', (input_name,)).fetchall()
    if not result:
        result = cur.execute("""INSERT INTO results(name, number_nikto, number_prongr, number_of_wins
                           ) VALUES(?,?,?,?)""", (input_name, 0, 0, 0)).fetchall()
    con.commit()
    con.close() # не забыть доделать базу данных



def start_game():
    # print(1)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
        screen.fill((84, 83, 83))
        print_text(f"Игрок {input_name}", 20, 20)
        pygame.display.update()
