from random import choice
from random import shuffle
from sys import exit

human_name = "Human"
human_mark = ""
computer_name = "Компьтер"
computer_mark = ""
counter = 0
current_player = ""
current_move = ()
HEADS_TALES = ('1', '2')
INP_INVITE = "?--> "
EMPTY = '-'
CROSS = 'X'
NOUGHT = 'O'
field = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, NOUGHT, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

legal_moves = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2)
               ]
# legal_moves = ['00', '01']

# BEST_MOVES = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]

ROW_0 = [(0, 0), (0, 1), (0, 2)]
ROW_1 = [(1, 0), (1, 1), (1, 2)]
ROW_2 = [(2, 0), (2, 1), (2, 2)]
COL_0 = [(0, 0), (1, 0), (2, 0)]
COL_1 = [(0, 1), (1, 1), (2, 1)]
COL_2 = [(0, 2), (1, 2), (2, 2)]
DIAG_0 = [(0, 0), (1, 1), (2, 2)]
DIAG_1 = [(0, 2), (1, 1), (2, 0)]

DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]

tally = {}


def clear_moves():
    global legal_moves
    legal_moves = [(0, 0), (0, 1), (0, 2),
                   (1, 0), (1, 1), (1, 2),
                   (2, 0), (2, 1), (2, 2)
                   ]


def clear_field():
    global field
    # print("hi from clear_field()")
    field = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    clear_moves()


def output_moves():
    # s = '[%s]' % ', '.join(map(str, legal_moves_str()))
    s = ', '.join(legal_moves_str())
    s = "Возможные ходы: " + (s or "ходов больше нет.")
    return s

def create_tally(name):
    global computer_name
    global tally
    if len(tally) == 0:
        tally = {name: 0, computer_name: 0}
    else:
        print('From create_tally(): something is wrong')


def update_tally(winner):
    global tally
    if len(tally) > 0:
        tally[winner] += 1
    else:
        print('From update_tally(): something is wrong')


def print_tally():
    global tally
    head = '| ' + computer_name + ' | ' + human_name + ' |'
    border = '=' * len(head)
    numbers = '|' + str(tally[computer_name]).center(len(computer_name) + 2)
    numbers += '|' + str(tally[human_name]).center(len(human_name) + 2) + '|'
    lst = [border, head, numbers, border]
    s = '\n'.join(lst)
    print(s)
    shift_right(s, 4)
    print()
    print(s)
    # print(border)
    # print(head)
    # print(border)
    # print(numbers)
    # print(border)


def shift_right(text, n=2):
    s = ''
    ls = text.split('\n')
    for line in ls:
        s += ' ' * n + str(line) + '\n'
    return s


def border(fnc):
    def wrapper(nbr_spaces=10):
        global counter
        global current_player
        global current_move

        if counter > 0:
            print(f"\n~~~Ход № {counter}, {current_player}:{current_move}~~~")
            fnc(nbr_spaces)
        else:
            clear_field()
            print(f"\nВот как выглядит игровое поле. Сначала указываются ряды, потом - столбцы:")
            print(output_moves())
            fnc(nbr_spaces)
    return wrapper


@border
def print_field(spaces=2):

    s = "\n   0  1  2\n"
    n = 0

    for i in range(3):
        # print(list(field[i][j] for j in range(3)))
        s += str(n)
        for j in range(3):
            s = s + '  ' + field[i][j]
        s += '\n'
        n += 1
    s = s[0:-1] #уберем 1 переход на новую строку
    s = shift_right(s, spaces)
    print(s)
    # counter += 1






def legal_moves_str():
    global legal_moves
    lst = [str(t[0]) + str(t[1]) for t in legal_moves]
    return lst


def no_more_moves():
    res = len(legal_moves) == 0
    return res


def play_again_or_leave():
    print("Сыграем еще? (Y/n)")
    reply = input(INP_INVITE).upper()
    if reply in ('Y', ''):
        res = True
    elif reply == 'N':
        res = False
    else:
        print(f'не понял ответа, {human_name}, но видимо, нет')
        res = False
    if res:
        print("Отлично, следующая игра!")
        initialize_game()
    else:
        print(f"Ну ладно, пока, {human_name}!")
        exit(0)


def action_draw():
    global human_name
    print(f"{human_name}, похоже, у нас ничья!")
    print_tally()
    play_again_or_leave()


