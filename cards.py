class Card(object):
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
