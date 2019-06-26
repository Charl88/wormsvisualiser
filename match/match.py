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
        self.current_player = None
        self.move_info = None
        self.end_game_state = None

        if match_directory:
            self.match_directory = match_directory
            self.players = self.get_players()
            self.rounds = self.get_rounds()
            self.end_game_state = self.parse_end_game_state()

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
            self.current_player = player
            self.move_info = self.parse_command(round_, player)
        else:
            self.current_state = None

    def parse_command(self, round_, player):
        command = {}
        file_path = os.path.join(self.match_directory, round_, player, 'PlayerCommand.txt')
        file = open(file_path, 'r')
        command['command'] = file.readline().strip().split(': ')[1]
        command['time'] = file.readline().strip().split(': ')[1]
        command['exception'] = file.readline().strip().split(': ')[1]
        file.close()
        return command

    def parse_end_game_state(self):
        end_game_state = {}
        rounds = [round_ for round_ in self.rounds]
        file_path = os.path.join(self.match_directory, rounds[-1], 'endGameState.txt')
        file = open(file_path, 'r')
        end_game_state['seed'] = file.readline().strip()
        file.readline()
        end_game_state['winner'] = file.readline().strip()
        file.readline()
        end_game_state['playerA'] = file.readline().strip()
        end_game_state['playerB'] = file.readline().strip()
        file.readline()
        file.readline()
        file.readline()
        end_game_state['referee'] = ''
        for line in file:
            end_game_state['referee'] += line
        file.close()
        return end_game_state












