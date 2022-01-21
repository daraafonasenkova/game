#Даша по поводу таблицы смотри строки 546-620
#Артём посмотри пожалуйста 3ий столбик(622 - 735)
#План-капкан:просто перепишем функции на пайгем и потом слепим всё в одно в таком же порядке какой и был
#Можно оставить без изменений:
import pygame
import random


SCREEN_SIZE = WIDTH, HEIGHT = 1200, 900
BACKGROUND = 18, 47, 170
name = ''


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player_hod = False
        self.perviy_user = False
        self.kozir = str(hand3.cards[0]).split('\t')[0]
        self.initUI()



 def proverka_pravilno_card(self, i):#должна совпадать либо масть(и бьем старшей картой) либо козырем можно не козырь
        if i[:4] == self.stol_cards[-1][:4] and int(i[4:]) > int(self.stol_cards[-1][4:]):
            return True
        elif i[:4] == self.kozir[:4] == self.stol_cards[-1][:4] \
                and int(i[4:]) > int(self.stol_cards[-1][4:]):#если козыри то опять бьем старшей картой
            return True
        elif i[:4] == self.kozir[:4] != self.stol_cards[-1][:4]:
            return True
        else:
            return False

        def hod_II(self):
            if (not hand2.cards or not hand.cards) and not deck.cards:  # если на руках и в колоде нет карт
                self.end_game()
            variants = []
            variants_bez_kozir = []
            self.variants2 = self.btns_names2[:]
            if self.perviy_user:
                labels = self.labels1[:]
                col = self.col1
            else:
                labels = self.labels[:]
                col = self.col
            if self.player_hod:
                for _ in range(len(self.btns_names2)):
                    if self.proverka_pravilno_card(self.btns_names2[_]):
                        if self.btns_names2[_][:4] != str(self.kozir)[:4]:
                            variants_bez_kozir.append(
                                self.btns_names2[_])  # сначала отбиваемся подходящими не козырными
                        variants.append(self.btns_names2[_])
                        if variants_bez_kozir:
                            variants = variants_bez_kozir[:]
                for _ in range(len(variants) - 1):
                    for j in range(len(variants) - 1 - _):
                        if int(variants[j][4:]) > int(variants[j + 1][4:]):
                            variants[j], variants[j + 1] = variants[j + 1], variants[j]
                if not variants:
                    self.vzal(hand2)
                    self.label6.setText('Компьютер взял')
                else:
                    self.fname1 = f'cards\\{variants[0]}.gif'
                    self.pixmap = QPixmap(self.fname1)
                    labels[self.col].setPixmap(self.pixmap.scaled(112, 171))
                    self.col += 1
                    rrr = self.btns_names2.index(variants[0])
                    hand2.give(hand2.cards[rrr], hand4)
                    self.btns1[rrr].hide()
                    self.stol_cards.append(variants[0])
                    del self.btns1[rrr]
                    del self.btns_names2[rrr]
            else:  # если ход компа
                if self.podkidivat_var:
                    self.variants2 = self.podkidivat_var
                self.variants2 = list(set(self.variants2))
                for _ in range(len(self.variants2) - 1):  # сортируем, чтобы ходить с наименьшей
                    for j in range(len(self.variants2) - 1 - _):
                        if int(self.variants2[j][4:]) > int(self.variants2[j + 1][4:]):
                            self.variants2[j], self.variants2[j + 1] = self.variants2[j + 1], self.variants2[j]
                for _ in range(len(self.variants2)):
                    self.fname1 = f'cards\\{self.variants2[_]}.gif'
                    self.pixmap = QPixmap(self.fname1)
                    labels[self.col].setPixmap(self.pixmap.scaled(112, 171))
                    rrr = self.btns_names2.index(self.variants2[_])
                    hand2.give(hand2.cards[rrr], hand4)
                    self.btns1[rrr].hide()
                    del self.btns1[rrr]
                    del self.btns_names2[rrr]
                    self.stol_cards.append(self.variants2[_])
                    del self.variants2[_]
                    break



