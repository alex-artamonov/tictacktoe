from random import choice

human_name = "Human"
machines_move = False
counter = 0
current_player = ""
HEADS_TALES = ('1', '2')
INP_INVITE = "?--> "
EMPTY = '-'
CROSS = 'X'
NOUGHT = 'O'
field = {'00': EMPTY, '01': EMPTY, '02': EMPTY,
         '10': EMPTY, '11': EMPTY, '12': EMPTY,
         '20': EMPTY, '21': EMPTY, '22': EMPTY
         }
legal_moves = ['00', '01', '02',
               '10', '11', '12',
               '20', '21', '22'
               ]
# legal_moves = ['00', '01']

ROW_0 = ['00', '01', '02']
ROW_1 = ['10', '11', '12']
ROW_2 = ['20', '21', '22']
COL_0 = ['00', '10', '20']
COL_1 = ['01', '11', '21']
COL_2 = ['02', '12', '22']
DIAG_0 = ['00', '11', '22']
DIAG_1 = ['02', '11', '20']

DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]

is_machine = False


def legal_moves_str():
    global legal_moves
    lst = [str(t[0]) + str(t[1]) for t in legal_moves]
    return lst


def clear_field():
    global field
    field = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]


def output_moves():
    s = '[%s]' % ', '.join(map(str, legal_moves))
    s = "Возможные ходы: " + (s[1:-1] or "ходов больше нет.")
    return s


def shift_right(text, n=2):
    ls = text.split('\n')
    for line in ls:
        print(' ' * n + str(line))


def border(fnc):
    def wrapper():
        global counter
        if counter > 0:
            print(f"\n~~~~~~~Ход № {counter}, {current_player}~~~~~~")
            fnc()
        else:
            print(f"\nВот как выглядит игровое поле. Сначала указываются ряды, потом - столбцы:")
            print(output_moves())
            fnc()

    return wrapper


@border
def print_field():
    global counter
    global current_player
    lst = list(field.values())
    print("  0 1 2")
    print('0', lst[0], lst[1], lst[2])
    print('1', lst[3], lst[4], lst[5])
    print('2', lst[6], lst[7], lst[8])
    print()
    counter += 1


def no_more_moves():
    res = len(legal_moves) == 0
    return res

def is_draw_next_move():
    mvs_look_ahead = legal_moves.copy()
    fld_look_ahead = field.copy()
    mark = CROSS #заменить на players_moves[HUMAN_MARK]
    if len(mvs_look_ahead) == 1:
        for dim in DIMENSIONS:
            res = all(fld_look_ahead[cell] == mark for cell in dim)
            if res:
                return field[0]



def play_again_or_leave():
    print("Сыграем еще? (Y/n)")
    reply = input(INP_INVITE).upper()
    if reply == ('Y' or ''):
        res = True
    elif reply == 'N':
        res = False
    else:
        print(f'не понял ответа, {human_name}, но видимо, нет')
        res = False
    if res:
        print("отлично, следующая игра!"
        initialize_game()
    else:
        print(f"Ну ладно, пока, {human_name}!")




def move_player(mark=CROSS):
    # global machines_move = False
    if no_more_moves():
        print(f"{human_name}, похоже, у нас ничья!")
    else:
        global current_player
        current_player = human_name
        print('Ваш ход (первая цифра ряд, вторая - столбец):')
        mv = input(INP_INVITE)
        if mv in legal_moves:
            field[mv] = mark
            legal_moves.remove(mv)
        #            print('hi from move_player, legal_moves:', str(legal_moves))
        else:
            s = s = ', '.join(legal_moves_str())
            print('Такого хода нет, попробуйте еще раз:', s)
            move_player()
        print_field()
        if is_win():
            print("Congrats, you win, human", human_name)
        else:
            move_machine()


def random_move(mark=NOUGHT):
    global legal_moves
    print('random move!')
    return choice(legal_moves)


def move_machine(mark=NOUGHT):
    if no_more_moves():
        print(f"{human_name} - похоже, ничья!")
    else:
        global current_player
        current_player = "компьютер"
        mv = attack() or check_danger() or random_move()
        field[mv] = mark
        legal_moves.remove(mv)
        #        print('hi from move_player, legal_moves: ', str(legal_moves))
        print_field()
        print(output_moves())
        if is_win(NOUGHT):
            print(f"I win, human {human_name}! ;-)")
            if play_again():
                initialize_game()
            else:
                print(f"Ладно, пока, {human_name}"))
        else:
            move_player()


def is_win(mark=CROSS):
    global field
    for dim in DIMENSIONS:

        res = all(field[cell] == mark for cell in dim)
        if res:
            # print(res)
            print('Победу одержал:', current_player, mark)
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


def attack():
    return check_danger(NOUGHT)


def check_danger(mark=CROSS):
    #    bool = False
    for dim in DIMENSIONS:
        i = where_attack([field[cell] for cell in dim], mark)
        if i is None:
            pass
        else:
            print('Danger! I\'m defending!')
            return dim[i]
    return False


def initialize_game():
    global HEADS_TALES
    clear_field()
    print(f"Для начала определим, кто первый ходит, компьютер или {human_name}. Чур, я играю за нолики!")
    print('орел (1) или решка (2)')
    s = input(INP_INVITE)
    if s in HEADS_TALES:
        t = choice(HEADS_TALES)
        if s.upper() == t:
            print("Ваш ход")
            print(output_moves())
            move_player()
        else:
            print("Мой ход")
            move_machine()
    else:
        print("Cтранный выбор, ну ладно, тогда мой ход.")
        move_machine()


def greeting():
    global human_name
    print("Ваше имя?")
    human_name = input(INP_INVITE).capitalize()
    print(f"Привет, {human_name}!")


greeting()
print_field()
# print("random move:", choice(legal_moves))
# move_player()
initialize_game()

# print(DIMENSIONS[2])
