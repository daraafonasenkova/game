import os
import sys
import pygame


class Card:
    RANKS = ['6', '7', '8', '9', '10', '11', '12', '13', '14']
    SUITS = ['bubi', 'chrv', 'piki', 'krst']  # масти

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        rep = self.suit + self.rank
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


def load_image(name, colorkey=None):
    fullname = os.path.join('cards', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
