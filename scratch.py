from random import choice



computer_name = "Компьтер"
EMPTY = '-'
CROSS = 'X'
NOUGHT = 'O'
human_name = "Навуходоносор"
machines_move = False
counter = 0
current_player = ""
HEADS_TALES = ('1', '2')
INP_INVITE = "?--> "

tally = {human_name: 0, computer_name: 0}
field = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

ROW_0 = [(0, 0), (0, 1), (0, 2)]
ROW_1 = [(1, 0), (1, 1), (1, 2)]
ROW_2 = [(2, 0), (2, 1), (2, 2)]
COL_0 = [(0, 0), (1, 0), (2, 0)]
COL_1 = [(0, 1), (1, 1), (2, 1)]
COL_2 = [(0, 2), (1, 2), (2, 2)]
DIAG_0 = [(0, 0), (1, 1), (2, 2)]
DIAG_1 = [(0, 2), (1, 1), (2, 0)]

DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]

BEST_MOVES = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]


legal_moves = [ (0, 1),
               (1, 0), (1, 2),
                (2, 1)
               ]

def legal_moves_str():
    global legal_moves
    lst = [str(t[0]) + str(t[1]) for t in legal_moves]
    return lst

def try_best_moves():
    for mv in BEST_MOVES:
        # print(mv)
        if mv in legal_moves:
            return mv
        else:
            continue


def output_moves():
    # s = '[%s]' % ', '.join(map(str, legal_moves_str()))
    s = ', '.join(legal_moves_str())
    s = "Возможные ходы: " + (s or "ходов больше нет.")
    return s


def no_more_moves():
    res = len(legal_moves) == 0
    return res


def trim_input():
    inp = input(INP_INVITE)
    t = ()
    print('legal_moves_str():', legal_moves_str())
    print(f'inp {inp} in legal_moves_str():', inp in legal_moves_str())
    if inp in legal_moves_str():
        "hi inp in legal_moves_str()"
        t = (int(inp[0]), int(inp[1]))
        print("t:", t)
        return t
    else:
        s = '[%s]' % ', '.join(map(str, legal_moves_str()))
        s = s[1:-1]
        print(f'Такого хода ({inp}) нет, попробуйте еще раз:', s)
        trim_input()

def is_win(mark=CROSS):
    global field
    for dim in DIMENSIONS:

        res = all(field[cell[0]][cell[1]] == mark for cell in dim)
        if res:
            # print(res)
            print('Победу одержал:', current_player, mark)
            return True


def check_danger(mark=CROSS):

    for dim in DIMENSIONS:
        i = where_attack([field[cell[0]][cell[1]] for cell in dim], mark)
        if i is None:
            pass
        else:
            return dim[i]
#    return False


def attack():
    return check_danger(NOUGHT)


def where_attack(triad, mark):
    bool = triad.count(EMPTY) == 1
    if not bool:
        return None
    else:
        i = triad.index(EMPTY)
        triad.pop(i)
        if triad[0] == triad[1] == mark:
            return i
        else:
            return None


def print_field():
    global counter
    global current_player
    s = "   "
    n = 0
    print("      0  1  2")
    for i in range(3):
        # print(list(field[i][j] for j in range(3)))
        s += str(n)
        for j in range(3):
            s = s + '  ' + field[i][j]
        s += '\n   '
        n += 1
    print(s)
    counter += 1


def win_or_continue(player, mark):
    global human_name
    global computer_name
    global CROSS
    if player == human_name:
        msg = f'Congrats, you win, human", {human_name}'
        who_moves = move_player
    elif player == computer_name:
        msg = f"I win, human {human_name}! ;-)"
        who_moves = move_machine
    else:
        msg = "there's something wrong with this program!"

    if is_win(mark):
        print(f'*winning move: {current_move}*')
        print(msg)
        update_tally(computer_name)
        print_tally()
        play_again_or_leave()
    else:
        who_moves()