class Hand(object):#набор карт на руках у одного игрока
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = '<пусто>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


    def can_podkidivat(self, ruka):
        if self.stol_cards:   #если не первый ход, то на столе есть карты, из них и выбираем
            self.podkidivat_var.clear()
            for _ in range(len(self.stol_cards)):
                for j in range(len(ruka)):
                    if int(self.stol_cards[_][4:]) == int(ruka[j][4:]):#сравниваем карты в руке подкидывающего и на столе
                        self.podkidivat_var.append(ruka[j])
            if self.podkidivat_var:
                return True
            else:
                return False
        else:
            return True

#Это нужно переделать из pqt на pygame:
class Hand(object):  # набор карт на руках у одного игрока
    def initUI(self):
        self.setGeometry(100, 100, 1200, 900)
        self.setWindowTitle('Дурак')
        self.col = 0
        self.col1 = 0
        self.btns_names = []
        self.btns_names2 = []
        self.podkidivat_var = []

        self.btn_bita = QPushButton(self)#нарисуем прямоугольник как картинку и при нажатии на координату происходит событие
        # почему я сам не написал?.. а потому что слишком много времени потратил на неработающий код и устал(((
        self.btn_bita.setGeometry(780, 750, 100, 30)
        self.btn_bita.setText('Бита')
        self.btn_bita.clicked.connect(self.bita)

        self.btn_vzal = QPushButton(self)#нарисуем прямоугольник как картинку и при нажатии на координату происходит событие
        self.btn_vzal.setGeometry(970, 750, 100, 30)
        self.btn_vzal.setText('Взял')
        self.btn_vzal.clicked.connect(lambda: self.vzal(hand))

        self.label7 = QLabel(self)
        self.label7.setGeometry(850, 500, 200, 120)
        xxx = str(self.kozir).split('\t')[0]
        self.fname1 = f'cards\\{xxx}.gif'
        self.pixmap = QPixmap(self.fname1)
        self.label7.setObjectName(xxx)
        t = QTransform().rotate(+90)
        self.pixmap = QPixmap(self.pixmap.transformed(t))
        self.label7.setPixmap(self.pixmap.scaled(171, 112))

        self.label8 = QLabel(self)
        self.label8.setGeometry(920, 460, 120, 200)
        self.fname1 = f'cards\\37.gif'
        self.pixmap = QPixmap(self.fname1)
        self.label8.setPixmap(self.pixmap.scaled(112, 171))

        self.stol()

        def stol(self):
            if hand3.cards:  # возвращаем козырь в колоду
                hand3.give(hand3.cards[0], deck)
            self.btns = []
            self.na_rukah()  # показывает карты на руках
            self.stol_cards = []
            self.variants2 = []
            self.podkidivat_var = []
            self.labels = [None for i in range(6)]  # создаем места, куда кладем карты
            self.labels1 = [None for i in range(6)]
            for col in range(6):
                self.label = QLabel(self)
                self.label.setGeometry(80 + col * 180, 230, 120, 200)
                self.labels[col] = self.label
                self.labels[col].clear()
                self.labels[col].show()

                self.label = QLabel(self)
                self.label.setGeometry(130 + col * 180, 230, 120, 200)
                self.labels1[col] = self.label
                self.labels[col].clear()
                self.labels1[col].show()

            if len(deck.cards) > 0:  # убираем изображение колоды, когда она кончилась
                self.label8.show()
            else:
                self.label8.hide()

            self.label6 = QLabel(self)
            self.label6.setGeometry(10, 200, 190, 30)
            self.label6.setText(name)
            self.label6.show()
            self.label7.show()
            self.btn_bita.show()
            self.btn_vzal.show()

            if len(deck.cards) == 24:  # если первый ход, то выясняем кто ходит первый
                self.perviy()
            if not self.player_hod:
                if self.can_podkidivat(self.btns_names2):
                    self.hod_II()
            if not hand.cards or not hand2.cards:
                self.end_game()

        def end_game(self):
            self.btn_bita.hide()
            self.btn_vzal.hide()
            self.basa()  # записываем в базу результат
            self.open_second_form()  # конец игры, можно посмотреть результаты игр

        def basa(self):
            con = sqlite3.connect("mydatabase_durak.db")
            cur = con.cursor()
            result = cur.execute(
                '''SELECT * FROM results WHERE name LIKE ?''', (name,)).fetchall()
            nikto, fails, wins = result[0][1], result[0][2], result[0][3]
            if not hand.cards:
                wins += 1
            elif not hand2.cards:
                fails += 1
            else:
                nikto += 1
            result = cur.execute("""UPDATE
            results SET number_nikto = ?, number_prongr = ?, number_of_wins = ? 
            WHERE name = ?""", (nikto, fails, wins, name))
            con.commit()
            con.close()

        def open_second_form(self):
            self.second_form = SecondForm(self, "Конец игры")
            self.second_form.show()

        def open_first_form(self):
            self.first_form = FirstForm(self, "Как Вас зовут?")
            self.first_form.show()

        def na_rukah(self):
            self.btns = [None for i in range(
                len(hand.cards))]  # список кнопок карт игрока(hand.cards) и лабелек карт компа(hand2.cards)
            self.btns1 = [None for i in range(len(hand2.cards))]
            self.btns_names = []
            self.btns_names2 = []
            for col in range(len(self.btns)):
                self.btn = QPushButton(self)
                self.btn.setGeometry(180 + col * 30, 650, 112, 171)
                self.btns[col] = self.btn
                xxx = str(hand).split('\t')
                print('xxx', xxx)
                xxx = xxx[:-1]
                self.btns[col].setObjectName(xxx[col])  # имя кнопки как элемент hand
                self.btns[col].setIcon(QIcon(f'cards\\{xxx[col]}.gif'))  # картинка кнопки
                self.btns[col].setIconSize(QtCore.QSize(112, 171))
                self.btns_names.append(self.btns[col].objectName())
                self.btns[col].show()
                self.btns[col].clicked.connect(self.hodim)
            for col in range(len(self.btns1)):
                self.label = QLabel(self)
                self.label.setGeometry(180 + col * 30, 10, 120, 200)
                self.btns1[col] = self.label
                xxx = str(hand2).split('\t')
                xxx = xxx[:-1]
                self.btns1[col].setObjectName(xxx[col])
                self.fname1 = f'cards\\37.gif'  # в строке ниже можно видеть карты компа
                # self.fname1 = f'cards\\{xxx[col]}.gif'
                self.pixmap = QPixmap(self.fname1)
                self.btns1[col].setPixmap(self.pixmap.scaled(112, 171))
                self.btns1[col].show()
                self.btns_names2.append(self.btns1[col].objectName())

        def hodim(self):
            self.xxx = self.sender().objectName()
            if self.player_hod:
                if self.can_podkidivat(self.btns_names):
                    if self.podkidivat_var:  # список с возможными вариантами карт для подкидывани
                        if self.xxx in self.podkidivat_var:
                            self.card_on_stol()  # выкладываем карту на стол
                            self.hod_II()  # ход компа
                    else:
                        self.card_on_stol()
                        self.hod_II()
            else:
                if self.proverka_pravilno_card(self.xxx):  # проверка можно ли такой картой крыть
                    self.card_on_stol()
                    self.col += 1  # счетчик лабелек для отображения карт(дал и покрыл)
                    self.stol_cards.append(self.xxx)  # список карт на столе для проверки можно ли подкидвать
                    if self.can_podkidivat(self.btns_names2):
                        self.hod_II()
                    else:
                        self.bita()

        def can_podkidivat(self, ruka):
            if self.stol_cards:  # если не первый ход, то на столе есть карты, из них и выбираем
                self.podkidivat_var.clear()
                for _ in range(len(self.stol_cards)):
                    for j in range(len(ruka)):
                        if int(self.stol_cards[_][4:]) == int(
                                ruka[j][4:]):  # сравниваем карты в руке подкидывающего и на столе
                            self.podkidivat_var.append(ruka[j])
                if self.podkidivat_var:
                    return True
                else:
                    return False
            else:
                return True

        def card_on_stol(self):
            if self.perviy_user:  # определяем на какой уровень будем выкладывать карты: на первый - когда подкидываем
                labels = self.labels[:]  # или на второй если отбиваемся
            else:
                labels = self.labels1[:]
                col = self.col1
            self.xxx = self.sender().objectName()
            self.fname1 = f'cards\\{self.xxx}.gif'
            self.pixmap = QPixmap(self.fname1)
            labels[self.col].setPixmap(self.pixmap.scaled(112, 171))
            rrr = self.btns_names.index(self.xxx)
            hand.give(hand.cards[rrr], hand4)
            for xxx in self.btns:
                xxx.hide()
            for xxx in self.btns1:
                xxx.hide()
            del self.btns[rrr]
            del self.btns_names[rrr]
            self.stol_cards.append(self.xxx)
            self.na_rukah()

        def bita(self):
            self.stol_restart()  # прячем все со стола и по новой показываем
            self.perviy_user = not self.perviy_user
            self.player_hod = not self.player_hod
            self.initUI()

        def berem_card_is_kolodi(self):
            self.stol_cards.clear()
            if len(hand2.cards) < 6:
                dobavit = 6 - len(hand2.cards)
                hands_proba = hands[:]
                hands_proba = hands_proba[1:]
                deck.deal(hands_proba, per_hand=dobavit)
            if len(hand.cards) < 6:
                dobavit = 6 - len(hand.cards)
                hands_proba = hands[:]
                hands_proba = hands_proba[:1]
                deck.deal(hands_proba, per_hand=dobavit)

        def vzal(self, komu):
            for xxx in range(len(hand4.cards)):
                ttt = hand4.cards[0]
                hand4.give(ttt, komu)
            self.stol_restart()
            self.initUI()

        def stol_restart(self):
            for _ in range(6):
                self.labels[_].hide()
                self.labels1[_].hide()
            for rrr in range(len(self.btns)):
                self.btns[rrr].hide()
            for rrr in range(len(self.btns1)):
                self.btns1[rrr].hide()
            self.stol_cards.clear()
            hand4.clear()
            self.label6.hide()
            self.label7.hide()
            self.label8.hide()
            self.btn_bita.hide()
            self.btn_vzal.hide()
            self.berem_card_is_kolodi()
            self.col = 0



    def na_rukah(self):
        self.btns = [None for i in range(len(hand.cards))] #список кнопок карт игрока(hand.cards) и лабелек карт компа(hand2.cards)
        self.btns1 = [None for i in range(len(hand2.cards))]
        self.btns_names = []
        self.btns_names2 = []
        for col in range(len(self.btns)):
            self.btn = QPushButton(self)
            self.btn.setGeometry(180 + col * 30, 650, 112, 171)
            self.btns[col] = self.btn
            xxx = str(hand).split('\t')
            print('xxx',xxx)
            xxx = xxx[:-1]
            self.btns[col].setObjectName(xxx[col])#имя кнопки как элемент hand
            self.btns[col].setIcon(QIcon(f'cards\\{xxx[col]}.gif'))#картинка кнопки
            self.btns[col].setIconSize(QtCore.QSize(112, 171))
            self.btns_names.append(self.btns[col].objectName())
            self.btns[col].show()
            self.btns[col].clicked.connect(self.hodim)
        for col in range(len(self.btns1)):
            self.label = QLabel(self)
            self.label.setGeometry(180 + col * 30, 10, 120, 200)
            self.btns1[col] = self.label
            xxx = str(hand2).split('\t')
            xxx = xxx[:-1]
            self.btns1[col].setObjectName(xxx[col])
            self.fname1 = f'cards\\37.gif' #в строке ниже можно видеть карты компа
            # self.fname1 = f'cards\\{xxx[col]}.gif'
            self.pixmap = QPixmap(self.fname1)
            self.btns1[col].setPixmap(self.pixmap.scaled(112, 171))
            self.btns1[col].show()
            self.btns_names2.append(self.btns1[col].objectName())

    def hodim(self):
        self.xxx = self.sender().objectName()
        if self.player_hod:
            if self.can_podkidivat(self.btns_names):
                if self.podkidivat_var: #список с возможными вариантами карт для подкидывани
                    if self.xxx in self.podkidivat_var:
                        self.card_on_stol()#выкладываем карту на стол
                        self.hod_II()    #ход компа
                else:
                    self.card_on_stol()
                    self.hod_II()
        else:
            if self.proverka_pravilno_card(self.xxx):#проверка можно ли такой картой крыть
                self.card_on_stol()
                self.col += 1#счетчик лабелек для отображения карт(дал и покрыл)
                self.stol_cards.append(self.xxx) #список карт на столе для проверки можно ли подкидвать
                if self.can_podkidivat(self.btns_names2):
                    self.hod_II()
                else:
                    self.bita()



    def card_on_stol(self):
        if self.perviy_user:  # определяем на какой уровень будем выкладывать карты: на первый - когда подкидываем
            labels = self.labels[:]  # или на второй если отбиваемся
        else:
            labels = self.labels1[:]
            col = self.col1
        self.xxx = self.sender().objectName()
        self.fname1 = f'cards\\{self.xxx}.gif'
        self.pixmap = QPixmap(self.fname1)
        labels[self.col].setPixmap(self.pixmap.scaled(112, 171))
        rrr = self.btns_names.index(self.xxx)
        hand.give(hand.cards[rrr], hand4)
        for xxx in self.btns:
            xxx.hide()
        for xxx in self.btns1:
            xxx.hide()
        del self.btns[rrr]
        del self.btns_names[rrr]
        self.stol_cards.append(self.xxx)
        self.na_rukah()

        class FirstForm(QWidget):  # вводим имя игрока
            def __init__(self, *args):
                super().__init__()
                self.name = ''
                self.initUI(args)

            def initUI(self, args):
                self.setGeometry(300, 300, 300, 300)
                self.setWindowTitle('Имя игрока')
                self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
                self.lbl = QLabel(args[-1], self)
                self.lbl.setGeometry(20, 60, 100, 20)

                self.line = QLineEdit(self)
                self.line.setGeometry(80, 150, 200, 30)

                self.btns = QPushButton(self)
                self.btns.setGeometry(80, 250, 100, 30)
                self.btns.setText('Ок')
                self.btns.clicked.connect(self.close1)

            def close1(self):
                global name
                name = self.line.text()
                self.zapis_name_base()
                self.close()

            def zapis_name_base(self):
                con = sqlite3.connect("mydatabase_durak.db")
                cur = con.cursor()
                result = cur.execute(
                    '''SELECT * FROM results WHERE name LIKE ?''', (name,)).fetchall()
                if not result:
                    result = cur.execute("""INSERT INTO results(name, number_nikto, number_prongr, number_of_wins
                                       ) VALUES(?,?,?,?)""", (name, 0, 0, 0)).fetchall()
                con.commit()
                con.close()


