# -*- coding: utf-8 -*-
import sys
import logging
from traceback import format_exception
from PyQt5.QtWidgets import QApplication
from ui.mainWindow import MainWindow
import resources_rc


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('wormsvisualiser.log')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                              "%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
logger.addHandler(fh)


def except_hook(type_, value, traceback):
    logger.error(value)
    logger.debug(format_exception(type_, value, traceback))
    sys.__excepthook__(type_, value, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication([])
    application = MainWindow()
    application.showMaximized()
    app.exec()