def move_player():
    global human_mark
    global counter
    global current_player
    global current_move
    d = {NOUGHT: 'за нолики', CROSS: 'за крестики'}
    # if human_mark == NOUGHT:
    #     s = 'за нолики'
    # elif human_mark == CROSS:
    #     s = 'за крестики'
    # else:
    #     print("from move_player: something weird happened!")

    if no_more_moves():
        action_draw()
    else:
        current_player = human_name
        print(f'Ваш ход {d[human_mark]} (первая цифра ряд, вторая - столбец):')
        while True:
            mv = input(INP_INVITE)
            if mv in legal_moves_str():
                mv = (int(mv[0]), int(mv[1]))
                current_move = mv
                print("mv:", mv)
                field[mv[0]][mv[1]] = human_mark
                counter += 1
                legal_moves.remove(mv)
                print_field(10)
                break
            else:
                s = '[%s]' % ', '.join(map(str, legal_moves_str()))
                s = s[1:-1]
                print(f'Такого хода ({mv}) нет, попробуйте еще раз:', s)
                continue
        win_or_continue(human_name)


def try_kill():
    # print('hi from try_kill')
    global computer_mark
    assert computer_mark != ''
    # print('I\'m trying to kill')
    msg = "*killing move!*"
    return check_danger(computer_mark, msg)


def check_danger(mark, msg=''):
    # print("human_mark:", human_mark, "mark:", mark or "empty string")
    # assert mark != ''
    # print('hi from check_danger', mark)
    #    bool = False
    s = msg or '*Danger! I\'m defending!*'
    for dim in DIMENSIONS:
        i = where_attack([field[cell[0]][cell[1]] for cell in dim], mark)
        if i is None:
            pass
        else:
            print(s)
            return dim[i]
    return False


def random_move():
    global legal_moves
    print('*random move!*')
    return choice(legal_moves)


def try_best_moves():
    best_moves = [(0, 0), (0, 2), (2, 0), (2, 2)]
    shuffle(best_moves)
    best_moves = [(1, 1)] + best_moves
    print('best_moves:', best_moves)
    for mv in best_moves:
        # print(mv)
        if mv in legal_moves:
            print("*one of the best moves!*")
            return mv
        else:
            continue


def win_or_continue(player):
    global human_name
    global computer_name
    global human_mark
    global computer_mark
    if player == human_name:
        msg = f'- Congrats, you win, human", {human_name}'
        who_moves = move_machine
        mark = human_mark
    elif player == computer_name:
        msg = f"- I win, human {human_name}! ;-)"
        who_moves = move_player
        mark = computer_mark
    else:
        msg = "there's something wrong with this program!"

    if is_win(mark):
        print(f'*winning move: {current_move}*')
        print(msg)
        update_tally(player)
        print_tally()
        play_again_or_leave()
    else:
        who_moves()

# def swap_mark(mark):
#     if mark == CROSS:
#         return NOUGHT
#     elif mark == NOUGHT:
#         return CROSS
#     else:
#         print('from something is wrong: the mark is ', mark)


def move_machine():
    global current_player
    global current_move
    global human_name
    global human_mark
    global computer_mark
    global counter

    if no_more_moves():
        action_draw()
    else:
        current_player = computer_name
        mv = try_kill() or check_danger(human_mark) or try_best_moves() or random_move()
        current_move = mv
        field[mv[0]][mv[1]] = computer_mark
        legal_moves.remove(mv)
        #        print('hi from move_player, legal_moves: ', str(legal_moves))
        counter += 1
        print_field()
        print(output_moves())
        win_or_continue(computer_name)


def is_win(mark):
    global field
    for dim in DIMENSIONS:
        res = all(field[cell[0]][cell[1]] == mark for cell in dim)
        if res:
            # print(res)
            print(f'Победу одержал: {current_player} ходом {current_move}')
            return True


def where_attack(triad, mark):
    bln = triad.count(EMPTY) == 1
    if not bln:
        return None
    else:
        i = triad.index(EMPTY)
        triad.pop(i)
        if triad[0] == triad[1] == mark:
            return i
        else:
            return None


def initialize_game():
    global HEADS_TALES
    global computer_mark
    global human_mark
    global counter

    counter = 0
    print(f"Для начала определим, кто первый ходит, {computer_name} или "
          f"{human_name}. Первый будет ходить крестиками.")
    print('орел? (1) или решка? (2)')
    clear_field()
    s = input(INP_INVITE)
    if s in HEADS_TALES:
        t = choice(HEADS_TALES)
        if s.upper() == t:
            human_mark = CROSS
            computer_mark = NOUGHT
            print("Угадали - ходите первым за крестики!")
            print(output_moves())
            move_player()
        else:
            human_mark = NOUGHT
            computer_mark = CROSS
            print("Не повезло - я хожу первым за крестики!")
            move_machine()
    else:
        print("Cтранный выбор, ну ладно, тогда мой ход.")
        human_mark = NOUGHT
        computer_mark = CROSS
        move_machine()


def greeting():
    global human_name
    print("Ваше имя?")
    human_name = input(INP_INVITE).capitalize()
    print(f"Привет, {human_name}!")
    create_tally(human_name)
    print_tally()


def start_game():
    greeting()
    print_field()
    initialize_game()

# # print("random move:", choice(legal_moves))
# # move_player()
# initialize_game()

# print(DIMENSIONS[2])


