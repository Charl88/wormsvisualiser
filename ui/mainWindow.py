# -*- coding: utf-8 -*-
import json

from PyQt5.QtWidgets import QMainWindow, QLabel, QMenu, QStatusBar, QMenuBar, QAction, QGridLayout, QWidget
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon

from settings import import_settings

from ui.groups.matchLogGroup import MatchLogGroup
from ui.groups.matchViewGroup import MatchViewGroup

groupType = {
    'MatchLogGroup': MatchLogGroup,
    'MatchViewGroup': MatchViewGroup,
}


class MainWindow(QMainWindow):
    def __init__(self, ui_template_path, *args, **kwargs):
        """
        Initialise the MainWindow
        """
        super(MainWindow, self).__init__(*args, **kwargs)

        # Import settings
        self.ui_template = json.load(open(ui_template_path, 'r'))
        self.settings = import_settings()

        self.setWindowTitle('Worms Visualiser')
        self.setWindowIcon(QIcon(':resources/icons/main/worm.png'))
        self.setGeometry(350, 40, 1200, 980)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        # Error message on the right of the status bar
        self.error_label = QLabel()
        self.error_label.setStyleSheet('color: darkred')
        self.status_bar.addPermanentWidget(self.error_label)

        # Menu bar
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        # self.menu_bar.setGeometry(QRect(0, 0, 800, 21))
        # File menu
        self.menu_file = QMenu()
        self.menu_file.setTitle('File')
        self.menu_bar.addAction(self.menu_file.menuAction())
        # File menu --> Exit
        self.exit_action = QAction()
        self.exit_action.setIcon(QIcon(':resources/icons/menu/icons8-exit-32.png'))
        self.exit_action.triggered.connect(self.close)
        self.exit_action.setText('Exit')
        self.exit_action.setStatusTip('Exit the application')
        self.menu_file.addAction(self.exit_action)

        # Layout
        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnStretch(1, 1)

        # Central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

        """
        Groups
        """
        self.groups = {}
        for group in self.ui_template['groups']:
            group_object = groupType[group['type']](group)
            self.groups[group['name']] = group_object
            self.grid_layout.addWidget(group_object, group['row'], group['col'])

        """ 
        Signals 
        """
        self.groups['match_log_group'].select_new_directory_button.clicked.connect(
            self.groups['match_log_group'].change_directory
        )
        self.groups['match_log_group'].match_logs_list.selectionModel().selectionChanged.connect(
            self.groups['match_view_group'].match_selected
        )
        self.groups['match_log_group'].refresh_directory_button.clicked.connect(
            self.groups['match_log_group'].directory_refreshed
        )
        self.groups['match_view_group'].rounds_list.selectionModel().selectionChanged.connect(
            self.groups['match_view_group'].round_selected
        )
