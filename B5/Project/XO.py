import os
import time

print('Добро пожаловать в игру Крестики-Нолики!\n\n!!!Внимание!!!\n'
      'За попытку занять уже занятую клетку последует кара!')


def win_cond(f, t):
    for i in range(3):
        if f[i] == [t[-2]] * 3 or \
                f[0][i] == f[1][i] == f[2][i] == t[-2] or \
                f[0][0] == f[1][1] == f[2][2] == t[-2] or \
                f[2][0] == f[1][1] == f[0][2] == t[-2]:
            os.system('cls')
            print(f'Победили {t[-2].upper()}!')
            return False
    if not '-' in f[0] and not '-' in f[1] and not '-' in f[2]:
        os.system('cls')
        print(f'Победила дружба!')
        return False
    else:
        return True


def show_f(field):
    print(f'\n  0 1 2')
    for ind, val in enumerate(field):
        print(f'{ind} {" ".join(val)}')


def game():
    pf = [['-'] * 3 for _ in range(3)]
    turns = ['o', 'x'] * 6

    while win_cond(pf, turns):
        show_f(pf)
        current_fig = turns[-1]
        trn = input(f'Введите координаты следующего {current_fig.upper()} через пробел ('
                    f'ряд колонка):\n').split()
        os.system('cls')
        try:
            if pf[int(trn[0])][int(trn[1])] == '-':
                pf[int(trn[0])][int(trn[1])] = current_fig
                turns.pop()
            else:
                os.system('cls')
                print(f'Хорошая попытка, но нет. Вы дисквалифицированы! Победил {turns[-2].upper()}\n')
                break
        except:  # Обрабатываем все возможные варианты неверного ввода за раз
            print('Неверный формат ввода, попробуйте еще раз через 3 секунды.\n')
            time.sleep(3)

    q = input('Хотите сыграть еще раз? (Y/N) ')
    if q.lower() == 'y':
        os.system('cls')
        game()


game()
