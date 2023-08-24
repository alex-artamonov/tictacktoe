#!/usr/bin/env python
import cli as c
import game as gm

# import simple as sm


def start_game():
    ui = c.Cli()
    game = gm.Gameplay(ui)
    game.greeting()
    game.initialize_game()


if __name__ == "__main__":
    start_game()
