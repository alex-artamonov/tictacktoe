from random import choice
from random import shuffle
from sys import exit

HUMAN_NAME = 'human_name'
HUMAN_MARK = 'human_mark'
COMPUTER_MARK = 'computer_mark'
COMPUTER_NAME = 'computer_name'
CURRENT_PLAYER = 'current_player'
COUNTER = 'counter'
CURRENT_MOVE = 'current_move'
SHIFT_FIELD = 10
HEADS_TALES = ('1', '2')
INP_INVITE = "?--> "
EMPTY = ' '
CROSS = 'X'
NOUGHT = 'O'
players_moves = {
    HUMAN_NAME: '',
    HUMAN_MARK: '',
    COMPUTER_NAME: 'Компьютер',
    COMPUTER_MARK: '',
    CURRENT_PLAYER: '',
    CURRENT_MOVE: (),
    COUNTER: 0
}
field = {(0, 0): EMPTY, (0, 1): EMPTY, (0, 2): EMPTY,
         (1, 0): EMPTY, (1, 1): CROSS, (1, 2): CROSS,
         (2, 0): NOUGHT, (2, 1): EMPTY, (2, 2): EMPTY}

legal_moves = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2)]
# legal_moves = ['00', '01']

# BEST_MOVES = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]

ROW_0 = {(0, 0), (0, 1), (0, 2)}
ROW_1 = {(1, 0), (1, 1), (1, 2)}
ROW_2 = {(2, 0), (2, 1), (2, 2)}
COL_0 = {(0, 0), (1, 0), (2, 0)}
COL_1 = {(0, 1), (1, 1), (2, 1)}
COL_2 = {(0, 2), (1, 2), (2, 2)}
DIAG_0 = {(0, 0), (1, 1), (2, 2)}
DIAG_1 = {(0, 2), (1, 1), (2, 0)}

DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]

score = {}


def clear_moves():
    global legal_moves
    legal_moves = [(0, 0), (0, 1), (0, 2),
                   (1, 0), (1, 1), (1, 2),
                   (2, 0), (2, 1), (2, 2)]


def clear_field():
    global field
    # print("hi from clear_field()")
    field = {(0, 0): EMPTY, (0, 1): EMPTY, (0, 2): EMPTY,
             (1, 0): EMPTY, (1, 1): EMPTY, (1, 2): EMPTY,
             (2, 0): EMPTY, (2, 1): EMPTY, (2, 2): EMPTY}
    clear_moves()


def output_moves():
    # s = '[%s]' % ', '.join(map(str, legal_moves_str()))
    s = ', '.join(legal_moves_str())
    s = "Возможные ходы: " + (s or "ходов больше нет.")
    return s


def create_score(human_name):
    global players_moves
    global score
    computer_name = 'Компьютер'
    players_moves[COMPUTER_NAME] = computer_name
    players_moves[HUMAN_NAME] = human_name
    if len(score) == 0:
        score[human_name], score[computer_name] = 0, 0
        return True
    else:
        print('From create_score(): something is wrong')
        return False


def update_score(winner):
    if len(score) > 0:
        score[winner] += 1
    else:
        print('From update_score(): something is wrong')


def print_score():
    # print('score:', score)
    computer_name = players_moves[COMPUTER_NAME]
    human_name = players_moves[HUMAN_NAME]
    # print('computer_name:', computer_name, 'human_name:', human_name)
    head = '| ' + computer_name + ' | ' + human_name + ' |'
    s_border = '=' * len(head)
    numbers = '|' + str(score[computer_name]).center(len(computer_name) + 2)
    numbers += '|' + str(score[human_name]).center(len(human_name) + 2) + '|'
    lst = [s_border, head, numbers, s_border]
    s = '\n'.join(lst)
    s = shift_right(s, 6)
    print(s)


def view_dimensions():
    view = []

    for dim in DIMENSIONS:
        dct = {cell: field[cell] for cell in dim}
        view.append(dct)
        # print(dim)
    # [print(d) for d in view]
    return view



def shift_right(text, n=2):
    s = ''
    ls = text.splitlines(True)
    for line in ls:
        s += ' ' * n + str(line)
    return s


def border(fnc):
    def wrapper(nbr_spaces=SHIFT_FIELD):

        counter = players_moves[COUNTER]
        current_player = players_moves[CURRENT_PLAYER]
        current_move = players_moves[CURRENT_MOVE]

        # nbr_spaces = 10
        if counter > 0:
            print(f"\n~~~Ход № {counter}, {current_player}:{current_move}~~~")
            fnc(nbr_spaces)
            print()
        else:
            clear_field()
            print(f"\nВот как выглядит игровое поле. Сначала указываются ряды, потом - столбцы:")
            print(output_moves())
            fnc(nbr_spaces)
            print()
    return wrapper


