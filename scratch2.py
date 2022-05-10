from random import choice
from random import shuffle

BEST_MOVES = [(1, 1)]
k, m = 0, 3

n = 2
s = ''
t = list(str(d).rjust(3) for d in range(k, m))
# print('   ', *t)

for i in range(k, m):
    # print(list(field[i][j] for j in range(3)))
    s += '       ' + str(str(n) + '|').rjust(3)
    for j in range(k, m):
        # s += '  ' + str(i * j).rjust(3)
        s += f'({k}, {j}): EMPTY, '
    s += '\n'
    n += 1
# s = '  ' + s
print(s)

def tst():

    while True:
        st = input("enter letter:\n> ")
        if st == 'a':
            return "Win"
        else:
            print("try again")
            continue

# print(tst())

more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]


legal_moves = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2)
               ]

# s = "asdf"


def legal_moves_str():
    global legal_moves
    lst = [str(t[0]) + str(t[1]) for t in legal_moves]
    return lst



# print(s)

# print(str(more_stuff))
# print(more_stuff)
# s = ", ".join(legal_moves_str())
# print(s)
#
# print(legal_moves_str())


def shift_right(text, n=2):
    s = ''
    ls = text.splitlines(True)
    for line in ls:
        s += ' ' * n + str(line) #+ '\n'
    return s




# print(shift_right(s, 4))

def action1(msg):
    print("action1:", msg)

def action2(msg):
    print("action2:", msg)


# act = action2
# act("asdf")
t = choice([range(12, 24)])
# t = [range(2, 50)]
# print(t, type(t))
# lst = [1, 3, t]
# print(lst)

s = "a\nb\nc\n"
# print(s, len(s))
# print('asdf')
#
# s.replace('/n', '', -1)
# print(s, len(s))
# print('asdf')

# lst = [(0, 0), (0, 2), (2, 0), (2, 2)]
# shuffle(lst)
# BEST_MOVES += lst
# print(BEST_MOVES)

# s = '''
# ====================
# | Компьтер | Asdfs |
# |    1     |   0   |
# ====================
# '''

s = '''
    If you know what HTML is, then this should look fairly familiar. If not,
research HTML and try writing a few web pages by hand so you know how it
works. This HTML file, however, is a template, which means that flask will
fill in “holes” in the text depending on variables you pass in to the template.
Every place you see $greeting will be a variable you’ll pass to the template
that alters its contents.
'''

# s = shift_right(s, 10)
# S = ''
# print(s)

T = 'asdfds'

# def test_global():
#     global T
#     T = "some string"
#
# def print_s():
#     # global T
#     test_global()
#     print(T)

# print_s()


