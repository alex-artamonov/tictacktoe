from ui import UI
import utils as u


class Cli(UI):
    def __init__(self, computer_name, player_name, score) -> None:
        self.computer_name = computer_name
        self.player_name = player_name
        self.score = score
        print(computer_name, player_name)

    def display_score(self):
        shift_nbr = 6        
        head = '| ' + self.computer_name + ' | ' + self.player_name + ' |'
        s_border = '=' * len(head)
        numbers = '|' + str(self.score[self.computer_name]).center(len(self.computer_name) + 2)
        numbers += '|' + str(self.score[self.player_name]).center(len(self.player_name) + 2) + '|'
        lst = [s_border, head, numbers, s_border]
        output = '\n'.join(lst)
        output = u.shift_right(output, shift_nbr)
        print(output) 
        

    def display_field(self, field: dict, spaces: int, counter: str, 
                      current_player: str, current_move: int):
        # global EMPTY ??????????????
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
        print(f"\n~~~Ход № {counter}, {current_player}:{current_move}~~~")
        s = u.shift_right(s, spaces)
        print(s)