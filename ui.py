from typing import Protocol
from utils import shift_right


class UI(Protocol):
    def display_score(self, function=None):
        raise NotImplemented

    def display_field(self):
        raise NotImplemented

    def display_border(self):
        raise NotImplemented

    def clear_field(self):
        raise NotImplemented

    def display_moves(self):
        raise NotImplemented
    
    def display_message(self):
        raise NotImplemented
