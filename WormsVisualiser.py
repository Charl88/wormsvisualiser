# -*- coding: utf-8 -*-
import sys
import os
import logging
from traceback import format_exception
from PyQt5.QtWidgets import QApplication
from ui.mainWindow import MainWindow
import resources_rc


logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                 '%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('wormsvisualiser.log')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)


def except_hook(type_, value, traceback):
    logger.error(value)
    logger.debug(format_exception(type_, value, traceback))
    sys.__excepthook__(type_, value, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication([])
    ui_template_path = os.path.join('ui', 'ui.json')
    application = MainWindow(ui_template_path)
    application.showMaximized()
    app.exec()
