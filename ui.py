from typing import Protocol
from utils import shift_right


class UI(Protocol):
    def display_score(self):
        raise NotImplemented

    def display_field(self):
        raise NotImplemented

    def display_message(self):
        raise NotImplemented

    def get_player_input(self):
        raise NotImplemented

    def get_player_name(self):
        raise NotImplemented

    def get_computer_name(self):
        raise NotImplemented

    def get_user_input(self):
        raise NotImplemented
