# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QListView, QLineEdit, QPushButton, QAbstractItemView
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSignal
from helpers import import_settings


class MatchLogGroup(QGroupBox):
    """
    MatchLogGroup
    """
    def __init__(self):
        super(MatchLogGroup, self).__init__()

        # Import settings
        self.settings = import_settings()

        self.setTitle('Match Logs')

        # Layout
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        # Match log line edit
        self.current_directory_line = QLineEdit()
        self.current_directory_line.setText(self.settings.value('match_logs_directory'))
        self.current_directory_line.setReadOnly(True)
        self.grid_layout.addWidget(self.current_directory_line, 0, 0)

        # Match logs select button
        self.select_new_directory_button = QPushButton()
        self.select_new_directory_button.setIcon(QIcon(':resources/icons/main/icons8-folder-32.png'))
        self.grid_layout.addWidget(self.select_new_directory_button, 0, 1)

        # Match logs
        self.match_logs_list = QListView()
        self.match_logs_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.match_logs_list.setSelectionRectVisible(True)
        self.grid_layout.addWidget(self.match_logs_list, 1, 0, 1, 2)
        self.match_logs_list_model = QStandardItemModel()
        self.match_logs_list.setModel(self.match_logs_list_model)

        self.load_matches()

    def load_matches(self):
        directory = self.settings.value('match_logs_directory')
        names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
        for name in names:
            item = QStandardItem(name)
            self.match_logs_list_model.appendRow(item)
