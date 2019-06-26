# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QGraphicsView, QTreeView, QAbstractItemView
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
        self.grid_layout.addWidget(self.moves_tree, 1, 0, 3, 1)

        # Map view
        self.map_view = QGraphicsView()
        self.grid_layout.addWidget(self.map_view, 1, 1, 1, 2)

        # Player A info
        self.player_A_info_group = QGroupBox()
        self.player_A_info_group.setTitle('Player A')
        self.grid_layout.addWidget(self.player_A_info_group, 2, 1)

        # Player A worms info
        self.player_A_worms_info_group = QGroupBox()
        self.player_A_worms_info_group.setTitle('Worms')
        self.grid_layout.addWidget(self.player_A_worms_info_group, 3, 1)

        # Player B info
        self.player_B_info_group = QGroupBox()
        self.player_B_info_group.setTitle('Player B')
        self.grid_layout.addWidget(self.player_B_info_group, 2, 2)

        # Player B worms info
        self.player_B_worms_info_group = QGroupBox()
        self.player_B_worms_info_group.setTitle('Worms')
        self.grid_layout.addWidget(self.player_B_worms_info_group, 3, 2)

        # Match info
        self.match_info_group = QGroupBox()
        self.match_info_group.setTitle('Match')
        self.grid_layout.addWidget(self.match_info_group, 0, 1)

        # Round info
        self.round_info_group = QGroupBox()
        self.round_info_group.setTitle('Round')
        self.grid_layout.addWidget(self.round_info_group, 0, 2)

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
        else:
            self.current_match.set_current_move(None, None)

    def load_match(self, directory):
        self.current_match = Match(directory)
        self.list_rounds()

    def list_rounds(self):
        match_directory = self.current_match.match_directory
        model = self.moves_tree_model
        model.removeRows(0, model.rowCount())
        rounds = [round_ for round_ in os.listdir(match_directory) if 'Round' in round_ and
                  os.path.isdir(os.path.join(match_directory))]
        for round_ in rounds:
            item = QStandardItem(round_)
            players = os.listdir(os.path.join(match_directory, round_))
            for player in players:
                child = QStandardItem(player)
                item.appendRow(child)
            model.appendRow(item)



