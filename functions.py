from random import choice
from random import shuffle
from sys import exit
import os

RULE_1 = "*Первое правило крестиков-ноликов: если есть возможность - то делать выигрышный ход*"
RULE_2 = "*Второе правило  крестиков-ноликов: предотвратить немедленный проигрыш*"

QUIT = "QUIT"
HUMAN_NAME = 'human_name'
HUMAN_MARK = 'human_mark'
COMPUTER_MARK = 'computer_mark'
COMPUTER_NAME = 'computer_name'
CURRENT_PLAYER = 'current_player'
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
}
field = {(0, 0): EMPTY, (0, 1): EMPTY, (0, 2): EMPTY,
         (1, 0): EMPTY, (1, 1): EMPTY, (1, 2): EMPTY,
         (2, 0): EMPTY, (2, 1): EMPTY, (2, 2): EMPTY}


ROW_0 = [(0, 0), (0, 1), (0, 2)]
ROW_1 = [(1, 0), (1, 1), (1, 2)]
ROW_2 = [(2, 0), (2, 1), (2, 2)]
COL_0 = [(0, 0), (1, 0), (2, 0)]
COL_1 = [(0, 1), (1, 1), (2, 1)]
COL_2 = [(0, 2), (1, 2), (2, 2)]
DIAG_0 = [(0, 0), (1, 1), (2, 2)]
DIAG_1 = [(0, 2), (1, 1), (2, 0)]
CORNERS = [(0, 0), (0, 2), (2, 2), (2, 0)]
SIDES = [(0, 1), (1, 2), (2, 1), (1, 0)]


DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]
# previous_human_move = ()
score = {}


def get_moves_count():
    lst = list(field.values())
    return len(lst) - lst.count(EMPTY)


def get_legal_moves():
    return [key for (key, value) in field.items() if value == EMPTY]


def clear_field():
    global field
    for cell in field:
        field[cell] = EMPTY



def output_moves():
    # s = '[%s]' % ', '.join(map(str, legal_moves_str()))
    output = ', '.join(legal_moves_str())
    output = f"Возможные ходы: {(output or 'ходов больше нет.')}"
    return output


def create_score(human_name):
    global players_moves
    global score
    computer_name = 'Компьютер'
    players_moves[COMPUTER_NAME] = computer_name
    players_moves[HUMAN_NAME] = human_name
    score[human_name], score[computer_name] = 0, 0



def update_score(winner):
    score[winner] += 1



def print_score(function=print):
    computer_name = players_moves[COMPUTER_NAME]
    human_name = players_moves[HUMAN_NAME]
    head = '| ' + computer_name + ' | ' + human_name + ' |'
    s_border = '=' * len(head)
    numbers = '|' + str(score[computer_name]).center(len(computer_name) + 2)
    numbers += '|' + str(score[human_name]).center(len(human_name) + 2) + '|'
    lst = [s_border, head, numbers, s_border]
    s = '\n'.join(lst)
    s = shift_right(s, 6)
    function(s) 


def view_dimensions():
    view = []

    for dim in DIMENSIONS:
        dct = {cell: field[cell] for cell in dim}
        view.append(dct)

    return view


def shift_right(text, n=2):
    s = ''
    ls = text.splitlines(True)
    for line in ls:
        s += ' ' * n + str(line)
    return s


def border(fnc, display=print):
    def wrapper(nbr_spaces=SHIFT_FIELD):
        counter = get_moves_count()
        current_player = players_moves[CURRENT_PLAYER]
        current_move = players_moves[CURRENT_MOVE]

        if counter > 0:
            display(f"\n~~~Ход № {counter}, {current_player}:{current_move}~~~")
            fnc(nbr_spaces)
            display()
        else:
            clear_field()
            s = "\nВот как выглядит игровое поле. Сначала указываются ряды, потом - столбцы:"
            s += "Для ходя введите две цифры подрад, например 01. Чnобы выйти введите quit."
            display(s)
            display(output_moves())
            fnc(nbr_spaces)
            display()
    return wrapper


@border
def print_field(spaces, display=print):
    global EMPTY
    EMPTY = " "
    s = "\n    0    1    2\n\n"
    n = 0

    horiz_line = '\n    -----------\n'
    for i in range(3):
        s += str(n)
        t = '  '.join(field[(i, j)] + ' |' for j in range(3))[:-1]   # уберем 1 вертикальный разделитель
        s += '   ' + t + horiz_line
        n += 1
    s = s[:-len(horiz_line)-1]  # уберем 1 горизонтальный разделитель
    s = shift_right(s, spaces)
    display(s)