def move_player(mark=CROSS):
    # global machines_move = False
    if no_more_moves():
        print(f"{human_name}, похоже, у нас ничья!")
    else:
        global current_player
        current_player = human_name
        print('Ваш ход (первая цифра ряд, вторая - столбец):')
        while True:
            mv = input(INP_INVITE)
            if mv in legal_moves_str():
                mv = (int(mv[0]), int(mv[1]))
                print("mv:", mv)
                field[mv[0]][mv[1]] = mark
                legal_moves.remove(mv)
                print_field()
                break
            else:
                s = '[%s]' % ', '.join(map(str, legal_moves_str()))
                s = s[1:-1]
                print(f'Такого хода ({mv}) нет, попробуйте еще раз:', s)
                continue
        # if is_win():
        #     print("Congrats, you win, human", human_name)
        # else:
        #     move_machine()

def attack():
    return check_danger(NOUGHT)


def check_danger(mark=CROSS):
    #    bool = False
    for dim in DIMENSIONS:
        i = where_attack([field[cell[0]][cell[1]] for cell in dim], mark)
        if i is None:
            pass
        else:
            print('Danger! I\'m defending!')
            return dim[i]
    return False


def random_move(mark=NOUGHT):
    global legal_moves
    print('random move!')
    print(legal_moves)
    return choice(legal_moves)


def move_machine(mark=NOUGHT):
    if no_more_moves():
        print(f"{human_name} - похоже, ничья!")
    else:
        global current_player
        current_player = "компьютер"
        mv = attack() or check_danger() or random_move()
        print("mv:", mv)
        field[mv[0]][mv[1]] = mark
        legal_moves.remove(mv)
        #        print('hi from move_player, legal_moves: ', str(legal_moves))
        print_field()
        print(output_moves())
        if is_win(NOUGHT):
            print(f"I win, human {human_name}! ;-)")
        else:
            move_player()

def initialize_game():
    global HEADS_TALES
    print(f"Для начала определим, кто первый ходит, компьютер или {human_name}. Чур, я играю за нолики!")
    print('орел (1) или решка (2)')
    s = input(INP_INVITE)
    if s not in HEADS_TALES:
        print("странный выбор, ну ладно, тогда мой ход.")
        # move_machine()
    else:
        t = choice(HEADS_TALES)
        if s.upper() == t:
            print("Ваш ход")
            print(output_moves())
            # move_player()
        else:
            print("Мой ход")
            # move_machine()


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
        print("отлично, следующая игра!")
        # initialize_game()
    else:
        print(f"Ну ладно, пока, {human_name}!")

# print_field()


a = ['x', 'x', EMPTY]
b = [EMPTY, EMPTY, 'x']
c = ['x', 'y', 'x']

# print(where_attack(a, 'x'))
# print(where_attack(b, 'x'))
# print(where_attack(c, 'x'))

#print(check_danger(CROSS))
#print(attack())


#move_player()
# print(legal_moves)
# print(output_moves())
# move_player()
# #mv = trim_input()
# #print(str(mv))
# print(legal_moves)
# print_field()
# move_machine()

# initialize_game()

# play_again_or_leave()

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
    print(border)
    print(head)
    print(border)
    print(numbers)
    print(border)


    # print("счет:\n", tally)


EMPTY = 'EMPTY'
# print(try_best_moves())
# name = human_name.capitalize()
# create_tally(name)
# update_tally(name)
# print_tally()
# update_tally(name)
# print_tally()
# update_tally(computer_name)
# print_tally()
EMPTY = 'EMPTY'
# print_field()
# print_empty()
s = ""
for i in range(3):
    for j in range(3):
        s += f'({i}, {j}): {EMPTY}, '
    s += '\n'
print(s)


# for i in range(k, m):
#     # print(list(field[i][j] for j in range(3)))
#     s += '       ' + str(str(n) + '|').rjust(3)
#     for j in range(k, m):
#         # s += '  ' + str(i * j).rjust(3)
#         s += f'({k}, {j}): EMPTY, '
#     s += '\n'
#     n += 1
# # s = '  ' + s
# print(s)