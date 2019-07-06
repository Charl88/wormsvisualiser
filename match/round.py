# -*- coding: utf-8 -*-
import os
import json


class Round:
    def __init__(self, round_folder, match):
        self.name = round_folder
        self.match = match
        self.state = self.load_json_states(os.path.join(match.match_directory, round_folder))
        self.player_command = {}
        for key, value in self.match.players.items():
            self.player_command[key] = self.parse_command(round_folder, key)

    def load_json_states(self, round_folder):
        states = {}
        state_files = {player: os.path.join(round_folder, player, 'JsonMap.json')
                       for index, player in enumerate(self.match.players)}
        for player, state_file in state_files.items():
            try:
                temp = json.load(open(state_file, 'r'))
                states[player] = temp.pop('myPlayer')
                states[player]['consecutiveDoNothingCount'] = temp.pop('consecutiveDoNothingCount')
                temp.pop('opponents')
                states['map'] = temp.pop('map')
                self.match.state = temp
            except IOError:
                raise IOError('Could not parse JsonMap.json')
        return states

    def parse_command(self, round_, player):
        command = {}
        file_path = os.path.join(self.match.match_directory, round_, player, 'PlayerCommand.txt')
        file = open(file_path, 'r')
        command['player'] = player.split(' - ')[1]
        command['command'] = file.readline().strip().split(': ')[1]
        command['time'] = file.readline().strip().split(': ')[1]
        command['exception'] = file.readline().strip().split(': ')[1]
        file.close()
        command['consecutiveDoNothingCount'] = self.state[player]['consecutiveDoNothingCount']
        return command