def legal_moves_str():
    return [str(t[0]) + str(t[1]) for t in get_legal_moves()]


def play_again_or_leave(display=print):
    human_name = players_moves[HUMAN_NAME]
    display("Сыграем еще? (Y/n)")
    reply = input(INP_INVITE).upper().strip()
    if reply in ('Y', ''):
        res = True
    elif reply == 'N' or "QUIT":
        res = False
    else:
        display(f'не понял ответа, {human_name}, но видимо, нет')
        res = False
    if res:
        display("Отлично, следующая игра!")
        # initialize_game()
        clear_field()
        players_moves[HUMAN_MARK], players_moves[COMPUTER_MARK] = players_moves[COMPUTER_MARK], players_moves[HUMAN_MARK]
        if players_moves[COMPUTER_MARK] == CROSS:
            display("теперь я за крестики")
            computer_move()
        else:
            human_move()
    else:
        display(f"Ну ладно, пока, {human_name}!")
        exit(0)


def action_draw(display=print):

    display(f"{players_moves[HUMAN_NAME]}, похоже, у нас ничья!")
    print_score()
    play_again_or_leave()


def human_move(display=print):
    human_mark = players_moves[HUMAN_MARK]
    human_name = players_moves[HUMAN_NAME]

    d = {NOUGHT: 'за нолики', CROSS: 'за крестики'}
    players_moves[CURRENT_PLAYER] = players_moves[HUMAN_NAME]
    if len(get_legal_moves()) == 0:  # если ходов больше нет
        action_draw()
    else:
        display(f"Ваш ход {d[human_mark]} (первая цифра ряд, вторая - столбец):")
        while True:
            mv = input(INP_INVITE)
            if mv.upper().strip() == QUIT:
                display(f"Ну ладно, пока, {human_name}!")
                print_score()
                exit()
            if mv in legal_moves_str():
                mv = (int(mv[0]), int(mv[1]))
                players_moves[CURRENT_MOVE] = mv
                field[mv] = human_mark
                print_field(10)
                break
            else:
                s = '[%s]' % ', '.join(map(str, legal_moves_str()))
                s = s[1:-1]
                display(f'Такого хода ({mv}) нет, попробуйте еще раз:', s)
                continue
        win_or_continue(human_name)


# (https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8)
def computer_move(display=print):
    mv = ()
    computer_name = players_moves[COMPUTER_NAME]
    computer_mark = players_moves[COMPUTER_MARK]

    players_moves[CURRENT_PLAYER] = players_moves[COMPUTER_NAME]
    if len(get_legal_moves()) == 0:
        action_draw()
    elif players_moves[COMPUTER_MARK] == CROSS:
        mv = crosses_strategy()
    else:
        mv = noughts_strategy()
    players_moves[CURRENT_MOVE] = mv
    field[mv] = computer_mark
    print_field()
    display(output_moves())
    win_or_continue(computer_name)


def check_danger(mark, msg, display=print):
    vw = view_dimensions()

    for dim in vw:
        keys = list(dim.keys())
        values = list(dim.values())

        if values.count(mark) == 2 and values.count(EMPTY) == 1:
            mv = keys[values.index(EMPTY)]
            display(msg)
            return mv


def attack():
    mark = players_moves[COMPUTER_MARK]
    vw = view_dimensions()

    for dim in vw:
        keys = list(dim.keys())
        values = list(dim.values())
        if values.count(EMPTY) == 2 and values.count(mark) == 1:
            # print(lst, dim, lst.index(EMPTY))
            mv = keys[values.index(EMPTY)][0]
            print("*Attacking!*", mv)
            # print(mv)
            return mv


def random_move(dislpay=print):
    dislpay('*random move!*')
    return choice(get_legal_moves())


def get_fartherst_corner(corners, prev_mv, display=print):
# реализация части стратегии из Вики:
# https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8
# Остальные ходы, если неприменимы правила 1—2, делаются в тот из свободных углов,
# который дальше всего от предыдущего хода ноликов
    if not corners:
        return False
    else:
        dist, mv = 0, corners[0]
        for corner in corners:
            # print(mv, corner)
            dist = abs(complex(*mv) - complex(*prev_mv))
            # print(dist)
            if abs(complex(*corner) - complex(*prev_mv)) > dist:
                mv = corner

            else:
                continue
        display("*Ход в дальний угол*")
        return mv


