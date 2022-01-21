import pygame
import sqlite3


pygame.init()
pygame.display.set_caption('тут будет название')
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def data_base():
    con = sqlite3.connect("mydatabase_durak.db")
    cur = con.cursor()
    names = cur.execute(
        '''SELECT name FROM results''').fetchall()
    nikto = cur.execute(
        '''SELECT number_nikto FROM results''').fetchall()
    prongr = cur.execute(
        '''SELECT number_prongr FROM results''').fetchall()
    wins = cur.execute(
        '''SELECT number_of_wins FROM results''').fetchall()
    if names:
        result = sorted(list(names), key=lambda x: x[-1], reverse=True)

    run = True
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from Deck import menu
                    menu()
        screen.fill((208, 172, 122))
        from Deck import print_text
        print_text('Имя             Победы          Поражения          Ничьи', 100, 10, color=(146, 86, 50), size=45)
        x = 100
        y = 35
        for i in names:
            y += 21
            print_text(str(i[0]), x, y, color=(146, 86, 50), size=20)
        x1 = 300
        y = 35
        for i in nikto:
            y += 21
            print_text(str(i[0]), x1, y, color=(146, 86, 50), size=20)
        x3 = 650
        y = 35
        for i in prongr:
            y += 21
            print_text(str(i[0]), x3, y, color=(146, 86, 50), size=20)
        x4 = 900
        y = 35
        for i in wins:
            y += 21
            print_text(str(i[0]), x4, y, color=(146, 86, 50), size=20)

        pygame.display.update()


   # def basa(self):
        #con = sqlite3.connect("mydatabase_durak.db")
        #cur = con.cursor()
        #result = cur.execute(
            #'''SELECT * FROM results WHERE name LIKE ?''', (name,)).fetchall()
        #nikto, fails, wins = result[0][1], result[0][2], result[0][3]
        #if not hand.cards:
            #wins += 1
        #elif not hand2.cards:
            #fails += 1
        #else:
            #nikto += 1
        #result = cur.execute("""UPDATE
        #results SET number_nikto = ?, number_prongr = ?, number_of_wins = ?
        #WHERE name = ?""", (nikto, fails, wins, name))
        #con.commit()
        # con.close()      запись результата игры


