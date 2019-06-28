# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QListView, QLineEdit, QPushButton, QAbstractItemView, QFileDialog
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from settings import import_settings


class MatchLogGroup(QGroupBox):
    """
    MatchLogGroup
    """
    def __init__(self, ui_template):
        super(MatchLogGroup, self).__init__()

        # Import settings
        self.ui_template = ui_template
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

        # Match logs refresh button
        self.refresh_directory_button = QPushButton()
        self.refresh_directory_button.setIcon(QIcon(':resources/icons/main/icons8-refresh-32.png'))
        self.grid_layout.addWidget(self.refresh_directory_button, 0, 2)

        # Match logs
        self.match_logs_list = QListView()
        self.match_logs_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.match_logs_list.setSelectionRectVisible(True)
        self.grid_layout.addWidget(self.match_logs_list, 1, 0, 1, 3)
        self.match_logs_list_model = QStandardItemModel()
        self.match_logs_list.setModel(self.match_logs_list_model)

        self.load_matches()

    def load_matches(self):
        directory = self.settings.value('match_logs_directory')
        if os.path.isdir(directory):
            names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
            for name in names:
                item = QStandardItem(name)
                self.match_logs_list_model.appendRow(item)

    def change_directory(self):
        self.match_logs_list_model.clear()
        directory = QFileDialog.getExistingDirectory(QFileDialog(), 'Select Directory')
        self.settings.setValue('match_logs_directory', directory)
        self.settings.sync()
        self.current_directory_line.setText(directory)
        self.load_matches()

    def directory_refreshed(self):
        self.match_logs_list_model.clear()
        self.load_matches()