def crosses_strategy(display=print):

    free_corners = list(set(get_legal_moves()) & set(CORNERS))   # находим свободные углы

    # Первый ход сделать в центр. Остальные ходы, если неприменимы правила 1—2, делаются в тот из свободных углов,
    # который дальше всего от предыдущего хода ноликов, а если и это невозможно — в любую клетку.
    # https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8

    if get_moves_count() == 0:   # первый ход - в центр
        display("*За крестики: первый ход сделать в центр*")
        mv = (1, 1)
    else:
        mv = check_danger(CROSS, RULE_1) or check_danger(NOUGHT, RULE_2) or \
             get_fartherst_corner(free_corners, players_moves[CURRENT_MOVE]) or random_move()
    return mv


def noughts_strategy(display=print):

    # Если крестики сделали первый ход в центр, до конца игры ходить в любой угол,
    # а если это невозможно — в любую клетку.
    # Если крестики сделали первый ход в угол, ответить ходом в центр.

    if get_moves_count() == 1 and players_moves[CURRENT_MOVE] in SIDES:
        display('?first move on a side? Uhm...')
        mv = (1, 1)
    else:
        mv = check_danger(NOUGHT, RULE_1) or check_danger(CROSS, RULE_2) or try_best_moves() or random_move()

    return mv


def try_best_moves(display=print):
    best_moves = [(0, 0), (0, 2), (2, 0), (2, 2)]
    shuffle(best_moves)
    best_moves = [(1, 1)] + best_moves
    for mv in best_moves:
        # print(mv)
        if mv in get_legal_moves():
            display("*one of the best moves!*")
            return mv
        else:
            continue


def win_or_continue(player, display=print):
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
        display(f'*winning move: {players_moves[CURRENT_MOVE]}*')
        display(msg)
        update_score(player)
        print_score()
        play_again_or_leave()
    else:
        who_moves()


def is_win(mark, display=print):

    for dim in DIMENSIONS:
        res = all(field[cell] == mark for cell in dim)
        if res:
            display(f'Победу одержал: {players_moves[CURRENT_PLAYER]} ходом {players_moves[CURRENT_MOVE]}')
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


def initialize_game(display=print):
    global players_moves

    computer_name = players_moves[COMPUTER_NAME]
    human_name = players_moves[HUMAN_NAME]

    display(f"Для начала определим, кто первый ходит, {computer_name} или "
          f"{human_name}. Первый будет ходить крестиками.")
    display('орел? (1) или решка? (2)')
    clear_field()
    s = input(INP_INVITE).upper().strip()

    if s == QUIT:
        display("ну ладно, пока!")
        exit()
    if s in HEADS_TALES:
        t = choice(HEADS_TALES)
        if s.upper() == t:
            players_moves[HUMAN_MARK] = CROSS
            players_moves[COMPUTER_MARK] = NOUGHT
            players_moves[CURRENT_PLAYER] = human_name
            display(f"Угадали, {human_name} - ходите первым за крестики!")
            display(output_moves())
            human_move()
        else:
            players_moves[HUMAN_MARK] = NOUGHT
            players_moves[COMPUTER_MARK] = CROSS
            players_moves[CURRENT_PLAYER] = players_moves[COMPUTER_NAME]
            display(f"Не повезло, {human_name} - я хожу первым за крестики!")
            computer_move()
    else:
        display("Cтранный выбор, ну ладно, тогда мой ход.")
        players_moves[HUMAN_MARK] = NOUGHT
        players_moves[COMPUTER_MARK] = CROSS
        computer_move()


def greeting(display=print):
    # function("Ваше имя?")
    # players_moves[HUMAN_NAME] = input(INP_INVITE).capitalize()
    name = str(os.getlogin()).capitalize()
    players_moves[HUMAN_NAME] = name
    display(players_moves[HUMAN_NAME] )
    display(f"Привет, {players_moves[HUMAN_NAME]}!")
    create_score(players_moves[HUMAN_NAME])
    print_score()



def start_game():
    greeting()
    print_field()
    initialize_game()


start_game()

