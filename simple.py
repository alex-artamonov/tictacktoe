class Simple:
    def display_score(self, score):
        print(score)

    def display_field(
        self,
        field: dict,
        counter: str,
        current_player: str,
        current_move: int,
    ):
        print(f"{counter=}, {current_player=}, {current_move=}")
        print(field)

    # def display_border(self):
    #     raise NotImplemented

    def clear_field(self):
        print("field cleared ")

    def display_moves(self, moves):
        print(moves)

    def display_message(self, text):
        print(text)

    def get_player_input(self, request="Eh?\t"):
        return input(request)

    def get_player_name(self):
        return input("your name?\t")

    def get_computer_name(self):
        return "computer"

    def get_user_input(self, request="request?"):
        return input(request)
