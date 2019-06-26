# -*- coding: utf-8 -*-
import logging
from PyQt5.QtWidgets import QApplication
from ui.mainWindow import MainWindow
import resources_rc


logging.basicConfig(filename='wormsvisualiser.log', filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    try:
        app = QApplication([])
        application = MainWindow()
        application.show()
        app.exec()
    except Exception as e:
        logger.error(e)
