import os


def win_cond(f, t):
    for i in range(3):
        if f[i] == [t[-2]] * 3 or \
                f[0][i] == f[1][i] == f[2][i] == t[-2] or \
                f[0][0] == f[1][1] == f[2][2] == t[-2] or \
                f[2][0] == f[1][1] == f[0][2] == t[-2]:
            os.system('cls')
            show_f(f)
            print(f'\nПобедил игрок {t[-2].upper()}!')
            return True
    if len(t) == 3:
        os.system('cls')
        show_f(f)
        print(f'\nПобедила дружба!')
        return True
    else:
        return False


def show_f(field):
    print(f'\n \033[33m 0 1 2\033[0m')
    for ind, val in enumerate(field):
        print(f'\033[33m{ind}\033[0m {" ".join(val)}')


def game():
    pf = [['-'] * 3 for _ in range(3)]
    turns = ['o', 'x'] * 6

    while not win_cond(pf, turns):   #Пока условия выигрыша не соблюдаются игра продолжается.
        print(f'Ход {13 - len(turns)}, ходит игрок {turns[-1].upper()}')
        show_f(pf)
        current_fig = turns[-1]
        trn = input(f'Введите координаты следующего {current_fig.upper()} через пробел ('
                    f'ряд колонка):\n').split()
        os.system('cls')
        try:
            if pf[int(trn[0])][int(trn[1])] == '-' and int(trn[0]) >= 0 and int(trn[1]) >= 0:
                pf[int(trn[0])][int(trn[1])] = current_fig
                turns.pop()
            elif int(trn[0]) < 0 or int(trn[1]) < 0:
                print('Координаты должны быть положительными, попробуйте еще раз\n')
            else:
                print(f'Хорошая попытка, но нет. Вы дисквалифицированы!'
                      f'Победил игрок {turns[-2].upper()}\n')
                break
        except:  # Обрабатываем все возможные варианты неверного ввода за раз (числа вне диапазона, некорректный ввод)
            print('Неверный формат ввода, попробуйте еще раз\n')

    q = input('Хотите сыграть еще раз? (Y/N)\n')
    if q.lower() == 'y':
        os.system('cls')
        game()


if __name__ == '__main__':
    print('Добро пожаловать в игру Крестики-Нолики!\n\n!!!Внимание!!!\n'
          'За попытку занять уже занятую клетку последует кара!\n')

    game()
