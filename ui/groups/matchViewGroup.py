# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QListView, QAbstractItemView, QLabel, QTextBrowser, \
    QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QFont
from settings import import_settings
from match.match import Match

IMAGE = {
    'DEEP_SPACE': ':resources/icons/map/space.png',
    'AIR': ':resources/icons/map/air.png',
    'DIRT': ':resources/icons/map/dirt.png',
    'HEALTH_PACK': ':resources/icons/map/powerup-health.png'
}

PIXEL_SIZE = 18


class MatchViewGroup(QGroupBox):
    def __init__(self, ui_template):
        super(MatchViewGroup, self).__init__()

        """
        Import settings
        """
        self.ui_template = ui_template
        self.settings = import_settings()

        self.current_match = Match()

        self.setTitle('Match View')

        """
        Layout
        """
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.setColumnStretch(2, 1)
        self.grid_layout.setColumnStretch(3, 1)
        self.grid_layout.setRowStretch(1, 1)

        """
        Rounds list
        """
        self.rounds_list = QListView()
        self.rounds_list_model = QStandardItemModel()
        self.rounds_list.setModel(self.rounds_list_model)
        self.rounds_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.grid_layout.addWidget(self.rounds_list, 0, 0, 2, 1)

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
        self.map_scene = QGraphicsScene()
        self.map_view.setScene(self.map_scene)
        self.grid_layout.addWidget(self.map_view, 1, 1, 2, 2)

        # Add groups and field labels to the match view
        self.groups = {}
        self.populate_fields(self.ui_template, self.grid_layout)

    def populate_fields(self, template, layout, i=0):
        groups = template['groups']
        for group_ in groups:
            group = QGroupBox()
            group.setTitle(group_['title'])
            layout_ = QGridLayout()
            layout_.setSpacing(0)
            group.setLayout(layout_)
            self.groups[group_['name']] = group
            coordinates = [i, 0]
            span = [1, 1]
            if 'row' in group_ and 'col' in group_:
                coordinates = [group_['row'], group_['col']]
            if 'colSpan' in group_ or 'rowSpan' in group_:
                span = [group_.get('rowSpan', 1), group_.get('colSpan', 1)]
            layout.addWidget(group, *coordinates, *span)
            group.fields = {}
            if 'fields' in group_:
                for index, field_ in enumerate(group_['fields']):
                    if field_['name'] == 'worm':
                        field = QLabel()
                        field.setPixmap(QPixmap(field_['resource']))
                        layout_.addWidget(field, index-1, 0)
                    else:
                        field_label = QLabel()
                        field_label.setText(field_['label'])
                        field = QLabel()
                        if field_['label'] != '':
                            group.fields[field_['name']] = field
                            layout_.addWidget(field_label, index, 0)
                            layout_.addWidget(field, index, 1)
                        else:
                            group.fields[field_['name']] = field
                            layout_.addWidget(field, index, 1)
            if 'groups' in group_:
                self.populate_fields(group_, layout_, index + 1)

    def match_selected(self, *args):
        match = args[0].indexes()[0].data()
        match_logs_directory = self.settings.value('match_logs_directory')
        directory = os.path.join(match_logs_directory, match)
        self.map_scene.clear()
        if os.path.isdir(directory):
            self.load_match(directory)

    def round_selected(self, *args):
        index_array = args[0].indexes()
        if len(index_array):
            index = index_array[0]
            self.current_match.set_current_round(index.data())
            self.update_fields()
            self.draw_map()

    def draw_map(self):
        cells = self.current_match.current_round.state['map']
        self.map_scene.clear()
        self.map_scene.setSceneRect(0, 0, self.current_match.state['mapSize'] * PIXEL_SIZE,
                                    self.current_match.state['mapSize'] * PIXEL_SIZE)
        for row in cells:
            for cell in row:
                pic = QPixmap(IMAGE[cell['type']])
                item = self.map_scene.addPixmap(pic.scaled(PIXEL_SIZE, PIXEL_SIZE))
                item.setPos(cell['x'] * PIXEL_SIZE, cell['y'] * PIXEL_SIZE)
                if 'occupier' in cell:
                    if cell['occupier']['playerId'] == 1:
                        pic = QPixmap(':resources/icons/map/wormA.png')
                    else:
                        pic = QPixmap(':resources/icons/map/wormB.png')
                    item = self.map_scene.addPixmap(pic.scaled(PIXEL_SIZE, PIXEL_SIZE))
                    item.setPos(cell['x'] * PIXEL_SIZE, cell['y'] * PIXEL_SIZE)
                    health_label = QLabel()
                    font = QFont()
                    font.setBold(True)
                    health_label.setFont(font)
                    health_label.setText(str(cell['occupier']['id']) + ' - ' + str(cell['occupier']['health']))
                    item = self.map_scene.addWidget(health_label)
                    item.setPos((cell['x'] - 0.5) * PIXEL_SIZE, (cell['y'] - 1) * PIXEL_SIZE)
                if 'powerup' in cell:
                    pic = QPixmap(IMAGE[cell['powerup']['type']])
                    item = self.map_scene.addPixmap(pic.scaled(PIXEL_SIZE, PIXEL_SIZE))
                    item.setPos(cell['x'] * PIXEL_SIZE, cell['y'] * PIXEL_SIZE)

    def load_match(self, directory):
        self.current_match = Match(directory)
        self.list_rounds()
        self.update_end_game_state()
        self.rounds_list.setCurrentIndex(self.rounds_list_model.index(0, 0))

    def update_end_game_state(self):
        results = self.current_match.end_game_state
        self.match_seed_label.setText(results['seed'])
        self.match_winner_label.setText(results['winner'])
        self.player_A_results_label.setText(results['playerA'])
        self.player_B_results_label.setText(results['playerB'])
        self.referee_messages_text.setText(results['referee'])

    def list_rounds(self):
        match_directory = self.current_match.match_directory
        model = self.rounds_list_model
        model.clear()
        rounds = [round_ for round_ in os.listdir(match_directory) if 'Round' in round_ and
                  os.path.isdir(os.path.join(match_directory))]
        for round_ in rounds:
            item = QStandardItem(round_)
            model.appendRow(item)

    def update_fields(self):
        for group_key, group in self.groups.items():
            if group_key == 'match_info_group':
                state = self.current_match.state
                self.update_labels(group, state)
            if 'player_A_move_info' in group_key:
                temp = [value for key, value in self.current_match.current_round.player_command.items() if 'A -' in key]
                self.update_labels(group, temp[0])
            if 'player_B_move_info' in group_key:
                temp = [value for key, value in self.current_match.current_round.player_command.items() if 'B -' in key]
                self.update_labels(group, temp[0])
            if group_key == 'player_A_info_group':
                temp = [value for key, value in self.current_match.current_round.state.items() if 'A - ' in key]
                self.update_labels(group, temp[0])
            if group_key == 'player_B_info_group':
                temp = [value for key, value in self.current_match.current_round.state.items() if 'B - ' in key]
                self.update_labels(group, temp[0])
            if group_key == 'player_A_worms_info_group':
                players = [player for player in self.current_match.players]
                self.populate_worms_info(group, players[0])
            if group_key == 'player_B_worms_info_group':
                self.populate_worms_info(group, players[1])

    @staticmethod
    def update_labels(group, state):
        for field_key, field in group.fields.items():
            field.setText(str(state[field_key]))
            if field_key == 'colour':
                field.setIcon()

    def populate_worms_info(self, group, player):
        # Clears the layout before re-adding worms info
        for i in reversed(range(group.layout().count())):
            group.layout().itemAt(i).widget().setParent(None)
        worms = self.current_match.current_round.state[player]['worms']
        for worm in worms:
            wormGroup = QGroupBox()
            wormGroup_layout = QGridLayout()
            wormGroup_layout.setSpacing(0)
            wormGroup.setLayout(wormGroup_layout)
            group.layout().addWidget(wormGroup)
            for index, (key, value) in enumerate(worm.items()):
                label_ = QLabel()
                label_.setText(key + ': ')
                label = QLabel()
                label.setText(str(value))
                wormGroup_layout.addWidget(label_, index, 0)
                wormGroup_layout.addWidget(label, index, 1)
