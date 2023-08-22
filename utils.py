def shift_right(text, n=2):
    s = ""
    ls = text.splitlines(True)
    for line in ls:
        s += " " * n + str(line)
    return s


# @border
# def display_field(spaces, display=print):
#     global EMPTY
#     EMPTY = " "
#     s = "\n    0    1    2\n\n"
#     n = 0

#     horiz_line = '\n    -----------\n'
#     for i in range(3):
#         s += str(n)
#         t = '  '.join(field[(i, j)] + ' |' for j in range(3))[:-1]   # уберем 1 вертикальный разделитель
#         s += '   ' + t + horiz_line
#         n += 1
#     s = s[:-len(horiz_line)-1]  # уберем 1 горизонтальный разделитель
#     s = c.shift_right(s, spaces)
#     display(s)