@border
def print_field_old(spaces=2):
    s = "\n   0  1  2\n"
    n = 0

    for i in range(3):
        # print(list(field[i][j] for j in range(3)))
        s += str(n)
        for j in range(3):
            s = s + '  ' + field[(i, j)]
        s += '\n'
        n += 1
    s = s[0:-1]  # уберем 1 переход на новую строку
    s = shift_right(s, spaces)
    print(s)


@border
def print_field(spaces):
    s = "\n    0   1   2\n\n"
    n = 0
    horiz_line = '\n    ---------\n'
    for i in range(3):
        # print(list(field[i][j] for j in range(3)))
        s += str(n)
        t = ' '.join(field[(i, j)] + ' |' for j in range(3))[:-1]   # уберем 1 вертикальный разделитель
        s += '   ' + t + horiz_line
        n += 1
    s = s[:-len(horiz_line)-1]  # уберем 1 горизонтальный разделитель
    s = shift_right(s, spaces)
    print(s)


def legal_moves_str():
    global legal_moves
    lst = [str(t[0]) + str(t[1]) for t in legal_moves]
    return lst


def no_more_moves():
    res = len(legal_moves) == 0
    return res


def play_again_or_leave():
    human_name = players_moves[HUMAN_NAME]
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
    # global human_name

    print(f"{players_moves[HUMAN_NAME]}, похоже, у нас ничья!")
    print_score()
    play_again_or_leave()


def human_move():

    # global players_moves
    # current_player = players_moves[CURRENT_PLAYER]
    human_mark = players_moves[HUMAN_MARK]
    human_name = players_moves[HUMAN_NAME]
    assert human_mark != ''
    # players_moves[CURRENT_PLAYER] = players_moves[human_name]
    # players_moves[CURRENT_PLAYER] = 'asdf'
    d = {NOUGHT: 'за нолики', CROSS: 'за крестики'}
    players_moves[CURRENT_PLAYER] = players_moves[HUMAN_NAME]
    # print('from human_move:', players_moves)
    if no_more_moves():
        action_draw()
    else:
        # current_player = human_name
        print(f"Ваш ход {d[human_mark]} (первая цифра ряд, вторая - столбец):")
        while True:
            mv = input(INP_INVITE)
            if mv in legal_moves_str():
                mv = (int(mv[0]), int(mv[1]))
                players_moves[CURRENT_MOVE] = mv
                # print("mv:", mv)
                # print('hi from human_move:else, players_moves:', players_moves)
                field[mv] = human_mark
                players_moves[COUNTER] += 1
                legal_moves.remove(mv)
                print_field(10)
                break
            else:
                s = '[%s]' % ', '.join(map(str, legal_moves_str()))
                s = s[1:-1]
                print(f'Такого хода ({mv}) нет, попробуйте еще раз:', s)
                continue
        win_or_continue(human_name)


def computer_move():
    # global players_moves

    computer_name = players_moves[COMPUTER_NAME]
    computer_mark = players_moves[COMPUTER_MARK]
    human_mark = players_moves[HUMAN_MARK]
    assert computer_mark != ''
    assert human_mark != ''

    players_moves[CURRENT_PLAYER] = players_moves[COMPUTER_NAME]
    if no_more_moves():
        action_draw()
    else:
        mv = kill() or check_danger(human_mark) or attack() or try_best_moves() or random_move()
        players_moves[CURRENT_MOVE] = mv
        field[mv] = computer_mark
        legal_moves.remove(mv)
        #        print('hi from human_move, legal_moves: ', str(legal_moves))
        players_moves[COUNTER] += 1
        print_field()
        print(output_moves())
        win_or_continue(computer_name)


def kill():
    # print('hi from kill')
    global players_moves

    assert players_moves[COMPUTER_MARK] != ''
    print('I\'m trying to kill')
    msg = "*killing move!*"
    res = check_danger(players_moves[COMPUTER_MARK], msg)
    print('from kill:', res)
    return check_danger(players_moves[COMPUTER_MARK], msg)


def check_danger(mark, msg=''):
    # print("human_mark:", human_mark, "mark:", mark or "empty string")
    # assert mark != ''
    print('hi from check_danger', mark, 'msg:', msg)
    #    bool = False
    s = msg or '*Danger! I\'m defending!*'
    for dim in DIMENSIONS:
        i = where_attack([field[cell] for cell in dim], mark)
        if i is None:
            pass
        else:
            print(s)
            return dim[i]
    return False


