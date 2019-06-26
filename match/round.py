# -*- coding: utf-8 -*-
import os
import json


class Round:
    def __init__(self, round_folder, match):
        self.error = None
        self.name = round_folder
        self.match = match
        self.states = self.load_json_states(os.path.join(match.match_directory, round_folder))

    def load_json_states(self, round_folder):
        states = {}
        state_files = {player: os.path.join(round_folder, player, 'JsonMap.json')
                       for index, player in enumerate(self.match.players)}
        for player, state_file in state_files.items():
            try:
                states[player] = json.load(open(state_file, 'r'))
            except IOError:
                self.error = 'Could not open JsonMap.json'
        return states
