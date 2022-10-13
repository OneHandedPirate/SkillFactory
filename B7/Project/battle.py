import os
import time
from random import randint


class GameException(Exception):
    pass


class BoardOutException(GameException):
    def __str__(self):
        return 'Координаты вне доски'


class BoardUsedException(GameException):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку'


class BoardWrongShipException(GameException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # задаем условия равенства точек
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Ship:
    def __init__(self, start, length, orient):
        self.start = start  # Начало корабля (нос)
        self.length = length  # длина корабля
        self.orient = orient  # ориентация корабля (0 - гор., 1 - верт)
        self.lives = length  # жизни корабля равны его длине

    @property
    def dots(self):  # исходя из параметров корабля расчитываются координаты его точек
        s_dots = []  # список точек корабля
        for i in range(self.length):  # проходимся циклом от длины корабля
            x = self.start.x
            y = self.start.y

            if self.orient == 0:
                x += i

            elif self.orient == 1:
                y += i

            s_dots.append(Dot(x, y))  # добавляем получившуюся точку к списку

        return s_dots  # выводим список точек в виде кортежей

    def shooten(self, shot):  # проверяем каждый корабль на попадание при каждом выстреле
        return shot in self.dots


class Board:
    def __init__(self, size, hidden=False, ):
        self.size = size  # размер доски
        self.hidden = hidden  # переключатель видимости доски

        self.killed = 0  # количество "убитых" кораблей

        self.field = [["o"] * size for _ in range(size)]  # изначальное отображение "пустой" доски

        self.busy_dots = []  # занятые точки
        self.ships = []  # список кораблей доски

    def __str__(self):  # выводим доску на экран
        render = ''
        render += '\033[33m    '
        for i in range(1, self.size + 1):
            render += f'{i}   '
        render += '\033[0m'
        for c, r in enumerate(self.field):
            render += f'\n\033[33m{c + 1}\033[0m | ' + ' | '.join(r) + ' |'

        if self.hidden:  # если доска скрыта - скрываем корабли.
            render = render.replace('■', 'o')

        return render

    def out(self, dot):  # проверяем, не выходит ли проверяемая точка за пределы доски
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def ship_countour(self, ship, dead=False):  # "обводим" контур корабля чтобы корабли не слипались
        countour = [  # определяем все точки вокруг проверяемой точки (0,0)
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dot in ship.dots:  # проходимся по списку точек корабля
            for dx, dy in countour:  # для каждой точки корабля применяем "контур"
                c = Dot(dot.x + dx, dot.y + dy)
                if not (self.out(c)) and c not in self.busy_dots:
                    if dead:
                        self.field[c.x][c.y] = '.'  # помечаем точку точкой
                    self.busy_dots.append(c)  # добавляем точку к списку занятых

    def add_ship(self, ship):
        for dot in ship.dots:  # проверка точек корабля на принадлежность к полю и невхождение в список занятых
            if self.out(dot) or dot in self.busy_dots:
                raise BoardWrongShipException()

        for dot in ship.dots:
            self.field[dot.x][dot.y] = "■"  # помечаем точки кораблей смайликами
            self.busy_dots.append(dot)  # добавляем точку в список занятых

        self.ships.append(ship)  # добавляем корабль в список кораблей
        self.ship_countour(ship)  # вызываем метод ship_countour для обработки точек вокруг корабля

    def shot(self, dot):  # обработка выстрелов
        if self.out(dot):  # если точка за пределами игрового поля
            raise BoardOutException()

        if dot in self.busy_dots:  # если точка в занятых
            raise BoardUsedException

        self.busy_dots.append(dot)  # добавляем точку в список занятых

        for ship in self.ships:  # проверяем циклом попали или нет по кораблям из списка
            if dot in ship.dots:
                ship.lives -= 1  # если попал - минус одна жизнь у корабля
                self.field[dot.x][dot.y] = 'X'
                if ship.lives == 0:  # если жизней нет - корабль убит
                    self.killed += 1
                    self.ship_countour(ship, dead=True)  # показывает "контур" корабля (точки вокруг него)
                    print('Корабль потоплен!')
                else:
                    print('Корабль подбит!')
                time.sleep(2)
                return True  # можно сделать еще один ход

        self.field[dot.x][dot.y] = '.'
        print('Мимо!')
        time.sleep(2)
        return False  # ход переходит к другому игроку

    def clear_bdots(self):
        self.busy_dots = []  # очищает список занятых клеток после расстановки кораблей для корректной игры


class Player:  # дефолтный класс игрока
    def __init__(self, board, enemy_board):  # принимает свою доску и доску соперника
        self.board = board
        self.enemy_board = enemy_board

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                repeat = self.enemy_board.shot(
                    self.ask())  # в качестве аргумента метода shot выступает точка, по которой ведется огонь
                return repeat  # В случае промаха цикл прерывается, иначе - еще один выстрел
            except GameException as e:
                print(e)


class Bot(Player):
    def ask(self):  # опрос бота
        dot = Dot(randint(0, 5), randint(0, 5))  # бот "выбирает" точку случайным образом
        print(f'Бот думает...')
        time.sleep(2)
        print(f'Ход бота: {dot.x + 1} {dot.y + 1}')
        return dot  # возвращаем случайную точку


class User(Player):
    def ask(self):  # опрос игрока
        while True:
            dot = input('Ваш ход:\n').split()

            # Проверяем корректность ввода
            if len(dot) != 2:
                print('Введите 2 координаты (ряд колонка)')
                continue

            if not (dot[0].isdigit()) or not (dot[1].isdigit()):
                print('Введите числа!')
                continue

            return Dot(int(dot[0]) - 1, int(dot[1]) - 1)  # возвращаем точку, которую ввел игрок


class Game:
    def __init__(self):
        self.welcome()
        self.size = self.set_size()
        self.fleet = self.set_fleet()
        users_b = self.random_board()  # генерирует доску игрока со случайной расстановкой кораблей
        bots_b = self.random_board()  # генерирует доску бота со случайной расстановкой кораблей
        bots_b.hidden = True  # скрывает от игрока расположение кораблей бота

        # раздаем боту и игроку их доски
        self.bot = Bot(bots_b, users_b)
        self.user = User(users_b, bots_b)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        board = Board(size=self.size)
        attempts = 0  # счетчик попыток собрать доску
        for l in self.fleet:
            while True:
                attempts += 1
                if attempts > 3000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except:
                    pass
        board.clear_bdots()
        return board

    @staticmethod
    def welcome():  # приветствие
        print(f'{"*" * 37}\n Добро пожаловать в игру Морской бой!\n\n'
              f'      Формат ввода: ряд колонка\n'
              f'                Удачи!\n{"*" * 37}\n\n')
        time.sleep(5)

    def set_size(self):  # Метод для выбора размера доски
        s = input('Введите число от 5 до 9 в качестве размера игрового поля.\n'
                  'В случае некорректного ввода или '
                  'нажатия Enter без ввода значения '
                  'размер поля будет установлен на 6.\n')
        if s.isdigit() and 5 <= int(s) <= 9:
            return int(s)
        else:
            return 6

    def set_fleet(self):  # выбор размера флота и кораблей в нем в зависимости от размера доски
        fleets = {
            '5': [3, 2, 2, 1, 1, 1],
            '6': [3, 2, 2, 1, 1, 1, 1],
            '7': [4, 3, 3, 2, 2, 1, 1, 1, 1],
            '8': [4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1],
            '9': [4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]
        }
        return fleets[str(self.size)]

    def loop(self):  # основной цикл игры
        turn = 0  # очередность ходов. Четные - человек, нечетные - бот
        while True:
            os.system('cls')
            print("-" * 20)
            print("Ваша доска:")
            print(self.user.board)
            print("-" * 20)
            print("Доска бота:")
            print(self.bot.board)
            if turn % 2 == 0:
                print("-" * 20)
                print("Ходите!")
                repeat = self.user.move()
            else:
                print("-" * 20)
                print("Ходит бот!")
                repeat = self.bot.move()
            if repeat:
                turn -= 1

            # условия выигрыша - все корабли уничтожены
            if self.bot.board.killed == len(self.fleet):
                print("-" * 20)
                print("Вы выиграли выиграл!")
                break

            if self.user.board.killed == len(self.fleet):
                print("-" * 20)
                print("Бот выиграл!")
                break
            turn += 1


if __name__ == '__main__':
    g = Game()
    g.loop()
