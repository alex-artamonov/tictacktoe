EMPTY = ' '
CROSS = 'X'
NOUGHT = 'O'


field = {(0, 0): CROSS, (0, 1): NOUGHT, (0, 2): EMPTY,
         (1, 0): CROSS, (1, 1): EMPTY, (1, 2): NOUGHT,
         (2, 0): NOUGHT, (2, 1): NOUGHT, (2, 2): CROSS}




ROW_0 = {(0, 0), (0, 1), (0, 2)}
ROW_1 = {(1, 0), (1, 1), (1, 2)}
ROW_2 = {(2, 0), (2, 1), (2, 2)}
COL_0 = {(0, 0), (1, 0), (2, 0)}
COL_1 = {(0, 1), (1, 1), (2, 1)}
COL_2 = {(0, 2), (1, 2), (2, 2)}
DIAG_0 = {(0, 0), (1, 1), (2, 2)}
DIAG_1 = {(0, 2), (1, 1), (2, 0)}

DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]






def view_dimensions():
    view = []

    for dim in DIMENSIONS:
        dct = {cell: field[cell] for cell in dim}
    #     dct = {cell: field[cell] for cell in field}
    # view.append(dct)
    #     for cell in dim:
            # dct = {cell: field[cell] for cell in field}

        view.append(dct)
        # print(dim)
    # [print(d) for d in view]
    return view
#
# print(len(view_dimensions()))
[print(dim) for dim in view_dimensions()]


# a = {'a':10, 'b': 20, 'c': 30, 'd': 40}
# b = ['a', 'b', 'c']
#
# view_dims = []

# for dim in DIMENSIONS:
#     d = {i: field[i] for i, j in zip(dim, field)}
#     # for i, j in zip(dim, field):
#     #     d[i] = field[i]
#         # print(j, field[j])
#     view_dims.append(d)
# # [print(dim) for dim in view_dims]
# [print(d) for d in view_dims]

def print_field():
    s = "\n    0   1   2\n\n"
    n = 0
    horiz_line = '\n    ---------\n'
    for i in range(3):
        # print(list(field[i][j] for j in range(3)))
        s += str(n)
        t = ' '.join(field[(i,j)] + ' |' for j in range(3))[:-1] # уберем 1 вертикальный разделитель
            # print(s)
        s += '   ' + t + horiz_line
        n += 1
    s = s[:-len(horiz_line)-1]  # уберем 1 горизонтальный разделитель
    print(s)

# print_field()

# d = {NOUGHT:'за нолики', CROSS: 'за крестики'}
# s = d[NOUGHT]
# print(s)