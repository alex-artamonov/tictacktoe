from random import choice, shuffle
import ui

RULE_1 = "*Первое правило крестиков-ноликов: если есть возможность - то делать выигрышный ход*"
RULE_2 = "*Второе правило  крестиков-ноликов: предотвратить немедленный проигрыш*"

QUIT = ("q", "Q", "QUIT")
HUMAN_NAME = "human_name"
HUMAN_MARK = "human_mark"
COMPUTER_MARK = "computer_mark"
COMPUTER_NAME = "computer_name"
CURRENT_PLAYER = "current_player"
CURRENT_MOVE = "current_move"
SHIFT_FIELD = 10
HEADS_TALES = ("1", "2")
EMPTY = " "
CROSS = "X"
NOUGHT = "O"


class Gameplay:
    _players_moves = {
        HUMAN_NAME: "",
        HUMAN_MARK: "",
        COMPUTER_NAME: "Компьютер",
        COMPUTER_MARK: "",
        CURRENT_PLAYER: "",
        CURRENT_MOVE: (),
    }
    field = {
        (0, 0): EMPTY,
        (0, 1): EMPTY,
        (0, 2): EMPTY,
        (1, 0): EMPTY,
        (1, 1): EMPTY,
        (1, 2): EMPTY,
        (2, 0): EMPTY,
        (2, 1): EMPTY,
        (2, 2): EMPTY,
    }

    ROW_0 = [(0, y) for y in range(3)]
    ROW_1 = [(1, y) for y in range(3)]
    ROW_2 = [(2, y) for y in range(3)]
    COL_0 = [(x, 0) for x in range(3)]
    COL_1 = [(x, 1) for x in range(3)]
    COL_2 = [(x, 2) for x in range(3)]
    DIAG_0 = [(x, x) for x in range(3)]
    DIAG_1 = [(0, 2), (1, 1), (2, 0)]
    CORNERS = [(0, 0), (0, 2), (2, 2), (2, 0)]
    SIDES = [(0, 1), (1, 2), (2, 1), (1, 0)]

    DIMENSIONS = [ROW_0, ROW_1, ROW_2, COL_0, COL_1, COL_2, DIAG_0, DIAG_1]
    # previous_human_move = ()
    score = {}

    def __init__(self, ui: ui.UI):
        self.player_name = ui.get_player_name()
        self.computer_name = ui.get_computer_name()
        self.ui = ui

    def get_moves_count(self):
        lst = list(self.field.values())
        return len(lst) - lst.count(EMPTY)

    def get_legal_moves(self):
        return [key for (key, value) in self.field.items() if value == EMPTY]

    def clear_field(self):
        for cell in self.field:
            self.field[cell] = EMPTY

    @property
    def current_player(self):
        return self._players_moves[CURRENT_PLAYER]

    @current_player.setter
    def current_player(self, value):
        self._players_moves[CURRENT_PLAYER] = value

    @property
    def computer_name(self):
        return self._players_moves[COMPUTER_NAME]

    @computer_name.setter
    def computer_name(self, value):
        self._players_moves[COMPUTER_NAME] = value

    @property
    def player_name(self):
        return self._players_moves[HUMAN_NAME]

    @player_name.setter
    def player_name(self, value):
        self._players_moves[HUMAN_NAME] = value

    @property
    def current_move(self):
        return self._players_moves[CURRENT_MOVE]

    @current_move.setter
    def current_move(self, value):
        self._players_moves[CURRENT_MOVE] = value

    def get_legal_moves_str(self):
        # s = '[%s]' % ', '.join(map(str, legal_moves_str()))
        output = ", ".join(self.legal_moves_str())
        output = f"Возможные ходы: {(output or 'ходов больше нет.')}"
        return output

    def create_score(self, human_name):
        computer_name = self.computer_name
        self.player_name = human_name
        self.score[human_name], self.score[computer_name] = 0, 0

    def update_score(self, winner):
        self.score[winner] += 1

    def view_dimensions(self):
        view = []
        for dim in self.DIMENSIONS:
            dct = {cell: self.field[cell] for cell in dim}
            view.append(dct)
        return view

    def legal_moves_str(self):
        return [str(t[0]) + str(t[1]) for t in self.get_legal_moves()]

    def play_again_or_leave(self):
        self.display_message("Сыграем еще? (Y/n)")
        reply = self.get_player_input().upper()
        if reply in ("Y", ""):
            res = True
        elif reply == "N" or reply in [QUIT]:
            res = False
        else:
            self.display_message(f"не понял ответа, {self.player_name}, но видимо, нет")
            res = False
        if res:
            self.display_message("Отлично, следующая игра!")
            # initialize_game()
            self.clear_field()
            self._players_moves[HUMAN_MARK], self._players_moves[COMPUTER_MARK] = (
                self._players_moves[COMPUTER_MARK],
                self._players_moves[HUMAN_MARK],
            )
            if self._players_moves[COMPUTER_MARK] == CROSS:
                self.display_message("теперь я за крестики")
                self.computer_move()
            else:
                self.human_move()
        else:
            self.display_message(f"Ну ладно, пока, {self.player_name}!")
            exit(0)

    def action_draw(self):
        global ui
        self.display_message(f"{self.player_name}, похоже, у нас ничья!")
        self.display_score()
        self.play_again_or_leave()

    def human_move(self):
        human_mark = self._players_moves[HUMAN_MARK]
        human_name = self._players_moves[HUMAN_NAME]

        d = {NOUGHT: "за нолики", CROSS: "за крестики"}
        self.current_player = self.player_name
        if len(self.get_legal_moves()) == 0:  # если ходов больше нет
            self.action_draw()
        else:
            self.display_message(f"Ваш ход {d[human_mark]} (первая цифра ряд, вторая - столбец):")
            while True:
                mv = self.get_player_input()
                if mv.upper() in QUIT:
                    self.display_message(f"Ну ладно, пока, {human_name}!")
                    self.display_score()
                    exit()
                if mv in self.legal_moves_str():
                    mv = (int(mv[0]), int(mv[1]))
                    self.current_move = mv
                    self.field[mv] = human_mark
                    self.display_field(self.get_moves_count(), self.current_player, self.current_move)
                    break
                else:
                    s = "[%s]" % ", ".join(map(str, self.legal_moves_str()))
                    s = s[1:-1]
                    self.display_message(f"Такого хода ({mv}) нет, попробуйте еще раз: {s}")
                    continue
            self.win_or_continue(human_name)

    # (https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8)
    def computer_move(self):
        mv = ()
        computer_name = self._players_moves[COMPUTER_NAME]
        computer_mark = self._players_moves[COMPUTER_MARK]

        self.current_player = self.computer_name
        if len(self.get_legal_moves()) == 0:
            self.action_draw()
        elif self._players_moves[COMPUTER_MARK] == CROSS:
            mv = self.crosses_strategy()
        else:
            mv = self.noughts_strategy()
        self.current_move = mv
        self.field[mv] = computer_mark
        self.display_field(self.get_moves_count(), self.current_player, self.current_move)
        self.display_message(self.get_legal_moves_str())
        self.win_or_continue(computer_name)

    def check_danger(self, mark, msg):
        vw = self.view_dimensions()

        for dim in vw:
            keys = list(dim.keys())
            values = list(dim.values())

            if values.count(mark) == 2 and values.count(EMPTY) == 1:
                mv = keys[values.index(EMPTY)]
                self.display_message(msg)
                return mv

    def attack(self):
        mark = self._players_moves[COMPUTER_MARK]
        vw = self.view_dimensions()

        for dim in vw:
            keys = list(dim.keys())
            values = list(dim.values())
            if values.count(EMPTY) == 2 and values.count(mark) == 1:
                mv = keys[values.index(EMPTY)][0]
                self.display_message("*Attacking!*", mv)
                return mv

    def random_move(self):
        self.display_message("*random move!*")
        return choice(self.get_legal_moves())

    def get_fartherst_corner(self, corners, prev_mv):
        # реализация части стратегии из Вики:
        # https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8
        # Остальные ходы, если неприменимы правила 1—2, делаются в тот из свободных углов,
        # который дальше всего от предыдущего хода ноликов
        if not corners:
            return False
        else:
            dist, mv = 0, corners[0]
            for corner in corners:
                dist = abs(complex(*mv) - complex(*prev_mv))
                if abs(complex(*corner) - complex(*prev_mv)) > dist:
                    mv = corner

                else:
                    continue
            self.display_message("*Ход в дальний угол*")
            return mv

    def crosses_strategy(self):

        free_corners = list(
            set(self.get_legal_moves()) & set(self.CORNERS)
        )  # находим свободные углы

        # Первый ход сделать в центр. Остальные ходы, если неприменимы правила 1—2, делаются в тот из свободных углов,
        # который дальше всего от предыдущего хода ноликов, а если и это невозможно — в любую клетку.
        # https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8

        if self.get_moves_count() == 0:  # первый ход - в центр
            self.display_message("*За крестики: первый ход сделать в центр*")
            mv = (1, 1)
        else:
            mv = (
                self.check_danger(CROSS, RULE_1)
                or self.check_danger(NOUGHT, RULE_2)
                or self.get_fartherst_corner(free_corners, self.current_move)
                or self.random_move()
            )
        return mv

    def noughts_strategy(self):

        # Если крестики сделали первый ход в центр, до конца игры ходить в любой угол,
        # а если это невозможно — в любую клетку.
        # Если крестики сделали первый ход в угол, ответить ходом в центр.

        if self.get_moves_count() == 1 and self.current_move in self.SIDES:
            self.display_message("?first move on a side? Uhm...")
            mv = (1, 1)
        else:
            mv = (
                self.check_danger(NOUGHT, RULE_1)
                or self.check_danger(CROSS, RULE_2)
                or self.try_best_moves()
                or self.random_move()
            )

        return mv

    def try_best_moves(self):
        best_moves = [(0, 0), (0, 2), (2, 0), (2, 2)]
        shuffle(best_moves)
        best_moves = [(1, 1)] + best_moves
        for mv in best_moves:
            if mv in self.get_legal_moves():
                self.display_message("*one of the best moves!*")
                return mv
            else:
                continue

    def win_or_continue(self, player):
        human_name = self.player_name
        computer_name = self.computer_name
        human_mark = self._players_moves[HUMAN_MARK]
        computer_mark = self._players_moves[COMPUTER_MARK]
        mark = ""
        who_moves = None

        if player == human_name:
            msg = f'- Congrats, you win, human", {human_name}'
            who_moves = self.computer_move
            mark = human_mark
        elif player == computer_name:
            msg = f"- I win, human {human_name}! ;-)"
            who_moves = self.human_move
            mark = computer_mark
        else:
            msg = "there's something wrong with this program!"
        # global cli
        if self.is_win(mark):
            self.display_message(f"*winning move: {self.current_move}*")
            self.display_message(msg)
            self.update_score(player)
            self.display_score()
            self.play_again_or_leave()
        else:
            who_moves()

    def is_win(self, mark):

        for dim in self.DIMENSIONS:
            res = all(self.field[cell] == mark for cell in dim)
            if res:
                self.display_message(
                    f"Победу одержал: {self.current_player} ходом {self.current_move}"
                )
                return True

    def where_attack(self, triad, mark):
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

    def initialize_game(self):

        self.display_message(
            f"Для начала определим, кто первый ходит, {self.computer_name} или "
            f"{self.player_name}. Первый будет ходить крестиками."
        )
        self.display_message("орел? (1) или решка? (2)")
        self.clear_field()
        # s = input().upper().strip()
        s = self.get_player_input()

        if s == QUIT:
            self.display_message("ну ладно, пока!")
            exit()
        if s in HEADS_TALES:
            t = choice(HEADS_TALES)
            if s.upper() == t:
                self._players_moves[HUMAN_MARK] = CROSS
                self._players_moves[COMPUTER_MARK] = NOUGHT
                self.current_player = self.player_name
                self.display_message(f"Угадали, {self.player_name} - ходите первым за крестики!")
                self.display_message(self.get_legal_moves_str())
                self.human_move()
            else:
                self._players_moves[HUMAN_MARK] = NOUGHT
                self._players_moves[COMPUTER_MARK] = CROSS
                self.current_player = self.computer_name
                self.display_message(f"Не повезло, {self.player_name} - я хожу первым за крестики!")
                self.computer_move()
        else:
            self.display_message("Cтранный выбор, ну ладно, тогда мой ход.")
            self._players_moves[HUMAN_MARK] = NOUGHT
            self._players_moves[COMPUTER_MARK] = CROSS
            self.computer_move()

    def display_field(self, counter='<Номер хода>', player= '<чей ход>', move = '<ход>'):
        self.ui.display_field(self.field,
                         counter=counter,
                         current_player=player,
                         current_move=move)
        
    def display_score(self):
        self.ui.display_score(self.score)

    def display_message(self, text):
        self.ui.display_message(text)
        
    def get_player_input(self):
        return self.ui.get_player_input()

    def greeting(self):
        # global ui
        # ui = cli.Cli(self.computer_name, self.player_name, self.score)
        # self.player_name
        # self._players_moves[HUMAN_NAME] = player_name
        self.display_message(self.player_name)
        self.display_message(f"Привет, {self.player_name}!")
        self.create_score(self.player_name)
        
        self.display_score()
        s = "Вот как выглядит игровое поле. Сначала указываются ряды, потом - столбцы:"
        self.display_message(s)
        self.display_field()
        self.display_message(self.get_legal_moves_str())
        s = "Для хода введите две цифры подряд, например 01. Чтобы выйти введите quit."
        self.display_message(s)        
        
        # ui.display_field()