def attack():
    mark = players_moves[COMPUTER_MARK]
    for dim in DIMENSIONS:
        keys = [cell for cell in dim]
        values = [field[cell] for cell in dim]
        # print(keys, values)
        if values.count(EMPTY) == 2 and values.count(mark) == 1:
            # print(lst, dim, lst.index(EMPTY))
            mv = keys[values.index(EMPTY)]
            print("*Attacking!*", mv)
            # print(mv)
            return mv
        # else:
        #     continue


def random_move():
    global legal_moves
    print('*random move!*')
    return choice(legal_moves)


def try_best_moves():
    best_moves = [(0, 0), (0, 2), (2, 0), (2, 2)]
    shuffle(best_moves)
    best_moves = [(1, 1)] + best_moves
    # print('best_moves:', best_moves)
    for mv in best_moves:
        # print(mv)
        if mv in legal_moves:
            print("*one of the best moves!*")
            return mv
        else:
            continue


def win_or_continue(player):
    global players_moves
    human_name = players_moves[HUMAN_NAME]
    computer_name = players_moves[COMPUTER_NAME]
    human_mark = players_moves[HUMAN_MARK]
    computer_mark = players_moves[COMPUTER_MARK]
    mark = ''
    who_moves = None

    if player == human_name:
        msg = f'- Congrats, you win, human", {human_name}'
        who_moves = computer_move
        mark = human_mark
    elif player == computer_name:
        msg = f"- I win, human {human_name}! ;-)"
        who_moves = human_move
        mark = computer_mark
    else:
        msg = "there's something wrong with this program!"

    if is_win(mark):
        print(f'*winning move: {players_moves[CURRENT_MOVE]}*')
        print(msg)
        update_score(player)
        print_score()
        play_again_or_leave()
    else:
        who_moves()


def is_win(mark):

    for dim in DIMENSIONS:
        res = all(field[cell] == mark for cell in dim)
        if res:
            # print(res)
            print(f'Победу одержал: {players_moves[CURRENT_PLAYER]} ходом {players_moves[CURRENT_MOVE]}')
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
    global players_moves

    computer_name = players_moves[COMPUTER_NAME]
    human_name = players_moves[HUMAN_NAME]

    # print("from initialize game: players_moves:", players_moves)
    players_moves[COUNTER] = 0
    print(f"Для начала определим, кто первый ходит, {computer_name} или "
          f"{human_name}. Первый будет ходить крестиками.")
    print('орел? (1) или решка? (2)')
    clear_field()
    s = input(INP_INVITE)
    if s in HEADS_TALES:
        t = choice(HEADS_TALES)
        if s.upper() == t:
            players_moves[HUMAN_MARK] = CROSS
            players_moves[COMPUTER_MARK] = NOUGHT
            players_moves[CURRENT_PLAYER] = human_name
            print(f"Угадали, {human_name} - ходите первым за крестики!")
            print(output_moves())
            human_move()
        else:
            players_moves[HUMAN_MARK] = NOUGHT
            players_moves[COMPUTER_MARK] = CROSS
            players_moves[CURRENT_PLAYER] = players_moves[COMPUTER_NAME]
            print(f"Не повезло, {human_name} - я хожу первым за крестики!")
            computer_move()
    else:
        print("Cтранный выбор, ну ладно, тогда мой ход.")
        players_moves[HUMAN_MARK] = NOUGHT
        players_moves[COMPUTER_MARK] = CROSS
        computer_move()


def greeting():
    print("Ваше имя?")
    players_moves[HUMAN_NAME] = input(INP_INVITE).capitalize()
    print(f"Привет, {players_moves[HUMAN_NAME]}!")
    if create_score(players_moves[HUMAN_NAME]):
        print_score()
    else:
        print('From greeting(): something is wrong')


def start_game():
    greeting()
    print_field()
    initialize_game()


# # print("random move:", choice(legal_moves))
# # human_move()
# initialize_game()

# print(DIMENSIONS[2])

# start_game()
# print_field()
def print_vw_dimensions():
    [print(dim) for dim in view_dimensions()]


# print_vw_dimensions()

def check_attack():
    vw = view_dimensions()
    for dim in vw:
        keys = list(dim.keys())
        values = list(dim.values())
        if values.count(CROSS) == 2 and values.count(EMPTY) == 1:
            print(dim, keys[values.index(EMPTY)])



check_attack()


