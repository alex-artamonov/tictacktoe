from ui import UI
import utils as u
import os


INP_INVITE = "?--> "

class Cli(UI):
    def __init__(self, computer_name="Компьютер") -> None:
        self.computer_name = computer_name
        self.player_name = self.get_player_name()
        print(computer_name, self.player_name)

    def display_message(self, text: str):
        print(text)

    def display_score(self, score):
        shift_nbr = 6
        head = "| " + self.computer_name + " | " + self.player_name + " |"
        s_border = "=" * len(head)
        numbers = "|" + str(score[self.computer_name]).center(
            len(self.computer_name) + 2
        )
        numbers += (
            "|"
            + str(score[self.player_name]).center(len(self.player_name) + 2)
            + "|"
        )
        lst = [s_border, head, numbers, s_border]
        output = "\n".join(lst)
        output = u.shift_right(output, shift_nbr)
        print(output)

    def display_field(
        self,
        field: dict,
        counter: str,
        current_player: str,
        current_move: int,
        
    ):

        spaces: int = 10
        s = "\n    0    1    2\n\n"
        n = 0
        horiz_line = "\n    -----------\n"
        for i in range(3):
            s += str(n)
            t = "  ".join(field[(i, j)] + " |" for j in range(3))[
                :-1
            ]  # уберем 1 вертикальный разделитель
            s += "   " + t + horiz_line
            n += 1
        s = s[: -len(horiz_line) - 1]  # уберем 1 горизонтальный разделитель
        print(f"\n~~~Ход № {counter}, {current_player}:{current_move}~~~")
        s = u.shift_right(s, spaces)
        print(s)
        print()

    def get_player_input(self, request: str = INP_INVITE):
        reply = input(f"{request}\t").strip()
        return reply
    
    def get_computer_name(self):
        return self.computer_name
    
    def get_player_name(self):
        return str(os.getlogin()).capitalize()
    