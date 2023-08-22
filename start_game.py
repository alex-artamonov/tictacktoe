from sys import exit
import os
import cli as c
import utils as u
import game as gm


def start_game():
    player_name = str(os.getlogin()).capitalize()
    game = gm.Gameplay(player_name)
    game.greeting()
    counter = game.get_moves_count()
    current_player = game.current_player
    current_move = game.current_move
    ui = c.Cli(game.computer_name, game.player_name, game.score)
    ui.display_field(game.field, 10, counter, current_player, current_move)
    game.initialize_game()