def bita(self):
    self.stol_restart()  # прячем все со стола и по новой показываем
    self.perviy_user = not self.perviy_user
    self.player_hod = not self.player_hod
    self.initUI()


    def berem_card_is_kolodi(self):
        self.stol_cards.clear()
        if len(hand2.cards) < 6:
            dobavit = 6 - len(hand2.cards)
            hands_proba = hands[:]
            hands_proba = hands_proba[1:]
            deck.deal(hands_proba, per_hand=dobavit)
        if len(hand.cards) < 6:
            dobavit = 6 - len(hand.cards)
            hands_proba = hands[:]
            hands_proba = hands_proba[:1]
            deck.deal(hands_proba, per_hand=dobavit)

    def vzal(self, komu):
        for xxx in range(len(hand4.cards)):
            ttt = hand4.cards[0]
            hand4.give(ttt, komu)
        self.stol_restart()
        self.initUI()

    def stol_restart(self):
        for _ in range(6):
            self.labels[_].hide()
            self.labels1[_].hide()
        for rrr in range(len(self.btns)):
            self.btns[rrr].hide()
        for rrr in range(len(self.btns1)):
            self.btns1[rrr].hide()
        self.stol_cards.clear()
        hand4.clear()
        self.label6.hide()
        self.label7.hide()
        self.label8.hide()
        self.btn_bita.hide()
        self.btn_vzal.hide()
        self.berem_card_is_kolodi()
        self.col = 0


    class SecondForm(QWidget):  # форма в конце игры где можно либо посмотреть результаты либо закрыть
        def __init__(self, *args):
            super().__init__()
            self.initUI(args)

        def initUI(self, args):
            self.setGeometry(300, 300, 600, 600)
            self.setWindowTitle('Конец игры')
            self.lbl = QLabel(args[-1], self)
            self.lbl.setGeometry(20, 60, 100, 20)

            self.btns = QPushButton(self)
            self.btns.setGeometry(20, 150, 100, 30)
            self.btns.setText('Ок')
            self.btns.clicked.connect(self.close1)

            self.btn_res = QPushButton(self)
            self.btn_res.setGeometry(180, 150, 100, 30)
            self.btn_res.setText('Результаты')
            self.btn_res.clicked.connect(self.start)

            self.table = QTableWidget(self)
            self.table.setGeometry(QtCore.QRect(10, 180, 480, 300))
            self.table.setColumnCount(4)
            self.table.hide()

        def start(self):  # формируем таблицу с результатами
            self.table.show()
            con = sqlite3.connect("mydatabase_durak.db")
            cur = con.cursor()
            result = cur.execute(
                '''SELECT * FROM results''').fetchall()
            if result:
                result = sorted(list(result), key=lambda x: x[-1], reverse=True)
            title = ['Имя игрока', 'Кол-во ничьих', 'Кол-во поражений', 'Кол-во побед']
            self.table.setHorizontalHeaderLabels(title)
            if result:
                self.table.setColumnCount(4)
                self.table.setRowCount(0)
                for i, row in enumerate(result):
                    self.table.setRowCount(
                        self.table.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.table.setItem(
                            i, j, QTableWidgetItem(str(elem)))
            self.table.resizeColumnsToContents()
            con.close()

        def close1(self):
            os.execv(sys.executable, ['python'] + sys.argv)


            def end_game(self):
                self.btn_bita.hide()
                self.btn_vzal.hide()
                self.basa()  # записываем в базу результат
                self.open_second_form()  # конец игры, можно посмотреть результаты игр

            def basa(self):
                con = sqlite3.connect("mydatabase_durak.db")
                cur = con.cursor()
                result = cur.execute(
                    '''SELECT * FROM results WHERE name LIKE ?''', (name,)).fetchall()
                nikto, fails, wins = result[0][1], result[0][2], result[0][3]
                if not hand.cards:
                    wins += 1
                elif not hand2.cards:
                    fails += 1
                else:
                    nikto += 1
                result = cur.execute("""UPDATE
                results SET number_nikto = ?, number_prongr = ?, number_of_wins = ? 
                WHERE name = ?""", (nikto, fails, wins, name))
                con.commit()
                con.close()
#вроде бы не надо переделывать, но я не уверен:
    def perviy(self):#ходит тот, у кого наименьший козырь
        variants = []
        variants2 = []
        for _ in range(len(self.btns_names)):
            if self.btns_names[_][:4] == self.label7.objectName()[:4]:
                variants.append(self.btns_names[_])
        for _ in range(len(variants)-1):
            for j in range(len(variants) - 1 - _):
                if int(variants[j][4:]) > int(variants[j + 1][4:]):
                    variants[j], variants[j + 1] = variants[j + 1], variants[j]
        for _ in range(len(self.btns_names2)):
            if self.btns_names2[_][:4] == self.label7.objectName()[:4]:
                variants2.append(self.btns_names2[_])
        for _ in range(len(variants2) - 1):
            for j in range(len(variants2) - 1 - _):
                if int(variants2[j][4:]) > int(variants2[j + 1][4:]):
                    variants2[j], variants2[j + 1] = variants2[j + 1], variants2[j]
        if variants and variants2:
            if int(variants[0][4:]) < int(variants2[0][4:]):
                self.player_hod = True
                self.perviy_user = True
        elif not variants2:
            self.player_hod = True
            self.perviy_user = True
        self.open_first_form()


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


class Hand(object):#набор карт на руках у одного игрока
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = '<пусто>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=0):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Карты закончились')

    def vibor_kozir(self, handdd):
        hand = handdd
        if self.cards:
            kozir_card = self.cards[0]
            self.give(kozir_card, hand)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    deck = Deck()
    deck.populate()
    deck.shuffle()
    hand, hand2, hand3 = Hand(), Hand(), Hand()
    hands = [hand, hand2]
    deck.deal(hands, per_hand=6)
    hand4 = Hand()
    deck.vibor_kozir(hand3)

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())