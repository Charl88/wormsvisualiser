# -*- coding: utf-8 -*-
import os
from .player import Player
from .round import Round


class Match:
    def __init__(self, match_directory=None):
        # Define all initial variables to None so that our UI can display empty labels
        self.error = None
        self.match_directory = None
        self.players = None
        self.rounds = None
        self.current_state = None

        if match_directory:
            self.match_directory = match_directory
            self.players = self.get_players()
            self.rounds = self.get_rounds()

    def get_players(self):
        players = {player.split('.')[0]: Player(player, self) for player in os.listdir(self.match_directory)
                   if '.csv' in player}
        return players

    def get_rounds(self):
        return_obj = {}
        rounds = [Round(round_, self) for round_ in os.listdir(self.match_directory)
                  if 'Round' in round_ and os.path.isdir(os.path.join(self.match_directory, round_))]
        if len(rounds) > 0:
            for round_ in rounds:
                return_obj[round_.name] = round_
            return return_obj
        else:
            return {}

    def set_current_move(self, round_, player):
        if round_ is not None or player is not None:
            self.current_state = self.rounds[round_].states[player]
        else:
            self.current_state = None











