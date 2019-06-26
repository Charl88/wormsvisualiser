# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QLabel, QMenu, QStatusBar, QMenuBar, QAction, QGridLayout, QWidget
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon

from helpers import import_settings

from ui.matchLogGroup import MatchLogGroup
from ui.matchViewGroup import MatchViewGroup


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        """
        Initialise the MainWindow
        """
        super(MainWindow, self).__init__(*args, **kwargs)

        # Import settings
        self.settings = import_settings()

        self.setWindowTitle('Worms Visualiser')
        self.setWindowIcon(QIcon(':resources/icons/main/worms.png'))
        self.setGeometry(200, 200, 1200, 600)

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
        self.menu_bar.setGeometry(QRect(0, 0, 800, 21))
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

        # Match logs
        self.match_log_group = MatchLogGroup()

        # Match view
        self.match_view_group = MatchViewGroup()

        # Layout
        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.addWidget(self.match_log_group, 0, 0)
        self.grid_layout.addWidget(self.match_view_group, 0, 1)

        # Central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)

        """ 
        Signals 
        """
        # Signal when a new match is selected
        self.match_log_group.match_logs_list.selectionModel().selectionChanged.connect(
            self.match_view_group.match_selected)

        # Signal when a new round is selected
        self.match_view_group.moves_tree.selectionModel().selectionChanged.connect(
            self.match_view_group.move_selected)
