# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QGraphicsView, QTreeView, QAbstractItemView, QLabel, QTextBrowser, \
    QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from helpers import import_settings
from match.match import Match


class MatchViewGroup(QGroupBox):
    def __init__(self):
        super(MatchViewGroup, self).__init__()

        # Import settings
        self.settings = import_settings()

        self.current_match = Match()

        self.setTitle('Match View')

        # Layout
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.setColumnStretch(2, 1)

        # Moves tree
        self.moves_tree = QTreeView()
        self.moves_tree_model = QStandardItemModel()
        self.moves_tree.setModel(self.moves_tree_model)
        self.moves_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.moves_tree.setHeaderHidden(True)
        self.grid_layout.addWidget(self.moves_tree, 0, 0, 2, 1)

        """
        End game state info
        """
        self.end_game_state_info_group = QGroupBox()
        self.end_game_state_info_layout = QVBoxLayout()
        self.end_game_state_info_group.setLayout(self.end_game_state_info_layout)
        self.end_game_state_info_group.setTitle('Results')
        self.grid_layout.addWidget(self.end_game_state_info_group, 2, 0, 2, 1)
        # Results
        self.match_seed_label = QLabel()
        self.end_game_state_info_layout.addWidget(self.match_seed_label)
        self.match_winner_label = QLabel()
        self.end_game_state_info_layout.addWidget(self.match_winner_label)
        self.player_A_results_label = QLabel()
        self.end_game_state_info_layout.addWidget(self.player_A_results_label)
        self.player_B_results_label = QLabel()
        self.end_game_state_info_layout.addWidget(self.player_B_results_label)
        self.referee_messages_label = QLabel()
        self.referee_messages_label.setText('Referee Messages')
        self.end_game_state_info_layout.addWidget(self.referee_messages_label)
        self.referee_messages_text = QTextBrowser()
        self.end_game_state_info_layout.addWidget(self.referee_messages_text)

        # Map view
        self.map_view = QGraphicsView()
        self.grid_layout.addWidget(self.map_view, 1, 1, 1, 2)

        """
        Player A info
        """
        self.player_A_info_group = QGroupBox()
        self.player_A_info_layout = QGridLayout()
        self.player_A_info_group.setLayout(self.player_A_info_layout)
        self.player_A_info_group.setTitle('Player A')
        self.grid_layout.addWidget(self.player_A_info_group, 2, 1)
        # ID
        self.player_A_ID_label_ = QLabel()
        self.player_A_ID_label_.setText("ID: ")
        self.player_A_ID_label = QLabel()
        self.player_A_info_layout.addWidget(self.player_A_ID_label_, 0, 0)
        self.player_A_info_layout.addWidget(self.player_A_ID_label, 0, 1)
        # Score
        self.player_A_score_label_ = QLabel()
        self.player_A_score_label_.setText('Score: ')
        self.player_A_score_label = QLabel()
        self.player_A_info_layout.addWidget(self.player_A_score_label_, 1, 0)
        self.player_A_info_layout.addWidget(self.player_A_score_label, 1, 1)
        # Health
        self.player_A_health_label_ = QLabel()
        self.player_A_health_label_.setText('Health: ')
        self.player_A_health_label = QLabel()
        self.player_A_info_layout.addWidget(self.player_A_health_label_, 2, 0)
        self.player_A_info_layout.addWidget(self.player_A_health_label, 2, 1)
        # Current worm ID
        self.player_A_worm_id_label_ = QLabel()
        self.player_A_worm_id_label_.setText("Current worm ID: ")
        self.player_A_worm_id_label = QLabel()
        self.player_A_info_layout.addWidget(self.player_A_worm_id_label_, 3, 0)
        self.player_A_info_layout.addWidget(self.player_A_worm_id_label, 3, 1)
        # Remaining worm selections
        self.player_A_remaining_worms_selections_label_ = QLabel()
        self.player_A_remaining_worms_selections_label_.setText('Remaining worm selections: ')
        self.player_A_remaining_worms_selections_label = QLabel()
        self.player_A_info_layout.addWidget(self.player_A_remaining_worms_selections_label_, 4, 0)
        self.player_A_info_layout.addWidget(self.player_A_remaining_worms_selections_label, 4, 1)

        """
        Player A worms info
        """
        self.player_A_worms_info_group = QGroupBox()
        self.player_A_worms_info_group.setTitle('Worms')
        self.grid_layout.addWidget(self.player_A_worms_info_group, 3, 1)

        """
        Player B info
        """
        self.player_B_info_group = QGroupBox()
        self.player_B_info_layout = QGridLayout()
        self.player_B_info_group.setLayout(self.player_B_info_layout)
        self.player_B_info_group.setTitle('Player B')
        self.grid_layout.addWidget(self.player_B_info_group, 2, 2)
        # ID
        self.player_B_ID_label_ = QLabel()
        self.player_B_ID_label_.setText("ID: ")
        self.player_B_ID_label = QLabel()
        self.player_B_info_layout.addWidget(self.player_B_ID_label_, 0, 0)
        self.player_B_info_layout.addWidget(self.player_B_ID_label, 0, 1)
        # Score
        self.player_B_score_label_ = QLabel()
        self.player_B_score_label_.setText('Score: ')
        self.player_B_score_label = QLabel()
        self.player_B_info_layout.addWidget(self.player_B_score_label_, 1, 0)
        self.player_B_info_layout.addWidget(self.player_B_score_label, 1, 1)
        # Health
        self.player_B_health_label_ = QLabel()
        self.player_B_health_label_.setText('Health: ')
        self.player_B_health_label = QLabel()
        self.player_B_info_layout.addWidget(self.player_B_health_label_, 2, 0)
        self.player_B_info_layout.addWidget(self.player_B_health_label, 2, 1)
        # Current worm ID
        self.player_B_worm_id_label_ = QLabel()
        self.player_B_worm_id_label_.setText("Current worm ID: ")
        self.player_B_worm_id_label = QLabel()
        self.player_B_info_layout.addWidget(self.player_B_worm_id_label_, 3, 0)
        self.player_B_info_layout.addWidget(self.player_B_worm_id_label, 3, 1)
        # Remaining worm selections
        self.player_B_remaining_worms_selections_label_ = QLabel()
        self.player_B_remaining_worms_selections_label_.setText('Remaining worm selections: ')
        self.player_B_remaining_worms_selections_label = QLabel()
        self.player_B_info_layout.addWidget(self.player_B_remaining_worms_selections_label_, 4, 0)
        self.player_B_info_layout.addWidget(self.player_B_remaining_worms_selections_label, 4, 1)

        """
        Player B worms info
        """
        self.player_B_worms_info_group = QGroupBox()
        self.player_B_worms_info_group.setTitle('Worms')
        self.grid_layout.addWidget(self.player_B_worms_info_group, 3, 2)

        """
        Match info
        """
        self.match_info_group = QGroupBox()
        self.match_info_layout = QGridLayout()
        self.match_info_group.setLayout(self.match_info_layout)
        self.match_info_group.setTitle('Match Info')
        self.grid_layout.addWidget(self.match_info_group, 0, 1, 1, 1)
        # Current round
        self.current_round_label_ = QLabel()
        self.current_round_label_.setText('Current round: ')
        self.current_round_label = QLabel()
        self.match_info_layout.addWidget(self.current_round_label_, 0, 0)
        self.match_info_layout.addWidget(self.current_round_label, 0, 1)
        # Max rounds
        self.max_rounds_label_ = QLabel()
        self.max_rounds_label_.setText('Max rounds: ')
        self.max_rounds_label = QLabel()
        self.match_info_layout.addWidget(self.max_rounds_label_, 1, 0)
        self.match_info_layout.addWidget(self.max_rounds_label, 1, 1)
        # Pushback damage
        self.pushback_damage_label_ = QLabel()
        self.pushback_damage_label_.setText('Pushback damage: ')
        self.pushback_damage_label = QLabel()
        self.match_info_layout.addWidget(self.pushback_damage_label_, 2, 0)
        self.match_info_layout.addWidget(self.pushback_damage_label, 2, 1)
        # Map size
        self.map_size_label_ = QLabel()
        self.map_size_label_.setText('Map size: ')
        self.map_size_label = QLabel()
        self.match_info_layout.addWidget(self.map_size_label_, 3, 0)
        self.match_info_layout.addWidget(self.map_size_label, 3, 1)
        # Consecutive do nothing count
        self.consecutive_do_nothing_count_label_ = QLabel()
        self.consecutive_do_nothing_count_label_.setText('Consecutive do-nothing count: ')
        self.consecutive_do_nothing_count_label = QLabel()
        self.match_info_layout.addWidget(self.consecutive_do_nothing_count_label_, 4, 0)
        self.match_info_layout.addWidget(self.consecutive_do_nothing_count_label, 4, 1)

        """
        Move info
        """
        self.move_info_group = QGroupBox()
        self.move_info_layout = QGridLayout()
        self.move_info_group.setLayout(self.move_info_layout)
        self.move_info_group.setTitle('Move Info')
        self.grid_layout.addWidget(self.move_info_group, 0, 2, 1, 1)
        # Player
        self.move_info_player_label_ = QLabel()
        self.move_info_player_label_.setText('Player: ')
        self.move_info_player_label = QLabel()
        self.move_info_layout.addWidget(self.move_info_player_label_, 0, 0)
        self.move_info_layout.addWidget(self.move_info_player_label, 0, 1)
        # Command
        self.move_info_command_label_ = QLabel()
        self.move_info_command_label_.setText('Command: ')
        self.move_info_command_label = QLabel()
        self.move_info_layout.addWidget(self.move_info_command_label_, 1, 0)
        self.move_info_layout.addWidget(self.move_info_command_label, 1, 1)
        # Execution time
        self.move_info_execution_time_label_ = QLabel()
        self.move_info_execution_time_label_.setText('Execution time: ')
        self.move_info_execution_time_label = QLabel()
        self.move_info_layout.addWidget(self.move_info_execution_time_label_, 2, 0)
        self.move_info_layout.addWidget(self.move_info_execution_time_label, 2, 1)
        # Exception
        self.move_info_exception_label_ = QLabel()
        self.move_info_exception_label_.setText('Exception: ')
        self.move_info_exception_label = QLabel()
        self.move_info_layout.addWidget(self.move_info_exception_label_, 3, 0)
        self.move_info_layout.addWidget(self.move_info_exception_label, 3, 1)

    def match_selected(self, *args):
        match = args[0].indexes()[0].data()
        match_logs_directory = self.settings.value('match_logs_directory')
        directory = os.path.join(match_logs_directory, match)
        if os.path.isdir(directory):
            self.load_match(directory)

    def move_selected(self, *args):
        index_array = args[0].indexes()
        if len(index_array):
            index = index_array[0]
            if index.child(0, 0).isValid():
                self.moves_tree.setCurrentIndex(index.child(0, 0))
            else:
                self.current_match.set_current_move(index.parent().data(), index.data())
                self.update_round_info()
        else:
            self.current_match.set_current_move(None, None)
            self.update_round_info()

    def load_match(self, directory):
        self.current_match = Match(directory)
        self.list_rounds()
        self.update_end_game_state()

    def update_end_game_state(self):
        results = self.current_match.end_game_state
        self.match_seed_label.setText(results['seed'])
        self.match_winner_label.setText(results['winner'])
        self.player_A_results_label.setText(results['playerA'])
        self.player_B_results_label.setText(results['playerB'])
        self.referee_messages_text.setText(results['referee'])

    def list_rounds(self):
        match_directory = self.current_match.match_directory
        model = self.moves_tree_model
        model.removeRows(0, model.rowCount())
        rounds = [round_ for round_ in os.listdir(match_directory) if 'Round' in round_ and
                  os.path.isdir(os.path.join(match_directory))]
        for round_ in rounds:
            item = QStandardItem(round_)
            players = [player for player in os.listdir(os.path.join(match_directory, round_))
                       if 'endGameState' not in player]
            for player in players:
                child = QStandardItem(player)
                item.appendRow(child)
            model.appendRow(item)

    def update_round_info(self):
        move_state = self.current_match.current_state

        # Match info
        self.current_round_label.setText(str(move_state['currentRound']))
        self.max_rounds_label.setText(str(move_state['maxRounds']))
        self.pushback_damage_label.setText(str(move_state['pushbackDamage']))
        self.map_size_label.setText(str(move_state['mapSize']))
        self.consecutive_do_nothing_count_label.setText(str(move_state['consecutiveDoNothingCount']))

        # Player A info
        if self.current_match.current_player.split(' - ')[0] == 'A':
            player_info = move_state['myPlayer']
        else:
            player_info = move_state['opponents'][0]
            player_info['health'] = ''
        self.player_A_ID_label.setText(str(player_info['id']))
        self.player_A_score_label.setText(str(player_info['score']))
        self.player_A_health_label.setText(str(player_info['health']))
        self.player_A_worm_id_label.setText(str(player_info['currentWormId']))
        self.player_A_remaining_worms_selections_label.setText(str(player_info['remainingWormSelections']))

        # Player A worms info

        # Player B info
        if self.current_match.current_player.split(' - ')[0] == 'B':
            player_info = move_state['myPlayer']
        else:
            player_info = move_state['opponents'][0]
            player_info['health'] = ''
        self.player_B_ID_label.setText(str(player_info['id']))
        self.player_B_score_label.setText(str(player_info['score']))
        self.player_B_health_label.setText(str(player_info['health']))
        self.player_B_worm_id_label.setText(str(player_info['currentWormId']))
        self.player_B_remaining_worms_selections_label.setText(str(player_info['remainingWormSelections']))

        # Player B worms info

        # Move info
        self.move_info_player_label.setText(self.current_match.current_player)
        self.move_info_command_label.setText(self.current_match.move_info['command'])
        self.move_info_execution_time_label.setText(self.current_match.move_info['time'])
        self.move_info_exception_label.setText(self.current_match.move_info['exception'])
